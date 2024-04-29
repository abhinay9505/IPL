import numpy as np
import pandas as pd
import streamlit as st
import joblib

model = joblib.load("C:\\Users\\Abinay Rachakonda\\Desktop\\IPL\\pages\\requirements.txt")

st.header("ipl_ELITE_13")

df =pd.read_csv()
st.title("IPL 1st Innings Score Prediction")

col1,col2 = st.columns(2)

with col1:
    batting_team =st.selectbox('Select the batting team',df.bat_team.unique())
with col2:
    bowling_team_options = df['bowl_team'].unique()
# Removing the batting team from the options for bowling team selection
    bowling_team_options = [team for team in bowling_team_options if team != batting_team]
    bowling_team = st.selectbox('Select the bowling team', bowling_team_options)


selected_venue = st.selectbox('Venue',df.venue.unique())

overs_list = [f"{i}.{j}" for i in range(5, 20) for j in range(1, 7)]

Overs = st.selectbox('Overs',overs_list)

col3,col4,col5,col6= st.columns(4)
with col3 :
    score =st.number_input('Current Score',min_value=15)
with col4 :
    wickets =st.number_input('Current Wickets',min_value=0,max_value=9)
with col5 :
    prev_5_Score = st.number_input('Runs in previous 5 Overs',min_value=10,max_value=200)

with col6:

    prev_5_wickets = st.number_input('Wickets in prev 5',min_value=0,max_value=9)

if st.button('Predict Probability'):

    df2 = pd.DataFrame({"bat_team":[batting_team],
                  "bowl_team":[bowling_team],
                  "venue":[selected_venue],
                  "overs":[float(Overs)],
                  "runs":[score],
                  "wickets":[wickets],
                  "runs_last_5":[prev_5_Score],
                  "wickets_last_5":[prev_5_wickets]

                    })
    
    y_pred = model.predict(df2)

    st.header(f"Predicted Score : {int(np.round(y_pred[0]))-6}"+"\t\t to" + f"\t\t{int(np.round(y_pred[0]))+6}" )
    

    