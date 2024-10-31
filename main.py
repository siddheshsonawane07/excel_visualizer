import streamlit as st
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.title("Excel Visualizer Agent")
    
    excel_file = st.file_uploader("Upload your CSV File", type=["csv", "xls", "xlsx"])
    if excel_file is not None:
        df = pd.read_csv(excel_file) if excel_file.name.endswith('.csv') else pd.read_excel(excel_file)
        st.write("Data Sample:")
        st.write(df.head())
        
        llm = ChatMistralAI()

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an assistant that analyzes an Excel file and suggests diagrams we can create using seaborn or matplotlib. "
                    "You analyze data types and suggest possible visualizations.",
                ),
                ("human", "Suggest visualizations for the data in the uploaded Excel file."),
            ]
        )        
        chain = prompt | llm

        result = chain.invoke(
            {
                "input": df.head().to_string(),  
            }
        )

        st.write("Suggested Visualizations:")
        st.write(result)

        fig, ax = plt.subplots()
        sns.pairplot(df)
        st.pyplot(fig)

if __name__ == '__main__':
    main()
