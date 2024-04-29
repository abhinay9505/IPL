import numpy as np
import pandas as pd
import streamlit as st
predicted = pd.read_csv('datasets\Predicted_DataFrame.csv')
import joblib
#predicted Data Frame Representation
st.header("ipl_ELITE_13")
model = joblib.load("C:\\Users\\Abinay Rachakonda\\Desktop\\IPL\\pages\\requirements.txt")
st.title('IPL Win Predictor')
col1,col2 = st.columns(2)

with col1:
    batting_team =st.selectbox('Select the batting team',predicted.BattingTeam.unique())
with col2:
    bowling_team = st.selectbox('Select the bowling team',predicted.bowling_team.unique())

selected_city = st.selectbox('Cities',predicted.City.unique())

target = st.number_input('Target',min_value=0,max_value=300)

col3,col4,col5 = st.columns(3)
with col3 :
    score =st.number_input('Score',min_value=0)
with col4 :
    wickets =st.number_input('Wickets',min_value=0,max_value=9)
with col5 :
    overs = st.number_input('Overs completed',min_value=0,max_value=20)

if st.button('Predict Probability'):
    runs_left = target-score
    balls_left = 120 - overs*6
    wickets = 10-wickets
    crr = score/overs
    rrr = runs_left*6/balls_left
    df =pd.DataFrame({'BattingTeam':[batting_team],'bowling_team':[bowling_team],'City':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'Target':[target],'crr':[crr],'rrr':[rrr]})
        
    result = model.predict_proba(df)
    r_1 = round(result[0][0]*100)
    r_2 = round(result[0][1]*100)
    st.header('Wining Probabilty ')
    st.header(f"{batting_team}  : {r_2} %")
    st.header(f"{bowling_team}  : {r_1} %")