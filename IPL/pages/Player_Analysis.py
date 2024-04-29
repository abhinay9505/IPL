import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(
    page_title="Ipl Statistics",
    page_icon="🏏🏏",
)

df = pd.read_csv('datasets\Batsmen.csv')
df_Bowler = pd.read_csv('datasets\Bowler_stats.csv')

df['Season'] = df['Season'].astype(str).apply(lambda x: x.replace(",", ""))
df['City'] = df['City'].astype(str).replace("Navi Mumbai","Mumbai")


maps ={'Rising Pune Supergiant':'Rising Pune Supergiants','Delhi Daredevils':'Delhi Capitals',
      'Delhi Dardevils':'Delhi Capitals','Kings XI Punjab':'Punjab Kings','Deccan Chargers':'Sunrisers Hyderabad'}
df =df.replace(maps)
df_Bowler =df_Bowler.replace(maps)
# Assuming df and df_bowler are your dataframes
unique_names_df = df['batter'].unique()
unique_names_df_bowler = df_Bowler['bowler'].unique()

# Combine unique names from both datasets
unique_names_combined = set(unique_names_df) | set(unique_names_df_bowler)

# Convert back to a list if needed
unique_players_combined = list(unique_names_combined)


player = st.sidebar.selectbox("Select a Player",unique_players_combined)



if st.sidebar.button("Player_stats"):

    Batsman=df[df.batter==player]
    df_Bowler_player=df_Bowler[df_Bowler.bowler==player]

    if not Batsman.empty:

        
        avg_strike_Season = round(Batsman.batsman_run.sum()/Batsman.Balls_Faced.sum()*100,2)
        avg_in_Season = round(Batsman.batsman_run.sum()/len(Batsman[Batsman.kind !=0]),2)
        matches = Batsman.ID.count()
        Runs = Batsman.batsman_run.sum()
        Balls = Batsman.Balls_Faced.sum()
        Max = Batsman.batsman_run.max()
        Fours = Batsman.No_of_fours.sum()
        Sixes = Batsman.No_of_sixes.sum()
        _50s = Batsman[(Batsman['batsman_run'] >= 50) & (Batsman['batsman_run'] < 100)].shape[0]
        _100s = Batsman[(Batsman['batsman_run'] >= 100)].shape[0]
        Not_out= Batsman[Batsman.kind=='0'].shape[0]
        player_statss = pd.DataFrame({'Matches':matches,'Runs':Runs,'Balls':Balls,
                                'Highest_Score':Max,'Strike_Rate':avg_strike_Season,
                                'Avg':avg_in_Season,'4s':Fours,'6s':Sixes,
                                '50':_50s,'100':_100s ,'Not_out': Not_out},index=['Overall'])
        
        st.title(f"{player} stats as a Batsman")
        st.write(player_statss)
        
    else:
        st.title(f"{player} as a Batting stats not found")
        st.write(Batsman)

    
    matchesss = df_Bowler_player.ID.nunique()
    overs_bowled = df_Bowler_player.overs.sum()
    wickets = df_Bowler_player.wickets.sum()
    Balls = df_Bowler_player.Balls_Bowled.sum()
    runs = df_Bowler_player.runs_conceeded.sum()
    wides = df_Bowler_player.wides.sum()
    noballs = df_Bowler_player.noballs.sum()
    Econ = round(runs/overs_bowled,2)
    Avg = round(runs/wickets,2)
    Strike = round(Balls/wickets,2)

    st.title(f"{player} Bowling Statistics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Matches : " , matchesss)
        st.write("Overs Bowled:", overs_bowled)
        st.write("Wickets:", wickets)
        st.write("Balls Bowled:", Balls)

    with col2:
        
        st.write("Runs Conceded:", runs)
        st.write("Wides:", wides)
        st.write("No Balls:", noballs)

    with col3:
        
        st.write("Economy:", Econ)
        st.write("Average:", Avg)
        st.write("Strike Rate:", Strike)



st.sidebar.divider()

# Assuming df and df_bowler are your dataframes
unique_names_df = df['BattingTeam'].unique()
unique_names_df_bowler = df_Bowler['bowling_team'].unique()

# Combine unique names from both datasets
unique_names_combined = set(unique_names_df) | set(unique_names_df_bowler)

# Convert back to a list if needed
unique_teams_combined = list(unique_names_combined)

player =st.sidebar.selectbox("Select a player to Against",unique_players_combined)
Team=st.sidebar.selectbox("Select a Team to Against",unique_teams_combined)
if st.sidebar.button("Against a Team"):

    st.header(f"{player} Stats against {Team}")
    Batsman =df[df.batter==player]
    Batsman=Batsman[Batsman.bowling_team==Team]
    df_player = df_Bowler[df_Bowler.BattingTeam==Team]
    df_Bowler_player = df_player[df_player.bowler==player]


    if not Batsman.empty:

        
        avg_strike_Season = round(Batsman.batsman_run.sum()/Batsman.Balls_Faced.sum()*100,2)
        avg_in_Season = round(Batsman.batsman_run.sum()/len(Batsman[Batsman.kind !=0]),2)
        matches = Batsman.ID.count()
        Runs = Batsman.batsman_run.sum()
        Balls = Batsman.Balls_Faced.sum()
        Max = Batsman.batsman_run.max()
        Fours = Batsman.No_of_fours.sum()
        Sixes = Batsman.No_of_sixes.sum()
        _50s = Batsman[(Batsman['batsman_run'] >= 50) & (Batsman['batsman_run'] < 100)].shape[0]
        _100s = Batsman[(Batsman['batsman_run'] >= 100)].shape[0]
        Not_out= Batsman[Batsman.kind=='0'].shape[0]
        player_statss = pd.DataFrame({'Matches':matches,'Runs':Runs,'Balls':Balls,
                                'Highest_Score':Max,'Strike_Rate':avg_strike_Season,
                                'Avg':avg_in_Season,'4s':Fours,'6s':Sixes,
                                '50':_50s,'100':_100s ,'Not_out': Not_out},index=['Overall'])
        
        st.title("Batting Stats")
        st.write(player_statss)
        
    else:
        st.title(f"{player} as a Batting stats not found")
        st.write(Batsman)


    matchesss = df_Bowler_player.ID.nunique()
    overs_bowled = df_Bowler_player.overs.sum()
    wickets = df_Bowler_player.wickets.sum()
    Balls = df_Bowler_player.Balls_Bowled.sum()
    runs = df_Bowler_player.runs_conceeded.sum()
    wides = df_Bowler_player.wides.sum()
    noballs = df_Bowler_player.noballs.sum()
    Econ = round(runs/overs_bowled,2)
    Avg = round(runs/wickets,2)
    Strike = round(Balls/wickets,2)
    st.title(f"Bowling Statistics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Matches : ",matchesss)
        st.write("Overs Bowled:", overs_bowled)
        st.write("Wickets:", wickets)
        st.write("Balls Bowled:", Balls)

    with col2:
        
        st.write("Runs Conceded:", runs)
        st.write("Wides:", wides)
        st.write("No Balls:", noballs)

    with col3:
        
        st.write("Economy:", Econ)
        st.write("Average:", Avg)
        st.write("Strike Rate:", Strike)  

    df_player_runs =Batsman.groupby("Season")['batsman_run'].sum().reset_index()
    fig = px.bar(df_player_runs, x='Season', y='batsman_run', title=f'Season by runs by {player}',
             labels={'Season': 'Season'},color='Season')

    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    df_player_earns =Batsman.groupby("City")['batsman_run'].sum().reset_index()
    fig = px.bar(df_player_earns, x='City', y='batsman_run', title=f'City Wise runs by {player}',
             labels={'City': 'City'},color='City')

    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    runs_by_innings = Batsman.groupby('innings')['batsman_run'].sum().reset_index()
    fig = px.pie(runs_by_innings, values='batsman_run', names='innings', title=f'Distribution of Runs Scored Against {Team} by Innings'
                 ,color_discrete_sequence=px.colors.qualitative.Dark24)
    st.plotly_chart(fig)


    runs_to_a_team = Batsman.groupby('BattingTeam')['batsman_run'].sum().reset_index()
    fig = px.pie(runs_to_a_team, values='batsman_run', names='BattingTeam', title=f'Distribution of Runs Scored in a Team while playing against {Team}'
                 ,color_discrete_sequence=px.colors.qualitative.G10)
    st.plotly_chart(fig)

    df_player_wickets =df_Bowler_player.groupby("Season")['wickets'].sum().reset_index()
    fig = px.bar(df_player_wickets, x='Season', y='wickets', title=f'Season by wickets by {player}',
                 labels={'Season': 'Season'},color='Season')

    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    df_player_wickets =df_Bowler_player.groupby("City")['wickets'].sum().reset_index()
    fig = px.bar(df_player_wickets, x='City', y='wickets', title=f'City wise wickets by {player}',
             labels={'wickets': 'wickets'},color='City')

    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    runs_by_innings = df_Bowler_player.groupby('innings')['wickets'].sum().reset_index()
    fig = px.pie(runs_by_innings, values='wickets', names='innings', title=f'Distribution of wickets Against {Team} by Innings'
                 ,color_discrete_sequence=px.colors.qualitative.Dark24_r)
    st.plotly_chart(fig)

    runs_to_a_team = df_Bowler_player.groupby('bowling_team')['wickets'].sum().reset_index()
    fig = px.pie(runs_to_a_team, values='wickets', names='bowling_team', title=f'Distribution of wickets in a Team while playing against {Team}'
                 ,color_discrete_sequence=px.colors.qualitative.G10)
    
    st.plotly_chart(fig)

st.sidebar.divider()
unique_City_df = df.City.unique()
unique_City_df_bowler = df_Bowler.City.unique()

# Combine unique names from both datasets
unique_City_combined = set(unique_City_df) | set(unique_City_df_bowler)

unique_City_combined = list(unique_City_combined)

City =st.sidebar.selectbox("Select a City",unique_City_combined)
player = st.sidebar.selectbox("Select a Player stats",unique_players_combined)



if st.sidebar.button("City Wise analysis"):

    st.header(f"{player} Stats in {City}")
    Batsman =df[df.batter==player]
    Batsman=Batsman[Batsman.City==City]
    df_player = df_Bowler[df_Bowler.City==City]
    df_Bowler_player = df_player[df_player.bowler==player]

    if not Batsman.empty:

        
        avg_strike_Season = round(Batsman.batsman_run.sum()/Batsman.Balls_Faced.sum()*100,2)
        avg_in_Season = round(Batsman.batsman_run.sum()/len(Batsman[Batsman.kind !=0]),2)
        matches = Batsman.ID.count()
        Runs = Batsman.batsman_run.sum()
        Balls = Batsman.Balls_Faced.sum()
        Max = Batsman.batsman_run.max()
        Fours = Batsman.No_of_fours.sum()
        Sixes = Batsman.No_of_sixes.sum()
        _50s = Batsman[(Batsman['batsman_run'] >= 50) & (Batsman['batsman_run'] < 100)].shape[0]
        _100s = Batsman[(Batsman['batsman_run'] >= 100)].shape[0]
        Not_out= Batsman[Batsman.kind=='0'].shape[0]
        player_statss = pd.DataFrame({'Matches':matches,'Runs':Runs,'Balls':Balls,
                                'Highest_Score':Max,'Strike_Rate':avg_strike_Season,
                                'Avg':avg_in_Season,'4s':Fours,'6s':Sixes,
                                '50':_50s,'100':_100s ,'Not_out': Not_out},index=['Overall'])
        
        st.title("Batting Stats")
        st.write(player_statss)
        
    else:
        st.title(f"{player} as a Batting stats not found")
        st.write(Batsman)
    matchesss = df_Bowler_player.ID.nunique()
    overs_bowled = df_Bowler_player.overs.sum()
    wickets = df_Bowler_player.wickets.sum()
    Balls = df_Bowler_player.Balls_Bowled.sum()
    runs = df_Bowler_player.runs_conceeded.sum()
    wides = df_Bowler_player.wides.sum()
    noballs = df_Bowler_player.noballs.sum()
    Econ = round(runs/overs_bowled,2)
    Avg = round(runs/wickets,2)
    Strike = round(Balls/wickets,2)
    st.title(f"Bowling Statistics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Matches :" ,matchesss)
        st.write("Overs Bowled:", overs_bowled)
        st.write("Wickets:", wickets)
        st.write("Balls Bowled:", Balls)

    with col2:
        
        st.write("Runs Conceded:", runs)
        st.write("Wides:", wides)
        st.write("No Balls:", noballs)

    with col3:
        
        st.write("Economy:", Econ)
        st.write("Average:", Avg)
        st.write("Strike Rate:", Strike) 



    df_player_runs =Batsman.groupby("Season")['batsman_run'].sum().reset_index()
    fig = px.bar(df_player_runs, x='Season', y='batsman_run', title=f'Season by runs by {player}',
             labels={'Season': 'Season'},color='Season')

    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    df_player_earns =Batsman.groupby("bowling_team")['batsman_run'].sum().reset_index()
    fig = px.bar(df_player_earns, x='bowling_team', y='batsman_run', title=f'{City} Wise runs by {player} against a Team',
             labels={'City': 'City'},color='bowling_team')

    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    runs_by_innings = Batsman.groupby('innings')['batsman_run'].sum().reset_index()
    fig = px.pie(runs_by_innings, values='batsman_run', names='innings', title=f'Distribution of Runs Scored in {City} by Innings'
                 ,color_discrete_sequence=px.colors.qualitative.Dark24)
    st.plotly_chart(fig)


    runs_to_a_team = Batsman.groupby('BattingTeam')['batsman_run'].sum().reset_index()
    fig = px.pie(runs_to_a_team, values='batsman_run', names='BattingTeam', title=f'Distribution of Runs Scored in a Team while playing in {City}'
                 ,color_discrete_sequence=px.colors.qualitative.G10)
    st.plotly_chart(fig)

    df_player_wickets =df_Bowler_player.groupby("Season")['wickets'].sum().reset_index()
    fig = px.bar(df_player_wickets, x='Season', y='wickets', title=f'Season by wickets by {player}',
                 labels={'Season': 'Season'},color='Season')

    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    df_player_wickets =df_Bowler_player.groupby("BattingTeam")['wickets'].sum().reset_index()
    fig = px.bar(df_player_wickets, x='BattingTeam', y='wickets', title=f'{City} wise wickets by {player} against each Team',
             labels={'wickets': 'wickets'},color='BattingTeam')

    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    runs_by_innings = df_Bowler_player.groupby('innings')['wickets'].sum().reset_index()
    fig = px.pie(runs_by_innings, values='wickets', names='innings', title=f'Distribution of wickets in {City} by Innings'
                 ,color_discrete_sequence=px.colors.qualitative.Dark24_r)
    st.plotly_chart(fig)

    runs_to_a_team = df_Bowler_player.groupby('bowling_team')['wickets'].sum().reset_index()
    fig = px.pie(runs_to_a_team, values='wickets', names='bowling_team', title=f'Distribution of wickets in a Team while playing in {City}'
                 ,color_discrete_sequence=px.colors.qualitative.G10)
    
    st.plotly_chart(fig)


st.sidebar.divider()

bat_ball = pd.read_csv('datasets\Bats_vs_BAll.csv')
# Assuming df and df_bowler are your dataframes
Batter = bat_ball['batter'].unique()
Bowlers = bat_ball['bowler'].unique()

Batsman =st.sidebar.selectbox("Batsman",Batter)
Bowler=st.sidebar.selectbox("Bowler",Bowlers)
if st.sidebar.button("Batsman V/S Bowler"):

    st.title(f"{Batsman} vs {Bowler} in IPL")

    st.header("IPL stats")

    Bats_vs_Ball = bat_ball[(bat_ball['batter'] == Batsman) & (bat_ball['bowler'] == Bowler)]

    Runs = Bats_vs_Ball.batsman_run.sum()
    Out = Bats_vs_Ball.dismissal.sum()
    Balls = len(Bats_vs_Ball)
    _4s = len(Bats_vs_Ball[Bats_vs_Ball.batsman_run==4])
    _6s = len(Bats_vs_Ball[Bats_vs_Ball.batsman_run==6])
    Dot = len(Bats_vs_Ball[Bats_vs_Ball.batsman_run==0])
    Strike = round(Runs/Balls*100,2)
    Avg = round(Bats_vs_Ball.batsman_run.sum()/Bats_vs_Ball.dismissal.sum(),2)
    Matches =Bats_vs_Ball.ID.nunique()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Matches:", Matches)
        st.write("Runs:", Runs)
        st.write("Balls Faced:", Balls)

    with col2:
        
        st.write("4s:", _4s)
        st.write("6s:", _6s)
        st.write("Dots:", Dot)

    with col3:
        st.write("Outs:", Out)
        st.write("Average:", Avg)
        st.write("Strike Rate:", Strike) 


    df_player_runs =Bats_vs_Ball.groupby("Season")['batsman_run'].sum().reset_index()
    fig = px.bar(df_player_runs, x='Season', y='batsman_run', 
             title=f'Season by runs {Batsman} vs {Bowler}',
             labels={'Season': 'Season'},
             color='Season',
             color_continuous_scale='rainbow')
    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    df_player_runs =Bats_vs_Ball.groupby("City")['batsman_run'].sum().reset_index()
    fig = px.bar(df_player_runs, x='City', y='batsman_run', 
             title=f'City by runs {Batsman} against {Bowler}',
             labels={'City': 'City'},
             color='City',
             )
    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    df_player_runs =Bats_vs_Ball.groupby("Venue")['batsman_run'].sum().reset_index()
    fig = px.bar(df_player_runs, x='Venue', y='batsman_run', 
             title=f'Venue by runs {Batsman} against {Bowler}',
             labels={'Venue': 'Venue'},
             color='Venue',
             )
    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)

    df_player_runs =Bats_vs_Ball.groupby("bowling_team")['batsman_run'].sum().reset_index()
    fig = px.bar(df_player_runs, x='bowling_team', y='batsman_run', 
             title=f'{Batsman} Runs against {Bowler} while playig against a Team',
             labels={'bowling_team': 'bowling_team'},
             color='bowling_team',
             )
    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)
    df_player_runs =Bats_vs_Ball.groupby("BattingTeam")['batsman_run'].sum().reset_index()
    fig = px.bar(df_player_runs, x='BattingTeam', y='batsman_run', 
             title=f'{Batsman} Runs against {Bowler} while playig in a Team',
             labels={'BattingTeam': 'BattingTeam'},
             color='BattingTeam',
             )
    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)
    Bats_vs_Baller = Bats_vs_Ball[Bats_vs_Ball.dismissal==1]
    df_player_runs =Bats_vs_Baller.groupby("City")['dismissal'].sum().reset_index()
    fig = px.bar(df_player_runs, x='City', y='dismissal', 
             title=f'{Batsman} Wickets against {Bowler} while playig in a City',
             labels={'City': 'City'},
             color='City',
             )
    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)
 
