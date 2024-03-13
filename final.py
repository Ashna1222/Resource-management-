import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\Ashna Nadarajan\Downloads\final_HR.csv")

unique_states = data['State'].unique()
unique_districts = data['District'].unique()
unique_nic_names = data['NICName'].unique()

selected_state = st.sidebar.selectbox("Select State", unique_states, key="state_selector")
selected_district = st.sidebar.selectbox("Select District", unique_districts, key="district_selector")

filtered_nic_names = data[data['District'] == selected_district]['NICName'].unique()
filtered_nic_names = [nic.replace('[', '').replace(']', '').replace("'", "") for nic in filtered_nic_names]
filtered_nic_names = [nic.capitalize() for nic in filtered_nic_names]
selected_nic_name = st.sidebar.selectbox("Select NIC Name", filtered_nic_names, key="nic_name_selector")


# #------------------------------------------------------------------------------------------------



# Plotting data for Rural, Main, and Urban workers
rural_cols = ['MainWorkersRuralPersons', 'MainWorkersRuralMales', 'MainWorkersRuralFemales']
urban_cols = ['MainWorkersUrbanPersons', 'MainWorkersUrbanMales', 'MainWorkersUrbanFemales']

rural_data = data[rural_cols].sum().values
main_data = data[['MainWorkersTotalPersons', 'MainWorkersTotalMales', 'MainWorkersTotalFemales']].iloc[0].values
urban_data = data[urban_cols].sum().values

# Plotting Rural, Main, and Urban data
fig, ax = plt.subplots(figsize=(10, 6))
x_labels = ['Rural', 'Main', 'Urban']
ax.bar(x_labels, rural_data, color='#1f77b4', label='Rural')
ax.bar(x_labels, main_data, bottom=rural_data, color='#ff7f0e', label='Main')
ax.bar(x_labels, urban_data, bottom=rural_data + main_data, color='#2ca02c', label='Urban')
ax.set_title(f"{selected_state} - {selected_district} - Workers Distribution")
ax.legend()
st.pyplot(fig)