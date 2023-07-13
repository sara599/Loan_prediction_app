import streamlit as st
import pandas as pd
import joblib

#  import category_encoders  

 

Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")


def prediction(Gender,  Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, 
                            LoanAmount, Loan_Amount_Term , Credit_History, Property_Area,DTI ):
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"Gender"] = Gender
    test_df.at[0,"Married"] = Married
    test_df.at[0,"Dependents"] = Dependents
    test_df.at[0,"Education"] = Education
    test_df.at[0,"Self_Employed"] = Self_Employed
    test_df.at[0,"ApplicantIncome"] = ApplicantIncome
    test_df.at[0,"CoapplicantIncome"] = CoapplicantIncome
    test_df.at[0,"LoanAmount"] = LoanAmount
    test_df.at[0,"Loan_Amount_Term"] = Loan_Amount_Term
    test_df.at[0,"Credit_History"] = Credit_History
    test_df.at[0,"Property_Area"] = Property_Area
    test_df.at[0,"DTI"] = DTI
 
 
    
    st.dataframe(test_df)
    result = Model.predict(test_df)[0]
    return result


def main():
    # ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
    #    'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
    #    'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'DTI']
    
    st.title("Loan Prediction ")
    Gender = st.selectbox("Gender" , ['Male', 'Female'])
    Married = st.selectbox("Married" , ['Yes', 'No'] )
    Dependents = st.selectbox("Dependents" , ['1', '0', '2', '3+'] )
    Education = st.selectbox("Education" , ['Graduate', 'Not Graduate'] )
    Self_Employed = st.selectbox("Self_Employed" , ['No', 'Yes'] )
    ApplicantIncome = st.text_input("Applicant Income")
    CoapplicantIncome = st.text_input("Co_applicant Income")
    LoanAmount = st.text_input("Loan Amount")
    Loan_Amount_Term = st.text_input("Loan Amount Term")
    Credit_History = st.selectbox("Credit_History" , ['positive', 'negative'] )
    Property_Area = st.selectbox("Property_Area" , ['Rural', 'Urban', 'Semiurban'] )
    DTI = ((pd.to_numeric(LoanAmount) / (pd.to_numeric(Loan_Amount_Term) * 12)) / pd.to_numeric(ApplicantIncome)) * 100
    
    if st.button("predict"):
        result = prediction( Gender,  Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, 
                            LoanAmount, Loan_Amount_Term , Credit_History, Property_Area,DTI )
        label = ["No" , "Yes"]
        st.text(f"The Loan approval is {label[result]}")
    
    
if __name__ == '__main__':
    main() 