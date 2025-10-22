import streamlit as st
import pandas as pd
from datetime import datetime

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
    name_member = st.text_input("Enter Member Name")
    email_member = st.text_input("Enter Member Email")
    room_member = st.text_input("Enter Room Number")
    if st.button("Add Member to List"):
        if name_member:
            st.session_state.members = pd.concat(
                [st.session_state.members, pd.DataFrame([[name_member, email_member, room_member]], columns=['Name','Email','Room No'])],
                ignore_index=True
            )
            st.success(f"Member {name_member} added!")
        else:
            st.warning("Please enter a member name.")

st.subheader("All Members")
st.table(st.session_state.members)

# ---------- Rent & Electricity ----------
st.header("Monthly Rent & Electricity")

with st.expander("Add Rent"):
    month_rent = st.text_input("Enter Month for Rent (e.g., October 2025)")
    member_rent = st.selectbox("Select Member for Rent", st.session_state.members['Name'].tolist(), key="rent_member_select")
    rent_paid = st.number_input("Enter Rent Paid", min_value=0)
    if st.button("Add Rent Record"):
        if member_rent:
            st.session_state.rent = pd.concat(
                [st.session_state.rent, pd.DataFrame([[month_rent, member_rent, rent_paid]], columns=['Month','Member','Rent Paid'])],
                ignore_index=True
            )
            st.success(f"Rent for {member_rent} added!")

with st.expander("Add Electricity Bill"):
    month_elec = st.text_input("Enter Month for Electricity", key="month_elec_input")
    total_bill = st.number_input("Enter Total Electricity Bill", min_value=0)
    members_elec = st.multiselect("Select Members for Electricity Bill", st.session_state.members['Name'].tolist(), key="elec_members_select")
    if st.button("Add Electricity Record"):
        if members_elec:
            st.session_state.electricity = pd.concat(
                [st.session_state.electricity, pd.DataFrame([[month_elec, total_bill, members_elec]], columns=['Month','Total Bill','Members'])],
                ignore_index=True
            )
            st.success(f"Electricity bill for {month_elec} added!")

# ---------- Ration ----------
st.header("Ration Management")
with st.expander("Add Ration Item"):
    month_ration = st.text_input("Enter Month for Ration", key="month_ration_input")
    item_name = st.text_input("Enter Item Name")
    qty_item = st.number_input("Enter Quantity", min_value=0)
    cost_item = st.number_input("Enter Cost", min_value=0)
    bought_by_member = st.selectbox("Select Member Who Bought Ration", st.session_state.members['Name'].tolist(), key="ration_member_select")
    if st.button("Add Ration Item"):
        if item_name:
            st.session_state.ration = pd.concat(
                [st.session_state.ration, pd.DataFrame([[month_ration, item_name, qty_item, cost_item, bought_by_member]], columns=['Month','Item','Quantity','Cost','Bought By'])],
                ignore_index=True
            )
            st.success(f"Ration item {item_name} added!")

# ---------- Meal Tracking ----------
st.header("Meal Tracking")
with st.expander("Add Meal Data"):
    date_meal = st.date_input("Select Date for Meal Record", key="meal_date_input")
    member_meal = st.selectbox("Select Member for Meal", st.session_state.members['Name'].tolist(), key="meal_member_select")
    meals_taken = st.selectbox("Number of Meals Taken", ["1", "2"], key="meal_count_select")
    if st.button("Add Meal Record"):
        st.session_state.meals = pd.concat(
            [st.session_state.meals, pd.DataFrame([[date_meal, member_meal, meals_taken]], columns=['Date','Member','Meals Taken'])],
            ignore_index=True
        )
        st.success(f"Meal data added for {member_meal} on {date_meal}")

# ---------- Cooking Duty ----------
st.header("Cooking Duty")
today_date = datetime.today().date()
with st.expander("Assign Cooking Duty"):
    member_cook = st.selectbox("Select Member for Cooking Duty", st.session_state.members['Name'].tolist(), key="cook_member_select")
    shift_cook = st.selectbox("Select Shift", ["Day", "Night"], key="cook_shift_select")
    if st.button("Assign Cooking Duty"):
        st.session_state.cooking = pd.concat(
            [st.session_state.cooking, pd.DataFrame([[today_date, member_cook, shift_cook]], columns=['Date','Member','Shift'])],
            ignore_index=True
        )
        st.success(f"{member_cook} assigned for {shift_cook} shift today!")

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
