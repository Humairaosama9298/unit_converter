import streamlit as st

def convert(value, from_unit, conversion_factors):
    return {unit: value * (conversion_factors[unit] / conversion_factors[from_unit]) for unit in conversion_factors if unit != from_unit}

categories = {
    "Length": {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371},
    "Weight": {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462},
    "Time": {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600},
    "Speed": {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694},
    "Temperature": {"Celsius": 1, "Fahrenheit": 33.8, "Kelvin": 274.15},
    "Area": {"Square Meters": 1, "Square Kilometers": 0.000001, "Acres": 0.000247105},
    "Volume": {"Liters": 1, "Milliliters": 1000, "Gallons": 0.264172},
    "Energy": {"Joules": 1, "Kilojoules": 0.001, "Calories": 0.239006},
    "Data Storage": {"Bytes": 1, "Kilobytes": 0.001, "Megabytes": 0.000001},
    "Fuel Efficiency": {"Kilometers per liter": 1, "Miles per gallon": 2.35215}
}

st.set_page_config(page_title="Unit Converter", layout="centered")
st.title(" Simple Unit Converter")

category = st.selectbox("Select category", list(categories.keys()))
units = list(categories[category].keys())
from_unit = st.selectbox("From", units)
value = st.number_input("Enter value", min_value=0, format="%d")

if st.button("Convert"):
    results = convert(value, from_unit, categories[category])
    for unit, result in results.items():
        st.success(f"{value} {from_unit} = {result:.2f} {unit}")