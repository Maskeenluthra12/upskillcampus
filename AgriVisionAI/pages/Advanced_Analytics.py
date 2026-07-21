import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Advanced Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("Advanced Analytics")

st.write(
    "Explore agricultural production trends across India using interactive analytics."
)

st.divider()

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("datasets/crop_production.csv")

# ------------------------------------------
# Clean column names
# ------------------------------------------

df.columns = df.columns.str.strip()

# Rename columns (if required)

rename_dict = {
    "State_Name": "State",
    "District_Name": "District",
    "Crop_Year": "Year",
    "Season": "Season",
    "Crop": "Crop",
    "Area": "Area",
    "Production": "Production"
}

df.rename(columns=rename_dict, inplace=True)

# ------------------------------------------
# Remove missing values
# ------------------------------------------

df = df.dropna(
    subset=[
        "State",
        "Crop",
        "Year",
        "Production"
    ]
)

# Convert Production to numeric

df["Production"] = pd.to_numeric(
    df["Production"],
    errors="coerce"
)

df = df.dropna(subset=["Production"])

# ==========================================
# SIDEBAR FILTERS
# ==========================================

st.sidebar.header("Filters")

state = st.sidebar.selectbox(
    "State",
    sorted(df["State"].unique())
)

crop = st.sidebar.selectbox(
    "Crop",
    sorted(
        df[df["State"] == state]["Crop"].unique()
    )
)

filtered = df[
    (df["State"] == state)
    &
    (df["Crop"] == crop)
]

# ==========================================
# KPI CARDS
# ==========================================

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Total Production",
        f"{filtered['Production'].sum():,.0f}"
    )

with k2:

    st.metric(
        "Average Production",
        f"{filtered['Production'].mean():,.0f}"
    )

with k3:

    st.metric(
        "Years Available",
        filtered["Year"].nunique()
    )

with k4:

    st.metric(
        "Districts",
        filtered["District"].nunique()
    )

st.write("")
# =====================================================
# PRODUCTION TREND
# =====================================================

st.markdown("## Production Trend")

trend = (
    filtered
    .groupby("Year", as_index=False)["Production"]
    .sum()
)

fig1 = px.line(
    trend,
    x="Year",
    y="Production",
    markers=True,
    title="Production Over the Years"
)

fig1.update_layout(
    template="plotly_white",
    height=450,
    xaxis_title="Year",
    yaxis_title="Production"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.write("")

# =====================================================
# TOP DISTRICTS
# =====================================================

st.markdown("## Top Producing Districts")

districts = (
    filtered
    .groupby("District", as_index=False)["Production"]
    .sum()
    .sort_values(
        "Production",
        ascending=False
    )
    .head(10)
)

fig2 = px.bar(
    districts,
    x="District",
    y="Production",
    title="Top 10 Districts by Production"
)

fig2.update_layout(
    template="plotly_white",
    height=500,
    xaxis_title="District",
    yaxis_title="Production"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.write("")

# =====================================================
# PIE CHART
# =====================================================

left, right = st.columns(2)

with left:

    st.markdown("### Production Distribution")

    fig3 = px.pie(
        districts,
        names="District",
        values="Production",
        hole=0.45
    )

    fig3.update_layout(
        height=450
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# =====================================================
# AREA vs PRODUCTION
# =====================================================

with right:

    st.markdown("### Area vs Production")

    scatter = filtered.copy()

    scatter["Area"] = pd.to_numeric(
        scatter["Area"],
        errors="coerce"
    )

    scatter = scatter.dropna(
        subset=["Area"]
    )

    fig4 = px.scatter(
        scatter,
        x="Area",
        y="Production",
        color="Year",
        hover_data=["District"]
    )

    fig4.update_layout(
        height=450,
        template="plotly_white"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.write("")
# =====================================================
# ANALYTICS SUMMARY
# =====================================================

st.markdown("## Analytics Summary")

# Total Production
total_production = filtered["Production"].sum()

# Average Production
average_production = filtered["Production"].mean()

# Best District
district_summary = (
    filtered
    .groupby("District")["Production"]
    .sum()
)

best_district = district_summary.idxmax()
best_production = district_summary.max()

# Highest Production Year
year_summary = (
    filtered
    .groupby("Year")["Production"]
    .sum()
)

best_year = year_summary.idxmax()
best_year_production = year_summary.max()

# Growth %
growth = 0

if len(year_summary) > 1:

    first = year_summary.iloc[0]
    last = year_summary.iloc[-1]

    if first != 0:
        growth = ((last - first) / first) * 100

# =====================================================
# SUMMARY CARDS
# =====================================================

c1, c2 = st.columns(2)

with c1:

    st.success(f"""
### Best Performing District

**District:** {best_district}

**Production:** {best_production:,.0f}
""")

with c2:

    st.info(f"""
### Highest Production Year

**Year:** {best_year}

**Production:** {best_year_production:,.0f}
""")

st.write("")

# =====================================================
# GROWTH
# =====================================================

if growth >= 0:

    st.metric(
        "Overall Growth",
        f"{growth:.2f}%"
    )

else:

    st.metric(
        "Overall Growth",
        f"{growth:.2f}%"
    )

st.write("")

# =====================================================
# PRODUCTION TABLE
# =====================================================

st.markdown("## Production Summary")

summary = (
    filtered
    .groupby(["Year", "District"], as_index=False)
    .agg(
        Production=("Production", "sum"),
        Area=("Area", "sum")
    )
)

summary = summary.sort_values(
    ["Year", "Production"],
    ascending=[True, False]
)

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

st.write("")

# =====================================================
# QUICK INSIGHTS
# =====================================================

st.markdown("## Key Insights")

st.info(f"""

• Total Production: **{total_production:,.0f}**

• Average Production: **{average_production:,.0f}**

• Best District: **{best_district}**

• Highest Production Year: **{best_year}**

• Growth Rate: **{growth:.2f}%**

These insights are generated automatically based on the selected crop and state.

""")

st.write("")