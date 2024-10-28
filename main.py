import streamlit as st
from langchain_community.document_loaders.csv_loader import CSVLoader
import os

def main():
    st.title("Excel Visualizer Agent")
    excel_file = st.file_uploader("Upload your CSV File", type=["csv", "xls", "xlsx"])

    if excel_file is not None:
        file_path = os.path.join(os.getcwd(), excel_file.name)
        
        with open(file_path, "wb") as f:
            f.write(excel_file.read())
        
        excel_loader = CSVLoader(file_path)
        data = excel_loader.load()
        
        st.write(data)

if __name__ == '__main__':
    main()
