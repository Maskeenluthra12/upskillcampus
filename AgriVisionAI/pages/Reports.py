import streamlit as st
import pandas as pd
import tempfile
import datetime

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import darkgreen

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Reports",
    page_icon="📄",
    layout="wide"
)

st.title("AI Agricultural Report Generator")

st.write(
    "Generate professional agricultural reports using historical crop production data."
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = pd.read_csv("datasets/crop_production.csv")

# ---------------------------------------------------
# DROPDOWNS
# ---------------------------------------------------

state = st.selectbox(
    "Select State",
    sorted(df["State_Name"].unique())
)

crop = st.selectbox(
    "Select Crop",
    sorted(
        df[df["State_Name"] == state]["Crop"].unique()
    )
)

year = st.selectbox(
    "Select Year",
    sorted(
        df[
            (df["State_Name"] == state)
            &
            (df["Crop"] == crop)
        ]["Crop_Year"].unique()
    )
)

# ---------------------------------------------------
# FILTER DATA
# ---------------------------------------------------

filtered = df[
    (df["State_Name"] == state)
    &
    (df["Crop"] == crop)
    &
    (df["Crop_Year"] == year)
]

# ---------------------------------------------------
# PDF FUNCTION
# ---------------------------------------------------

def create_pdf(
    state,
    crop,
    year,
    production,
    area,
    yield_value
):

    styles = getSampleStyleSheet()

    title = styles["Heading1"]
    title.alignment = TA_CENTER
    title.textColor = darkgreen

    heading = styles["Heading2"]

    body = styles["BodyText"]

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    doc = SimpleDocTemplate(temp.name)

    story = []

    story.append(
        Paragraph(
            "AgriVision AI",
            title
        )
    )

    story.append(
        Paragraph(
            "Agricultural Intelligence Report",
            heading
        )
    )

    story.append(
        Paragraph(
            f"Generated on: {datetime.date.today()}",
            body
        )
    )

    story.append(Paragraph("<br/><br/>", body))

    story.append(
        Paragraph(
            "<b>Crop Details</b>",
            heading
        )
    )

    story.append(
        Paragraph(f"State : {state}", body)
    )

    story.append(
        Paragraph(f"Crop : {crop}", body)
    )

    story.append(
        Paragraph(f"Year : {year}", body)
    )

    story.append(Paragraph("<br/>", body))

    story.append(
        Paragraph(
            "<b>Production Statistics</b>",
            heading
        )
    )

    story.append(
        Paragraph(
            f"Production : {production:,.0f} tonnes",
            body
        )
    )

    story.append(
        Paragraph(
            f"Area : {area:,.0f} hectares",
            body
        )
    )

    story.append(
        Paragraph(
            f"Yield : {yield_value:.2f} tonnes/hectare",
            body
        )
    )

    story.append(Paragraph("<br/>", body))

    story.append(
        Paragraph(
            "<b>Performance Analysis</b>",
            heading
        )
    )

    analysis = f"""
The selected crop ({crop}) in {state} for the year {year}
covered an area of {area:,.0f} hectares and produced
{production:,.0f} tonnes.

The average productivity was
{yield_value:.2f} tonnes per hectare.

Historical data indicates that maintaining
proper irrigation, balanced fertilization,
and pest monitoring can further improve
overall productivity.
"""

    story.append(
        Paragraph(
            analysis,
            body
        )
    )

    story.append(Paragraph("<br/>", body))

    story.append(
        Paragraph(
            "<b>Recommendations</b>",
            heading
        )
    )

    recommendations = [

        "Use certified high-quality seeds.",

        "Conduct soil testing before fertilizer application.",

        "Use balanced nutrient management.",

        "Monitor pests and diseases regularly.",

        "Adopt crop rotation for better soil health.",

        "Use efficient irrigation methods.",

        "Follow weather forecasts before spraying."
    ]

    for rec in recommendations:

        story.append(
            Paragraph(
                f"• {rec}",
                body
            )
        )

    story.append(Paragraph("<br/>", body))

    story.append(
        Paragraph(
            "<b>Conclusion</b>",
            heading
        )
    )

    conclusion = """
Overall, the crop demonstrates satisfactory production
based on historical records.

Adopting precision agriculture practices,
efficient irrigation, and improved crop management
can further increase productivity and sustainability.
"""

    story.append(
        Paragraph(
            conclusion,
            body
        )
    )

    story.append(Paragraph("<br/><br/>", body))

    story.append(
        Paragraph(
            "Generated by AgriVision AI",
            heading
        )
    )

    doc.build(story)

    return temp.name


# ---------------------------------------------------
# GENERATE REPORT
# ---------------------------------------------------

if st.button(
    "Generate Report",
    use_container_width=True
):

    if filtered.empty:

        st.error("No records found.")

    else:

        production = filtered["Production"].sum()

        area = filtered["Area"].sum()

        yield_value = (
            production / area
            if area != 0
            else 0
        )

        st.success("Report Generated Successfully!")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Production",
            f"{production:,.0f}"
        )

        c2.metric(
            "Area",
            f"{area:,.0f}"
        )

        c3.metric(
            "Yield",
            f"{yield_value:.2f}"
        )

        st.divider()

        st.subheader("Summary")

        st.write(f"**State:** {state}")

        st.write(f"**Crop:** {crop}")

        st.write(f"**Year:** {year}")

        st.write(
            f"""
The selected crop produced **{production:,.0f} tonnes**
over **{area:,.0f} hectares**.

Average productivity was
**{yield_value:.2f} tonnes/hectare**.

Based on historical trends, maintaining
good irrigation, soil fertility,
crop rotation and pest management
can improve future production.
"""
        )

        pdf = create_pdf(

            state,

            crop,

            year,

            production,

            area,

            yield_value

        )

        with open(pdf, "rb") as file:

            st.download_button(

                "📄 Download PDF Report",

                file,

                file_name=f"{state}_{crop}_{year}_Report.pdf",

                mime="application/pdf",

                use_container_width=True
            )