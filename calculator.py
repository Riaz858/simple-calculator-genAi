import streamlit as st

# Custom CSS for amazing UI/UX
st.markdown("""
    <style>
    body {
        background-color: #1a1a1a;
        color: #f0f0f0;
        font-family: 'Arial', sans-serif;
    }
    h1 {
        text-align: center;
        color: #4CAF50;
    }
    .button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Amazing Calculator with Streamlit")

# Input fields
num1 = st.number_input("Enter the first number", key='num1')
num2 = st.number_input("Enter the second number", key='num2')

# Operation selection
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation based on operation
if st.button("Calculate", key='calculate'):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    st.success(f"Result: {result}")
