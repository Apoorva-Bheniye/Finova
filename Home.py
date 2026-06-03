import streamlit as st
import sqlite3
import time
from utils.expenseTracker import ExpenseManager
from utils.expenseTracker import IncomeManager
from utils.expenseTracker import Account
from auth import AuthManager

st.title("Finova")
st.write("An AI poweredfinance tracker.")

auth = AuthManager()

# Session state for tracking login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.users_email = ""

tab1, tab2 = st.tabs(["🔑 Login","📝 Register"])

with tab1:
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if auth.login_user(email, password):
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success("Login Successful! Redirecting...")
            time.sleep(1.5)
            st.rerun()
        else:
            st.error("Invalid email or password.")

with tab2:
    st.subheader("Register")
    new_email = st.text_input("New Email")
    new_password = st.text_input("New Password", type="password")
    register_btn = st.button("Register")

    if register_btn:
        if auth.register_user(new_email, new_password):
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success("Registration successgul! Please log in.")
            
        else:
            st.error("Email already exists.")

#checking if the user is logged in
if st.session_state.logged_in:

    st.success("Head to side bar to use features")

#Dynimacally set the database name
db_name = "expenses.db"

#Initilize the managers with the database name
ExManager = ExpenseManager(db_name=db_name)
InManager = IncomeManager(db_name=db_name)
account = Account(db_name=db_name)

#Establish sqlite3 database connection for testing
conn = sqlite3.connect("expenses.db")
c = conn.cursor()

if st.session_state.logged_in:

#Toasted notification
    st.toast("Welcome to Finova!💰")

#close the connection
conn.close()



