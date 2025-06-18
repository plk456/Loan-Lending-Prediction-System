#print("jai sri ram")
import pickle
import numpy as np
import streamlit as st
from PIL import Image

#Loan_amout

with open('model.pkl','rb') as file:
    model=pickle.load(file)
st.header("this is a header")

st.title("this is a title")

loan_amount =st.text_input(" Loan amount")

int_rate =st.text_input("int_rate")

st.write('Please enter the interest rate in percentage (e.g., 5.5 or 5.5%)')
if int_rate.endswith('%'):
    int_rate = int_rate[:-1]

installment =st.text_input("installment")

grade=st.write('Please enter either "A", "B", "C", "D", "E", "F", or "G"')
if grade == "A" or "a":
    grade =0
elif grade == "B" or "b":
    grade =1
elif grade == "C" or "c":
    grade =2
elif grade == "D" or "d":
    grade =3
elif grade == "E" or "e":
    grade =4
elif grade == "F" or "f":
    grade =5
elif grade == "G" or "g":
    grade =6
else:
    st.write('thank you for your choice')
grade =st.text_input("grade")

emp_title =st.text_input("emp_title")

home_ownership =st.text_input("Either Rent, Own, or Mortgage")
if home_ownership == "Rent" or "rent":
    home_ownership =0
elif home_ownership == "Own" or "own":
    home_ownership =1
elif home_ownership == "Mortgage" or "mortgage":
    home_ownership =2
else:
    st.error('Please enter either "Rent", "Own", or "Mortgage"')


annual_inc =st.text_input("annual_inc")

dti =st.text_input("dti")

revol_balance=st.text_input("revol_balance")

total_acc =st.text_input("total_acc")

st.write('Please enter either "Individual application" or "Joint application"')
application=st.text_input("Application")
if application == "Individual application":
    application =0
elif application == "Joint application":
    application =1


if st.button("predict"):

    try:
        loan_amount = float(loan_amount)
        int_rate = float(int_rate)
        installment = float(installment)
        grade = int(grade)
        emp_title = int(emp_title)
        home_ownership = int(home_ownership)
        annual_inc = float(annual_inc)
        dti = float(dti)
        revol_balance = int(revol_balance)
        total_acc = int(total_acc)
        application = int(application)

    except ValueError as e:
        st.error(f"Invalid input: {e}")
        st.stop()

    # Create a DataFrame for prediction

    values = np.array([[loan_amount, int_rate, installment, grade, emp_title,
                       home_ownership, annual_inc, dti, revol_balance, total_acc, application]])
    prediction =model.predict(values)

    st.write("The predicted value is:", prediction[0])




