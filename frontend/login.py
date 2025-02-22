import streamlit as st
import streamlit_authenticator as stauth
from backend import database as db

def show_login():
    st.title("Login to SWU Trust")

    authenticator = stauth.Authenticate(
        db.get_users(), "swu_trust", "abcdef", cookie_expiry_days=30
    )

    name, authentication_status, swu_id = authenticator.login("Login", "main")

    if authentication_status:
        st.success(f"Welcome, {swu_id}!")
        st.session_state["swu_id"] = swu_id
        st.session_state["is_admin"] = db.is_admin(swu_id)
        st.experimental_rerun()
    elif authentication_status is False:
        st.error("Invalid SWU ID or Password")
    elif authentication_status is None:
        st.warning("Please enter your credentials.")
