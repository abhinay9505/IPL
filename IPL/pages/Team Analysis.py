import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np



st.set_page_config(
    page_title="Ipl Statistics",
    page_icon="👋",
)
st.header("IPL_Elite13")
st.title("Analysis of Team stats ")

df = pd.read_csv('datasets\IPL_Matches_2008_2022_Modified.csv')
df_Scores= pd.read_csv("datasets\match_innings_score.csv")
#st.write(df)

team = st.selectbox("select a team" ,df.Team1.unique())

df_Scores_team = df_Scores[df_Scores.BattingTeam==team]
Highest_Score = df_Scores_team.total_run_y.max()


st.divider()
team_pic=f'C:\\Users\\Abinay Rachakonda\\Desktop\\IPL\\images\\{team}.png'

title_writing = team
title_format = f'<p style="text-align: center; font-family: ' \
               f'Arial; color: #1b5587; font-size: 40px; ' \
               f'font-weight: bold;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1])

col2.image(team_pic, use_column_width=200)

df_team = df[((df['Team1'] == team) | (df['Team2'] == team))]
st.divider()
st.subheader(f"Complete Stats of {team}")
st.write(f"<div style='text-align: center;'><span style='color:black;'>Matches</span>&nbsp;&nbsp;<span style='color:green;'>{df_team.ID.nunique()}</span></div>", unsafe_allow_html=True)
st.write(f"<div style='text-align: center;'><span style='color:black;'>Won</span>&nbsp;&nbsp;<span style='color:green;'>{len(df_team[df_team.WinningTeam==team])}</span></div>", unsafe_allow_html=True)   
st.write(f"<div style='text-align: center;'><span style='color:black;'>Lost</span>&nbsp;&nbsp;<span style='color:green;'>{len(df_team[df_team.WinningTeam!=team])}</span></div>", unsafe_allow_html=True) 
st.write(f"<div style='text-align: center;'><span style='color:black;'>Toss Winning%</span>&nbsp;&nbsp;<span style='color:green;'>{round(len(df_team[df_team.TossWinner==team])/len(df_team)*100,2)}</span></div>", unsafe_allow_html=True)
filtered_data = df_team[(df_team['MatchNumber'].str.len()> 2)]
st.write(f"<div style='text-align: center;'><span style='color:black;'>playoffs</span>&nbsp;&nbsp;<span style='color:green;'>{filtered_data.Season.nunique()}</span></div>", unsafe_allow_html=True)
st.write(f"<div style='text-align: center;'><span style='color:black;'>Champions</span>&nbsp;&nbsp;<span style='color:green;'>{len(filtered_data[(filtered_data.MatchNumber=='Final')&(filtered_data.WinningTeam==team)])}</span></div>", unsafe_allow_html=True)
st.write(f"<div style='text-align: center;'><span style='color:black;'>Runners</span>&nbsp;&nbsp;<span style='color:green;'>{len(filtered_data[(filtered_data.MatchNumber=='Final')&(filtered_data.WinningTeam!=team)])}</span></div>", unsafe_allow_html=True)
st.write(f"<div style='text-align: center;'><span style='color:black;'>No Results</span>&nbsp;&nbsp;<span style='color:green;'>{len(df_team[df_team.WinningTeam=='No Results'])}</span></div>", unsafe_allow_html=True)
st.write(f"<div style='text-align: center;'><span style='color:black;'>Winning%</span>&nbsp;&nbsp;<span style='color:green;'>{round(len(df_team[df_team.WinningTeam==team])/len(df_team)*100,2)}</span></div>", unsafe_allow_html=True) 
st.write(f"<div style='text-align: center;'><span style='color:black;'>Highest Score</span>&nbsp;&nbsp;<span style='color:green;'>{Highest_Score}</span></div>", unsafe_allow_html=True) 
 
st.divider()


matches_city = df_team.groupby('City')["ID"].count().reset_index()
colums=['City','No of Matches']
matches_city.columns=colums
st.write(df_team)
fig = px.bar(matches_city, x='City', y='No of Matches', title='Matches Played in each City', color="City")
fig.update_layout(xaxis_title='City', yaxis_title='Matches Played')
fig.update_xaxes(tickangle=270)
st.plotly_chart(fig)



matches_season = df_team.groupby('Season')["ID"].count().reset_index()
colums=['Season','No of Matches']
matches_season.columns=colums

fig = px.bar(matches_season, x='Season', y='No of Matches', title='Matches Played in each Season', color="Season")
fig.update_layout(xaxis_title='Season', yaxis_title='Matches Played')
fig.update_xaxes(tickangle=270)
st.plotly_chart(fig)



matches_venue = df_team.groupby('Venue')["ID"].count().reset_index()
colums=['Venue','No of Matches']
matches_venue.columns=colums

fig = px.bar(matches_venue, x='Venue', y='No of Matches', title='Matches Played in each Venue', color="Venue")
fig.update_layout(xaxis_title='Venue', yaxis_title='Matches Played')
fig.update_xaxes(tickangle=270)
st.plotly_chart(fig)

filtered_data["Winsss"] =filtered_data.apply(lambda x: 1 if x['WinningTeam'] == team else 0, axis=1)


# Assuming filtered_data.Winsss is a list of values you want to plot
a=filtered_data.Winsss.value_counts()
fig = px.pie(values=a, names=a.index, title='Pie Chart of Won/Loss in playoffs')

st.plotly_chart(fig)
filtered_data2 = filtered_data[filtered_data.Winsss==1]
a=filtered_data2.WonBy.value_counts()
fig = px.pie(values=a, names=a.index, title='Pie Chart of WonBy in playoffs')

st.plotly_chart(fig)