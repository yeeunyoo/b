import streamlit as st   
import smartsheet


smartsheet_client = smartsheet.Smartsheet("rjjjwNgTfxwAjE5R5YcSKu5OocAMyLAUJa2av")
sheet = smartsheet_client.Sheets.get_sheet(1785827530434436)
st.write(sheet)