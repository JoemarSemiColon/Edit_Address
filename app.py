import streamlit as st
import pandas as pd

st.title("IDIT ADDRESS")

with st.form("upload_form"):

    uploaded_file = st.file_uploader(
        "Upload Excel file",
        type=["xlsx", "xls"]
    )

    submit = st.form_submit_button("Submit")

if submit:

    if uploaded_file is not None:

        df = pd.read_excel(uploaded_file)

        st.success("File submitted successfully!")

        st.write("File name:", uploaded_file.name)


        fullAdress = uploaded_file["AREA"]
        st.dataframe(fullAdress)

        

    else:
        st.warning("Please upload a file first.")