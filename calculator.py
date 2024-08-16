import streamlit as st

# Title of the calculator app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

# Select operation
operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate based on operation
if operation == "Add":
    result = num1 + num2
    st.write(f"The result of {num1} + {num2} is: {result}")
elif operation == "Subtract":
    result = num1 - num2
    st.write(f"The result of {num1} - {num2} is: {result}")
elif operation == "Multiply":
    result = num1 * num2
    st.write(f"The result of {num1} * {num2} is: {result}")
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
        st.write(f"The result of {num1} / {num2} is: {result}")
    else:
        st.write("Error! Division by zero.")

