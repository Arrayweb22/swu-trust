import sys
import os

# Add 'frontend' to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "frontend"))

import sys
import os

# Add 'frontend' to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "frontend"))

from login import show_login
from dashboard import show_dashboard
import streamlit as st
from api import process_request

st.set_page_config(page_title="SWU Trust", layout="wide")

# Sidebar Navigation
st.sidebar.title("SWU Trust Navigation")
page = st.sidebar.radio("Go to", ["Login", "Dashboard"])

# Display Pages
if page == "Login":
    show_login()
elif page == "Dashboard":
    show_dashboard()
