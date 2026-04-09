import streamlit as st

st.title("💪 BMI (Body Mass Index) Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=0.0, step=0.1, format="%.2f")
height = st.number_input("Enter your height (m):", min_value=0.0, step=0.01, format="%.2f")

if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")
    # Interpret the BMI value
    if bmi < 18.5:
        st.warning("You are Underweight 😕")
    elif 18.5 <= bmi < 25:
        st.info("You are Normal weight 😊")
    elif 25 <= bmi < 30:
        st.warning("You are Overweight 😐")
    else:
        st.error("You are Obese 😟")
else:
    st.write("Please enter valid weight and height values to calculate BMI.")
