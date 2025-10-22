import streamlit as st
import pandas as pd
from datetime import datetime
import smtplib

st.title("Hostel Food Management System")

# ---------- Initialize DataFrames ----------
if 'members' not in st.session_state:
    st.session_state.members = pd.DataFrame(columns=['Name', 'Email', 'Room No'])

if 'rent' not in st.session_state:
    st.session_state.rent = pd.DataFrame(columns=['Month', 'Member', 'Rent Paid'])

if 'electricity' not in st.session_state:
    st.session_state.electricity = pd.DataFrame(columns=['Month', 'Total Bill', 'Members'])

if 'ration' not in st.session_state:
    st.session_state.ration = pd.DataFrame(columns=['Month', 'Item', 'Quantity', 'Cost', 'Bought By'])

if 'meals' not in st.session_state:
    st.session_state.meals = pd.DataFrame(columns=['Date', 'Member', 'Meals Taken'])

if 'cooking' not in st.session_state:
    st.session_state.cooking = pd.DataFrame(columns=['Date', 'Member', 'Shift'])

# ---------- Member Management ----------
st.header("Member Details")
with st.expander("Add Member"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    room = st.text_input("Room Number")
    if st.button("Add Member"):
        st.session_state.members = pd.concat([st.session_state.members, pd.DataFrame([[name,email,room]], columns=['Name','Email','Room No'])])
        st.success(f"Member {name} added!")

st.table(st.session_state.members)

# ---------- Rent & Electricity ----------
st.header("Monthly Rent & Electricity")
with st.expander("Add Rent"):
    month = st.text_input("Month (e.g., October 2025)")
    member = st.selectbox("Member", st.session_state.members['Name'].tolist())
    rent_paid = st.number_input("Rent Paid", min_value=0)
    if st.button("Add Rent"):
        st.session_state.rent = pd.concat([st.session_state.rent, pd.DataFrame([[month, member, rent_paid]], columns=['Month','Member','Rent Paid'])])
        st.success(f"Rent for {member} added!")

with st.expander("Add Electricity Bill"):
    month_e = st.text_input("Month (Electricity)")
    total_bill = st.number_input("Total Bill", min_value=0)
    members_e = st.multiselect("Select Members", st.session_state.members['Name'].tolist())
    if st.button("Add Electricity Bill"):
        st.session_state.electricity = pd.concat([st.session_state.electricity, pd.DataFrame([[month_e, total_bill, members_e]], columns=['Month','Total Bill','Members'])])
        st.success(f"Electricity for {month_e} added!")

# ---------- Ration ----------
st.header("Ration Management")
with st.expander("Add Ration"):
    month_r = st.text_input("Month (Ration)")
    item = st.text_input("Item Name")
    qty = st.number_input("Quantity", min_value=0)
    cost = st.number_input("Cost", min_value=0)
    bought_by = st.selectbox("Bought By", st.session_state.members['Name'].tolist())
    if st.button("Add Ration"):
        st.session_state.ration = pd.concat([st.session_state.ration, pd.DataFrame([[month_r, item, qty, cost, bought_by]], columns=['Month','Item','Quantity','Cost','Bought By'])])
        st.success(f"Ration added!")

# ---------- Meal Tracking ----------
st.header("Meal Tracking")
with st.expander("Add Meal Data"):
    date = st.date_input("Date")
    member_meal = st.selectbox("Member", st.session_state.members['Name'].tolist())
    meals_taken = st.selectbox("Meals Taken", ["1", "2"])
    if st.button("Add Meal Record"):
        st.session_state.meals = pd.concat([st.session_state.meals, pd.DataFrame([[date, member_meal, meals_taken]], columns=['Date','Member','Meals Taken'])])
        st.success(f"Meal data added for {member_meal}")

# ---------- Cooking Duty ----------
st.header("Cooking Duty")
today = datetime.today().date()
with st.expander("Assign Cooking Duty"):
    member_cook = st.selectbox("Assign Member", st.session_state.members['Name'].tolist())
    shift = st.selectbox("Shift", ["Day", "Night"])
    if st.button("Assign Cooking"):
        st.session_state.cooking = pd.concat([st.session_state.cooking, pd.DataFrame([[today, member_cook, shift]], columns=['Date','Member','Shift'])])
        st.success(f"{member_cook} assigned for {shift} shift today!")
        # Optional: Send Email Notification
        # send_email(member_cook, shift)

# ---------- Display Tables ----------
st.subheader("Rent Records")
st.table(st.session_state.rent)
st.subheader("Electricity Records")
st.table(st.session_state.electricity)
st.subheader("Ration Records")
st.table(st.session_state.ration)
st.subheader("Meals Records")
st.table(st.session_state.meals)
st.subheader("Cooking Records")
st.table(st.session_state.cooking)
