import streamlit as st

st.set_page_config(page_title="Limmared Barbershop Booking", layout="centered")
st.title("💈 Limmared Barbershop")

st.image("logo.png", width=200)

st.markdown("### Book Your Appointment")

name = st.text_input("Full Name")
phone = st.text_input("Phone Number")
service = st.selectbox("Choose a Service", ["Haircut", "Beard", "Hair and Beard"])
date = st.date_input("Select a Date")
time = st.time_input("Select a Time")

if st.button("Book Now"):
    if name and phone:
        st.success(f"Thank you, {name}! Your appointment for **{service}** is booked on **{date}** at **{time}**.")
    else:
        st.error("Please enter your name and phone number.")