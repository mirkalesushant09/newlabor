import streamlit as st
import pandas as pd

# Sample Worker Data
workers = [
    {
        "Name": "Ramesh",
        "Phone": "9876543210",
        "Skill": "Electrician",
        "Location": "Nashik"
    },
    {
        "Name": "Suresh",
        "Phone": "9876543211",
        "Skill": "Plumber",
        "Location": "Pune"
    },
    {
        "Name": "Mahesh",
        "Phone": "9876543212",
        "Skill": "Carpenter",
        "Location": "Mumbai"
    },
    {
        "Name": "Ganesh",
        "Phone": "9876543213",
        "Skill": "Mason",
        "Location": "Nagpur"
    }
]

st.title("👷 Labour Management System")

# Skill Filter
skill_filter = st.selectbox(
    "Filter by Skill",
    ["All"] + list(set(worker["Skill"] for worker in workers))
)

# Apply Filter
if skill_filter == "All":
    filtered_workers = workers
else:
    filtered_workers = [
        worker for worker in workers
        if worker["Skill"] == skill_filter
    ]

# Display Data
st.subheader("Workers List")
st.dataframe(pd.DataFrame(filtered_workers))

# Register New Worker
st.subheader("➕ Register Worker")

name = st.text_input("Name")
phone = st.text_input("Phone")
skill = st.text_input("Skill")
location = st.text_input("Location")

if st.button("Add Worker"):
    workers.append({
        "Name": name,
        "Phone": phone,
        "Skill": skill,
        "Location": location
    })

    st.success("Worker Added Successfully ✅")
    st.dataframe(pd.DataFrame(workers))