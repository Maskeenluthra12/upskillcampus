import pandas as pd

def predict_traffic(
    model,
    weather_encoder,
    holiday_encoder,
    temperature,
    weather,
    holiday,
    hour,
    day,
    month,
):
    weather_encoded = weather_encoder.transform([weather])[0]
    holiday_encoded = holiday_encoder.transform([holiday])[0]

    day_mapping = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6,
    }

    input_data = pd.DataFrame(
        [[
            temperature,
            weather_encoded,
            holiday_encoded,
            hour,
            day_mapping[day],
            month,
        ]],
        columns=[
            "Temperature",
            "Weather",
            "Holiday",
            "Hour",
            "Day",
            "Month",
        ],
    )

    return int(model.predict(input_data)[0])
