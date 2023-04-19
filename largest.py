import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="Find the largest among 3 numbers", page_icon=":mag:")

# Add a title to the app
st.title("Find the largest among 3 numbers")

# Add a short description
st.markdown("This app will help you find the largest number among 3 given numbers.", 
            unsafe_allow_html=True)

# Create input fields for the 3 numbers
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
num3 = st.number_input("Enter the third number")

# Calculate the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the largest number in green color
st.write("The largest number is ", 
         "<span style='color:green; font-weight:bold;'>", largest, "</span>",
         unsafe_allow_html=True)
