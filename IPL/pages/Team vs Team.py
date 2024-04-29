import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(
    page_title="Ipl Statistics",
    page_icon="🏏🏏",
)

df = pd.read_csv("datasets\Ball_By_Ball.csv")
df_Scores= pd.read_csv('datasets\match_innings_score.csv')
df_Bats = pd.read_csv('datasets\Batsmen.csv')
df_Bowler = pd.read_csv('datasets\Bowler_stats.csv')


col1, col2 = st.columns(2)

with col1:


    Team_A= st.selectbox("Select a Team_A", df["Team1"].unique())


with col2:
    available_teams = df["Team2"].unique().tolist()
    available_teams.remove(Team_A)
    Team_B= st.selectbox("Select a Team_B", available_teams)

head_to_head_matches = df[(df['Team1'].str.contains(Team_A) | df['Team2'].str.contains(Team_A)) & 
                          (df['Team1'].str.contains(Team_B) | df['Team2'].str.contains(Team_B))]
df_Scores_Teams =df_Scores[(df_Scores['BattingTeam'].str.contains(Team_A) | df_Scores['bowling_team'].str.contains(Team_A)) & 
                          (df_Scores['bowling_team'].str.contains(Team_B) | df_Scores['BattingTeam'].str.contains(Team_B))]

df_Bats_Team =df_Bats[(df_Bats['BattingTeam'].str.contains(Team_A) | df_Bats['bowling_team'].str.contains(Team_A)) & 
                          (df_Bats['bowling_team'].str.contains(Team_B) | df_Bats['BattingTeam'].str.contains(Team_B))]


df_Bats_Team_A =df_Bats_Team[df_Bats_Team.BattingTeam==Team_A]
df_Bats_Team_B =df_Bats_Team[df_Bats_Team.BattingTeam==Team_B]

top_scorer_row_A = df_Bats_Team_A[df_Bats_Team_A["batsman_run"] == df_Bats_Team_A["batsman_run"].max()]
top_scorer_row_B = df_Bats_Team_B[df_Bats_Team_B["batsman_run"] == df_Bats_Team_B["batsman_run"].max()]


col1,col2,col3 = st.columns(3)

with col2:

    button =st.button("Analyse The Stats")

if button:

    col1, col2 = st.columns(2)

    with col1:
        col1.image(f"images\{Team_A}.png")

    with col2:
        col2.image(f"images\{Team_B}.png")


    col11,col22,col33 = st.columns(3)
    Matches_Played = head_to_head_matches.shape[0]
    Winning_Team_A = head_to_head_matches[head_to_head_matches.WinningTeam==Team_A].shape[0]
    Winning_Team_B = head_to_head_matches[head_to_head_matches.WinningTeam==Team_B].shape[0]
    No_results = head_to_head_matches[head_to_head_matches.method=='D/L'].shape[0]
    Winning_per_A = round(Winning_Team_A/Matches_Played*100,2)
    Winning_per_B = round(Winning_Team_B/Matches_Played*100,2)
    Toss_A =head_to_head_matches[head_to_head_matches.TossWinner==Team_A].shape[0]
    Toss_win_per_A = round(Toss_A/Matches_Played*100,2)
    Toss_B =head_to_head_matches[head_to_head_matches.TossWinner==Team_B].shape[0]
    Toss_win_per_B = round(Toss_B/Matches_Played*100,2)
    Highest_Score_A = df_Scores_Teams[df_Scores_Teams.BattingTeam==Team_A].total_run_y.max()
    Highest_Score_B = df_Scores_Teams[df_Scores_Teams.BattingTeam==Team_B].total_run_y.max()
    Least_Score_A = df_Scores_Teams[df_Scores_Teams.BattingTeam==Team_A].total_run_y.min()
    Least_Score_B = df_Scores_Teams[df_Scores_Teams.BattingTeam==Team_B].total_run_y.min()


    with col11:
        col11.write(Matches_Played)
        col11.write(Winning_Team_A)
        col11.write(Winning_Team_B)
        col11.write(No_results)
        col11.write(Winning_per_A)
        col11.write(Toss_win_per_A)
        col11.write(Highest_Score_A)
        col11.write(Least_Score_A)
        col11.write(top_scorer_row_A["batter"].iloc[0])
        col11.write(top_scorer_row_A["batsman_run"].iloc[0])
       
        
                    

    with col22:
        col22.write("No_of_Matches")
        col22.write("Won Matches")
        col22.write("Lost Matches")
        col22.write("No Results")
        col22.write("Match Win Percentage")
        col22.write("Toss win percentage")
        col22.write("Highest Score")
        col22.write("Least Score")
        col22.write("Highest_individual_Scorer")
        col22.write("Highest_individual_Score")
        


    with col33:
        col33.write(Matches_Played)
        col33.write(Winning_Team_B)
        col33.write(Winning_Team_A)
        col33.write(No_results)
        col33.write(Winning_per_B)
        col33.write(Toss_win_per_B)
        col33.write(Highest_Score_B)
        col33.write(Least_Score_B)
        col33.write(top_scorer_row_B["batter"].iloc[0])
        col33.write(top_scorer_row_B["batsman_run"].iloc[0])
        