import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (meters)."""
    bmi = weight / (height ** 2)
    return bmi

def main():
    st.title("BMI Calculator")

    # Input from user
    st.write("Enter your details to calculate BMI.")
    weight = st.number_input("Weight (kg)", min_value=0.0, step=0.1)
    height = st.number_input("Height (meters)", min_value=0.0, step=0.01)

    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.write(f"Your BMI is: {bmi:.2f}")

            # Health status based on BMI
            if bmi < 18.5:
                st.warning("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.success("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.warning("You are overweight.")
            else:
                st.error("You are obese.")
        else:
            st.error("Please enter valid weight and height.")

if __name__ == "__main__":
    main()
