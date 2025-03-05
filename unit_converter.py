import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🌐", layout="wide")

# Add a header with a background color
st.markdown(
    """
    <style>
    .header {
        background-color: #4CAF50; 
        color: white; 
        padding: 40px; 
        text-align: center; 
        font-size: 24px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)
st.markdown('<div class="header"><h1>🌏🌐 Unit Converter</h1></div>', unsafe_allow_html=True)


def converter_units(value,unit_from,unit_to):

    conversions = {
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,  # 1 kilometer = 1000 meter
        "grams_kilograms": 0.001,   # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000     # 1 kilogram = 1000 gram
    }

    key = f"{unit_from}_{unit_to}" # Generate a key based on the input and output units

    if key in conversions : 
        conversion = conversions[key]
        return value * conversion
    
    else:
        return "Sorry, this conversion type is not supported."

st.title("Unit Coverter")

value = st.number_input("Enter the value: ", min_value=1.0, step=1.0)

unit_from = st.selectbox("Convert from: ", ["meters","kilometers","grams","kilograms"])

unit_to = st.selectbox("Convert to: ", ["kilograms","grams","kilometers","meters"])

if st.button("Convert"):
    result = converter_units(value,unit_from,unit_to)
    st.write(f"Converted value : {result}")






###Commands 

#uv init unit-converter
#cd unit-converter
#uv add streamlit 
#.venv\scripts\activate

