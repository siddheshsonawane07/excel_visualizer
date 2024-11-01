import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def detect_column_types(df):
    column_types = {}
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            column_types[column] = 'numeric'
        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            column_types[column] = 'datetime'
        else:
            try:
                pd.to_datetime(df[column])
                column_types[column] = 'datetime'
            except:
                if df[column].nunique() / len(df) < 0.05:
                    column_types[column] = 'categorical'
                else:
                    column_types[column] = 'text'
    return column_types

def validate_columns(df, x_col, y_col=None, hue_col=None):
    valid = True
    message = ""
    if x_col not in df.columns:
        valid = False
        message += f"Column '{x_col}' not found in data. "
    if y_col and y_col not in df.columns:
        valid = False
        message += f"Column '{y_col}' not found in data. "
    if hue_col and hue_col not in df.columns:
        valid = False
        message += f"Column '{hue_col}' not found in data. "
    return valid, message

def create_visualization(viz_type, df, x_col, y_col=None, hue_col=None):
    valid, message = validate_columns(df, x_col, y_col, hue_col)
    if not valid:
        st.error(message)
        return None
    
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        if viz_type == 'bar':
            x_is_numeric = pd.api.types.is_numeric_dtype(df[x_col])
            y_is_numeric = y_col and pd.api.types.is_numeric_dtype(df[y_col])
            if y_is_numeric and not x_is_numeric:
                sns.barplot(data=df, y=x_col, x=y_col, hue=hue_col, ax=ax)
            else:
                sns.barplot(data=df, x=x_col, y=y_col, hue=hue_col, ax=ax)
            plt.xticks(rotation=45)
        
        elif viz_type == 'scatter':
            sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col, ax=ax)
        
        elif viz_type == 'line':
            sns.lineplot(data=df, x=x_col, y=y_col, hue=hue_col, ax=ax)
        
        elif viz_type == 'box':
            sns.boxplot(data=df, x=x_col, y=y_col, hue=hue_col, ax=ax)
        
        elif viz_type == 'violin':
            sns.violinplot(data=df, x=x_col, y=y_col, hue=hue_col, ax=ax)
        
        elif viz_type == 'hist':
            sns.histplot(data=df, x=x_col, hue=hue_col, kde=True, ax=ax)
        
        elif viz_type == 'count':
            sns.countplot(data=df, x=x_col, hue=hue_col, ax=ax)
            plt.xticks(rotation=45)
        
        plt.tight_layout()
        return fig
    
    except Exception as e:
        st.error(f"Error creating visualization: {str(e)}")
        return None

def suggest_visualizations(df, column_types):
    suggestions = []
    numeric_cols = [col for col, type_ in column_types.items() if type_ == 'numeric']
    categorical_cols = [col for col, type_ in column_types.items() if type_ == 'categorical']
    datetime_cols = [col for col, type_ in column_types.items() if type_ == 'datetime']
    
    if len(numeric_cols) >= 2:
        suggestions.append({'type': 'scatter', 'columns': (numeric_cols[0], numeric_cols[1]), 'description': f"Scatter plot of {numeric_cols[0]} vs {numeric_cols[1]}"})
    
    for cat_col in categorical_cols:
        for num_col in numeric_cols:
            suggestions.append({'type': 'bar', 'columns': (cat_col, num_col), 'description': f"Bar plot of {num_col} by {cat_col}"})
            suggestions.append({'type': 'box', 'columns': (cat_col, num_col), 'description': f"Box plot of {num_col} by {cat_col}"})
    
    for date_col in datetime_cols:
        for num_col in numeric_cols:
            suggestions.append({'type': 'line', 'columns': (date_col, num_col), 'description': f"Line plot of {num_col} over {date_col}"})
    
    for num_col in numeric_cols:
        suggestions.append({'type': 'hist', 'columns': (num_col,), 'description': f"Distribution of {num_col}"})
    
    return suggestions

def main():
    st.set_page_config(page_title="Dynamic Excel Visualizer", layout="wide")
    st.title("Dynamic Excel Visualizer")
    st.markdown("Upload a dataset and explore suggested and customizable visualizations.")
    
    st.sidebar.header("Upload Dataset")
    excel_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["xls", "xlsx"])
    
    if excel_file:
        df = pd.read_csv(excel_file) if excel_file.name.endswith('.csv') else pd.read_excel(excel_file)
        st.write("### Dataset Preview")
        st.dataframe(df.head())
        
        column_types = detect_column_types(df)
        suggestions = suggest_visualizations(df, column_types)
        
        st.write("### Create Custom Visualization")
        viz_type = st.selectbox("Select visualization type", ['bar', 'scatter', 'line', 'box', 'violin', 'hist', 'count'])
        
        x_col = st.selectbox("X-axis", df.columns)
        y_col = st.selectbox("Y-axis (optional)", ["None"] + list(df.columns))
        hue_col = st.selectbox("Grouping (optional)", ["None"] + list(df.columns))
        
        y_col = None if y_col == "None" else y_col
        hue_col = None if hue_col == "None" else hue_col
        
        if st.button("Generate Visualization"):
            fig = create_visualization(viz_type, df, x_col, y_col, hue_col)
            if fig:
                st.pyplot(fig)
        
        st.write("### Suggested Visualizations")
        for suggestion in suggestions:
            if st.checkbox(f"Show {suggestion['description']}"):
                fig = create_visualization(suggestion['type'], df, suggestion['columns'][0], suggestion['columns'][1] if len(suggestion['columns']) > 1 else None)
                if fig:
                    st.pyplot(fig)

if __name__ == '__main__':
    main()
