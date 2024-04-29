import streamlit as st
import pandas as pd
import plotly.express as px

df_Bowler = pd.read_csv("datasets\Bowler_stats.csv")

df_Bowler.Season = df_Bowler.Season.astype(str).apply(lambda x: x.replace(",", ""))

Bowler_name=st.sidebar.selectbox("Select_Bowler",df_Bowler.bowler.unique())

df_Bowler_player = df_Bowler[df_Bowler.bowler==Bowler_name]

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

# Create a Streamlit app
st.title("Cricket Bowling Statistics")

# Display the statistics in columns
col1, col2, col3 = st.columns(3)
if st.sidebar.button("Bowler_stats"):
    st.header(f"{Bowler_name} stats")
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

    st.divider()
    st.write(df_Bowler_player)

    st.write("### Season By Wickets")
    df_Bowler_player_Season = df_Bowler_player.groupby('Season')["wickets"].sum().reset_index()
    fig = px.bar(df_Bowler_player_Season, x='Season', y='wickets', title='Wickets per Season',color="Season")

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    df_Bowler_player_Team = df_Bowler_player.groupby('BattingTeam')["wickets"].sum().reset_index()
    fig = px.bar(df_Bowler_player_Team, x='BattingTeam', y='wickets', title='Wickets against a Team',
                color="BattingTeam")
    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)

    df_Bowler_player_Team = df_Bowler_player.groupby('City')["wickets"].sum().reset_index()
    fig = px.bar(df_Bowler_player_Team, x='City', y='wickets', title='Wickets in a City',
                color="City")
    fig.update_layout(xaxis_tickangle=270)



    # Display the plot in Streamlit
    st.plotly_chart(fig)

    df_Bowler_player_Team = df_Bowler_player.groupby('innings')["wickets"].sum().reset_index()
    fig = px.pie(df_Bowler_player_Team, names='innings', values='wickets', title='Wickets in a innings')

    fig.update_layout(xaxis_tickangle=270)

    # Display the plot in Streamlit
    st.plotly_chart(fig)

    df_Bowler_player_Team = df_Bowler_player.groupby('bowling_team')["wickets"].sum().reset_index()
    fig = px.bar(df_Bowler_player_Team, x='bowling_team', y='wickets', title='Wickets in a Team',
                color="bowling_team")
    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)

year = st.sidebar.selectbox("Select_year", df_Bowler['Season'].unique())
if st.sidebar.button("Bowler_stats_year"):

    selected_data = df_Bowler[df_Bowler['Season'] == str(year)]
    st.write(selected_data)
    selected_data_top = selected_data.groupby(["bowler","bowling_team"])['wickets'].sum().reset_index()
    a = selected_data_top.sort_values('wickets',ascending=False)

    top_wicket_takers = a.groupby('bowler').sum().nlargest(8, 'wickets').reset_index()

    # Plotting the graph using Plotly
    fig = px.bar(a.merge(top_wicket_takers['bowler']), 
                x='bowler', y='wickets', color='bowling_team',
                title=f'Top 8 Wicket Takers in  {year}',
                labels={'bowler': 'Bowler', 'wickets': 'Total Wickets'},
                hover_name='bowling_team', text='bowling_team')

    fig.update_layout(xaxis={'categoryorder':'total descending'},
                    yaxis=dict(title='Total Wickets'),
                    plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)

    ##top 5 wicket takers in a Bowling Team
    df_Bowler_Team = selected_data.groupby(['bowler','bowling_team'])['wickets'].sum().sort_values(ascending=False).reset_index()
    top_wicket_takers = df_Bowler_Team.loc[df_Bowler_Team.groupby('bowling_team')['wickets'].idxmax()]

    fig = px.bar(top_wicket_takers, 
                x='bowler', y='wickets', color='bowling_team',
                title=f'Top Wicket Takers in  {year} from Team',
                labels={'bowler': 'Bowler', 'wickets': 'Total Wickets'},
                hover_name='bowling_team', text='bowling_team')

    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)

    selected_data_innings =selected_data.groupby('innings')['wickets'].sum().reset_index()
    fig_pie = px.pie(selected_data_innings, names='innings', values='wickets', title='Wickets distribution in a innings')
    st.plotly_chart(fig_pie)

    df_Bowler_Team = selected_data.groupby(['bowler','BattingTeam'])['wickets'].sum().sort_values(ascending=False).reset_index()
    top_wicket_takers = df_Bowler_Team.loc[df_Bowler_Team.groupby('BattingTeam')['wickets'].idxmax()]

    fig = px.bar(top_wicket_takers, 
                x='bowler', y='wickets', color='BattingTeam',
                title=f'Top Wicket Takers in  {year} against a Team',
                labels={'bowler': 'Bowler', 'wickets': 'Total Wickets'},
                hover_name='BattingTeam', text='BattingTeam')

    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)

    df_Bowler_Team = selected_data.groupby(['bowler','City'])['wickets'].sum().sort_values(ascending=False).reset_index()
    top_wicket_takers = df_Bowler_Team.loc[df_Bowler_Team.groupby('City')['wickets'].idxmax()]

    fig = px.bar(top_wicket_takers, 
                x='bowler', y='wickets', color='City',
                title=f'Top Wicket Takers in  {year} in a City',
                labels={'bowler': 'Bowler', 'wickets': 'Total Wickets'},
                hover_name='City', text='City')

    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)



City = st.sidebar.selectbox("Select_year", df_Bowler['City'].unique())
if st.sidebar.button("Bowler_stats_City"):

    selected_data = df_Bowler[df_Bowler['City'] == City]
    st.write(selected_data)
    selected_data_top = selected_data.groupby(["bowler","bowling_team"])['wickets'].sum().reset_index()
    a = selected_data_top.sort_values('wickets',ascending=False)

    top_wicket_takers = a.groupby('bowler').sum().nlargest(8, 'wickets').reset_index()

    # Plotting the graph using Plotly
    fig = px.bar(a.merge(top_wicket_takers['bowler']), 
                x='bowler', y='wickets', color='bowling_team',
                title=f'Top 8 Wicket Takers in  {year}',
                labels={'bowler': 'Bowler', 'wickets': 'Total Wickets'},
                hover_name='bowling_team', text='bowling_team')

    fig.update_layout(xaxis={'categoryorder':'total descending'},
                    yaxis=dict(title='Total Wickets'),
                    plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)

    ##top 5 wicket takers in a Bowling Team
    df_Bowler_Team = selected_data.groupby(['bowler','bowling_team'])['wickets'].sum().sort_values(ascending=False).reset_index()
    top_wicket_takers = df_Bowler_Team.loc[df_Bowler_Team.groupby('bowling_team')['wickets'].idxmax()]

    fig = px.bar(top_wicket_takers, 
                x='bowler', y='wickets', color='bowling_team',
                title=f'Top Wicket Takers in  {year} from Team',
                labels={'bowler': 'Bowler', 'wickets': 'Total Wickets'},
                hover_name='bowling_team', text='bowling_team')

    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)

    selected_data_innings =selected_data.groupby('innings')['wickets'].sum().reset_index()
    fig_pie = px.pie(selected_data_innings, names='innings', values='wickets', title='Wickets distribution in a innings')
    st.plotly_chart(fig_pie)

    df_Bowler_Team = selected_data.groupby(['bowler','BattingTeam'])['wickets'].sum().sort_values(ascending=False).reset_index()
    top_wicket_takers = df_Bowler_Team.loc[df_Bowler_Team.groupby('BattingTeam')['wickets'].idxmax()]

    fig = px.bar(top_wicket_takers, 
                x='bowler', y='wickets', color='BattingTeam',
                title=f'Top Wicket Takers in  {year} against a Team',
                labels={'bowler': 'Bowler', 'wickets': 'Total Wickets'},
                hover_name='BattingTeam', text='BattingTeam')

    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)

    df_Bowler_Team = selected_data.groupby(['bowler','Season'])['wickets'].sum().sort_values(ascending=False).reset_index()
    top_wicket_takers = df_Bowler_Team.loc[df_Bowler_Team.groupby('Season')['wickets'].idxmax()]

    fig = px.bar(top_wicket_takers, 
                x='bowler', y='wickets', color='Season',
                title=f'Top Wicket Takers in  {City} in a Season',
                labels={'bowler': 'Bowler', 'wickets': 'Total Wickets'},
                hover_name='Season', text='Season')

    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)