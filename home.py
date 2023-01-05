import streamlit as st   
import smartsheet
import pandas as pd

smartsheet_client = smartsheet.Smartsheet("rjjjwNgTfxwAjE5R5YcSKu5OocAMyLAUJa2av")
sheet = smartsheet_client.Sheets.get_sheet(2954647561365380)
da = []
for i in sheet:
    da.append(i)
sheeet = pd.DataFrame(da)
st.write(sheeet)
