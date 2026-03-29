import streamlit as st
import pandas as pd
from source.logic import assign_deliveries
from source.ui import render_sidebar, display_results

st.set_page_config(page_title="Delivery Optimizer", layout="wide")

def main():
    st.title("🚚 Delivery Optimizer Project")
    st.write("A tool to balance workload across 3 agents based on priority and travel distance.")

    user_file = render_sidebar()

    if user_file:
        try:
            data = pd.read_csv(user_file)
            required = ['Location_ID', 'Distance', 'Priority']

            if all(col in data.columns for col in required):
                plan, summary = assign_deliveries(data)
                display_results(plan, summary)
            else:
                st.error("CSV must have: Location_ID, Distance, and Priority columns.")
        
        except Exception as e:
            st.error(f"Error processing file: {e}")
            
    else:
        st.info("Please upload a CSV file to generate the optimization plan.")
        st.write("Example Format:")
        st.table(pd.DataFrame({
            'Location_ID': ['L1', 'L2'], 'Distance': [10, 20], 'Priority': ['High', 'Low']
        }))

if __name__ == "__main__":
    main()