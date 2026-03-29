import streamlit as st
import plotly.express as px

def render_sidebar():
    st.sidebar.title("Settings")
    return st.sidebar.file_uploader("Upload CSV File", type=["csv"])

def display_results(plan_df, summary_df):
    st.write("### Project Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tasks", len(plan_df))
    col2.metric("Total Distance", f"{summary_df['Total KM'].sum()} km")
    col3.metric("Avg Load", f"{round(summary_df['Total KM'].mean(), 1)} km")

    tab1, tab2, tab3 = st.tabs(["Delivery Plan", "Workload Charts", "Agent Breakdown"])

    with tab1:
        st.info("The algorithm picks the agent with the lowest 'Load Before' distance for each task.")
        st.dataframe(plan_df, hide_index=True, use_container_width=True)
        st.download_button("Download Plan", plan_df.to_csv(index=False), "plan.csv")

    with tab2:
        st.write("#### Workload Comparison")
        c1, c2 = st.columns(2)
        fig1 = px.bar(summary_df, x='Agent', y='Total KM', color='Agent', title="Total Distance per Agent")
        c1.plotly_chart(fig1, use_container_width=True)
        
        fig2 = px.pie(summary_df, values='Total KM', names='Agent', title="Distance Distribution %")
        c2.plotly_chart(fig2, use_container_width=True)

    with tab3:
        st.write("#### Detailed Agent View")
        c1, c2 = st.columns(2)
        
        counts = plan_df.groupby('Assigned To').size().reset_index(name='Tasks')
        fig3 = px.bar(counts, x='Assigned To', y='Tasks', title="Tasks per Agent")
        c1.plotly_chart(fig3, use_container_width=True)

        mix = plan_df.groupby(['Assigned To', 'Priority']).size().reset_index(name='Count')
        fig4 = px.bar(mix, x='Assigned To', y='Count', color='Priority', title="Priority Mix", barmode='stack')
        c2.plotly_chart(fig4, use_container_width=True)

        st.divider()
        # Box plot showing individual trip lengths and spread
        fig5 = px.box(plan_df, x="Assigned To", y="KM", color="Assigned To", points="all",
                     title="Spread of Delivery Distances per Agent")
        st.plotly_chart(fig5, use_container_width=True)