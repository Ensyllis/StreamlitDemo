import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Simple Streamlit Demo",
    page_icon="📊",
    layout="wide"
)

# Add a title
st.title("Welcome to My Streamlit App! 👋")

# Add some text
st.write("""
This is a simple demonstration of what you can do with Streamlit.
Let's explore some basic features!
""")

# Create two columns
col1, col2 = st.columns(2)

# First column content
with col1:
    st.subheader("Interactive Widgets")
    
    # Add a slider
    number = st.slider("Pick a number", 0, 100, 50)
    st.write(f"You selected: {number}")
    
    # Add a text input
    user_input = st.text_input("Enter your name", "")
    if user_input:
        st.write(f"Hello, {user_input}!")
    
    # Add a selectbox
    option = st.selectbox(
        'What is your favorite color?',
        ['Red', 'Blue', 'Green', 'Yellow']
    )
    st.write(f'Your favorite color is {option}!')

# Second column content
with col2:
    st.subheader("Data Visualization")
    
    # Generate some random data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    # Create a line chart
    st.line_chart(chart_data)
    
    # Create a scatter plot using Plotly
    fig = px.scatter(
        chart_data, 
        x='A', 
        y='B',
        color='C',
        title='Interactive Scatter Plot'
    )
    st.plotly_chart(fig)

# Add a checkbox to show/hide data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(chart_data)

# Add a sidebar
with st.sidebar:
    st.header("Sidebar")
    st.write("You can add controls here!")
    
    # Add a radio button to sidebar
    view = st.radio(
        "Choose a view",
        ["Analysis", "Settings", "About"]
    )
    
    # Add some information based on selection
    if view == "About":
        st.info("This is a demo Streamlit application!")
    elif view == "Settings":
        st.warning("Settings are not implemented in this demo.")
    else:
        st.success("Viewing analysis page.")