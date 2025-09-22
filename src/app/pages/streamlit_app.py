import streamlit as st
import pandas as pd
import os
from pathlib import Path
st.set_page_config(
    layout="wide",  # Can be "centered" or "wide"
    page_title="Expense Analyst",  # Title that appears in the browser tab
    page_icon="💳"  # Emoji or path to an image file for the favicon
)
st.title("Expense Analysis 💳")
st.divider()
DATA_PATH = Path(__file__).parents[3]/"data"/"raw"
def upload_files():
    
upload_files()
    

