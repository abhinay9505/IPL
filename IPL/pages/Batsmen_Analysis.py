import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(
    page_title="Ipl Statistics",
    page_icon="👋",
)
st.header("IPL")
st.title("Analysis of Batsman stats ")

import numpy as np
import pandas as pd
df = pd.read_csv("datasets\Batsmen.csv")


df['Season'] = df['Season'].astype(str).apply(lambda x: x.replace(",", ""))
df['bowling_team'] = df['bowling_team'].astype(str).replace("Rising Pune Supergiant","Rising Pune Supergiants")
df['bowling_team'] = df['bowling_team'].astype(str).replace("Delhi Daredevils","Delhi Capitals")
df['City'] = df['City'].astype(str).replace("Navi Mumbai","Mumbai")

# Assuming df contains relevant data
a = st.sidebar.selectbox('Select Batsmen', list(df.batter.unique()))
b = st.sidebar.selectbox('Select Season', list(df.Season.unique()))

c=st.sidebar.selectbox("Bowling Team",list(df.bowling_team.unique()))
d=st.sidebar.selectbox("City",list(df.City.unique()))


if st.sidebar.button('Analyse Batsman and Season'):

    st.subheader(f'{a} in {b}')
    
    Batsman = df[(df.batter == a) & (df.Season == b)]

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
        player_stats = pd.DataFrame({'Matches':matches,'Runs':Runs,'Balls':Balls,
                                'Highest_Score':Max,'Strike_Rate':avg_strike_Season,
                                'Avg':avg_in_Season,'4s':Fours,'6s':Sixes,
                                '50':_50s,'100':_100s ,'Not_out': Not_out},index=['Overall'])
        
        st.title("Overall Performance in Season")
        st.write(player_stats)
        st.title("Performance in Match") 
        
        st.write(Batsman)
        import seaborn as sns
        import matplotlib.pyplot as plt
        fig=sns.barplot(data=Batsman, x=Batsman .index, y="batsman_run")
        plt.xlabel("Matche_ID")
        plt.xticks(rotation=90)
        plt.show()
        st.title("Runs Scored in each match")
        st.pyplot(fig.figure)
        import matplotlib.pyplot as plt
        # Group by 'bowling_team' and sum up 'batsman_run'
        runs_by_team = Batsman.groupby('bowling_team')['batsman_run'].sum().reset_index()

        # Plotting the bar graph
        plt.figure(figsize=(5, 5))
        fig = sns.barplot(x='bowling_team', y='batsman_run', data=runs_by_team, palette="viridis")
        plt.title('Total Runs Scored Against Each Team')
        plt.xlabel('Team')
        plt.ylabel('Total Runs')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.tight_layout()
        plt.show()
        st.pyplot(fig.figure)

        # Group by 'bowling_team' and sum up 'batsman_run'

        runs_by_City = Batsman.groupby('City')['batsman_run'].sum().reset_index()
        fig = sns.barplot(x='City', y='batsman_run', data=runs_by_City, palette="viridis")
        plt.title('Total Runs Scored Against Each City')
        plt.xlabel('City')
        plt.ylabel('Total Runs')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.tight_layout()
        plt.show()
        st.pyplot(fig.figure)

        # Assuming you already have the 'avg_against_a_team' DataFrame calculated as in your code snippet
        avg_against_a_team = Batsman.groupby(['innings'])['batsman_run'].sum().reset_index()

        # Calculate the total runs
        total_runs = avg_against_a_team['batsman_run'].sum()

        # Calculate the percentage of runs scored in each inning
        avg_against_a_team['percentage'] = (avg_against_a_team['batsman_run'] / total_runs) * 100

        # Plotting the pie chart
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(avg_against_a_team['percentage'], labels=avg_against_a_team['innings'], autopct='%1.1f%%', startangle=90)
        ax.set_title(f'Distribution of Runs by Innings - {b}')
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the pie chart
        st.pyplot(fig)

        sixes_against_a_team = Batsman.groupby(['bowling_team'])['No_of_sixes'].sum().reset_index()
        #avg_against_a_team.rename(columns = {'batsman_run':"AVG"})
        plt.figure(figsize=(4, 4))
        fig=sns.barplot(data=sixes_against_a_team, x='bowling_team', y='No_of_sixes')
        plt.title('Sixes Against Each Bowling Team')
        plt.xlabel('Bowling Team')
        plt.ylabel('No_of sixes')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.tight_layout()
        plt.show()
        st.pyplot(fig.figure)
            
        max_against_a_team = Batsman.groupby(['bowling_team'])['batsman_run'].max().reset_index()
        #avg_against_a_team.rename(columns = {'batsman_run':"AVG"})
        plt.figure(figsize=(6, 6))
        fig = sns.barplot(data=max_against_a_team, x='bowling_team', y='batsman_run')
        plt.title('Highest Score Against Each Bowling Team')
        plt.xlabel('Bowling Team')
        plt.ylabel('High Score')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.tight_layout()
        plt.show()
        st.pyplot(fig.figure)
        # Calculate average strike rate against each team
        avg_strike_rate = Batsman.groupby('bowling_team')['Strike_rate'].mean().reset_index()

        # Plotting the line plot
        plt.figure(figsize=(6, 6))
        fig=sns.lineplot(data=avg_strike_rate, x='bowling_team', y='Strike_rate', marker='o')
        plt.title('Average Strike Rate Against Each Bowling Team')
        plt.xlabel('Bowling Team')
        plt.ylabel('Average Strike Rate')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.tight_layout()
        plt.show()
        st.pyplot(fig.figure)

    else:
        st.title(f"{a} Not played in {b}")
        st.write(Batsman)




if st.sidebar.button('Overall stats by batsmen'):
    st.subheader(f'{a} IPL stats')
    Batsman = df[(df.batter == a)]
    
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
    player_stats = pd.DataFrame({'Matches':matches,'Runs':Runs,'Balls':Balls,
                             'Highest_Score':Max,'Strike_Rate':avg_strike_Season,
                             'Avg':avg_in_Season,'4s':Fours,'6s':Sixes,
                             '50':_50s,'100':_100s ,'Not_out': Not_out},index=['Overall'])
    
    st.title("Overall Performance in IPL")
    st.write(player_stats)
    st.title("Performance in Match") 
       
    st.write(Batsman)
    # Assuming you already have the 'avg_against_a_team' DataFrame calculated as in your code snippet
    
    import plotly.express as px

    # Assuming you already have the 'avg_against_a_team' DataFrame calculated as in your code snippet
    avg_against_a_team = Batsman.groupby(['Season'])['batsman_run'].sum().reset_index()

    # Define custom colors for the bars
    colors = px.colors.qualitative.Dark24

    # Plotting the bar chart using Plotly
    fig = px.bar(avg_against_a_team, x='Season', y='batsman_run', title='Season Wise runs', color='Season',
                color_discrete_sequence=colors)
    fig.update_layout(xaxis_title='Innings', yaxis_title='Total Runs', xaxis_tickangle=270)
    st.plotly_chart(fig)

        # Group by 'bowling_team' and sum up 'batsman_run'
    runs_by_team = Batsman.groupby('bowling_team')['batsman_run'].sum().reset_index()

    # Plotting the bar graph using Plotly Express with a predefined color scale
    fig = px.bar(runs_by_team, x='bowling_team', y='batsman_run', title='Total Runs Scored Against Each Team',
                labels={'bowling_team': 'Team', 'batsman_run': 'Total Runs'},
                color='bowling_team', color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(xaxis_tickangle=270)
    st.plotly_chart(fig)
# Plotting the pie chart using Plotly Express
    runs_by_innings = Batsman.groupby('innings')['batsman_run'].sum().reset_index()
    fig = px.pie(runs_by_innings, values='batsman_run', names='innings', title='Distribution of Runs Scored Against Each Team by Innings'
                 ,color_discrete_sequence=px.colors.qualitative.Dark24)
    st.plotly_chart(fig)
    runs_to_a_team = Batsman.groupby('BattingTeam')['batsman_run'].sum().reset_index()
    fig = px.pie(runs_to_a_team, values='batsman_run', names='BattingTeam', title='Distribution of Runs Scored in a Team'
                 ,color_discrete_sequence=px.colors.qualitative.G10)
    st.plotly_chart(fig)
    max_against_a_team = Batsman.groupby(['bowling_team'])['batsman_run'].max().reset_index()
    # Plotting the bar chart using Plotly Express
    # Plotting the bar chart using Plotly Express with a predefined color scale
    fig = px.bar(max_against_a_team, x='bowling_team', y='batsman_run', title='Highest Score Against Each Team',
             color='bowling_team', color_discrete_sequence=px.colors.qualitative.Dark24)
    fig.update_layout(xaxis_title='Bowling Team', yaxis_title='High Score', xaxis_tickangle=-90)
    st.plotly_chart(fig)


if st.sidebar.button('Top performers'):
    st.write(df)
    import matplotlib.pyplot as plt
    # Assuming you already have the 'avg_against_a_team' DataFrame calculated as in your code snippet
    avg_against_a_team = df.groupby(['batter'])['batsman_run'].sum().reset_index()
# Sorting the DataFrame based on 'batsman_run' column in descending order
    sorted_df = avg_against_a_team.sort_values(by='batsman_run', ascending=False)

    avg = sorted_df.head(10)
# Define custom colors for the bars
    colors = px.colors.qualitative.Set3

# Plotting the bar chart using Plotly
    fig = px.bar(avg, x='batter', y='batsman_run', title='Top Scorers', color='batter',
             color_discrete_sequence=colors)
    fig.update_layout(xaxis_title='Batsmen', yaxis_title='Total Runs', xaxis_tickangle=270)
    st.plotly_chart(fig)

    batsman_runsperseason = df.groupby(['Season', 'BattingTeam', 'batter'])['batsman_run'].sum().reset_index()
    # Calculate total runs scored by each batter
    batsman_runsperseason = batsman_runsperseason.groupby(['Season', 'batter'])['batsman_run'].sum().unstack().T
    batsman_runsperseason['Total'] = batsman_runsperseason.sum(axis=1)
    batsman_runsperseason = batsman_runsperseason.sort_values(by='Total', ascending=False)
    batsman_runsperseason = batsman_runsperseason.drop(columns=['Total'])

    fig = px.line(batsman_runsperseason[:8].T, labels={'index': 'Season', 'value': 'Number of Runs'}, title='Top 8 Batsmen Runs in IPL')
    fig.update_layout(yaxis_title='Number of Runs')
    st.plotly_chart(fig)

    batsman_sixes_perseason = df.groupby(['Season', 'BattingTeam', 'batter'])['No_of_sixes'].sum().reset_index()
    # Calculate total runs scored by each batter
    batsman_sixes_perseason = batsman_sixes_perseason.groupby(['Season', 'batter'])['No_of_sixes'].sum().unstack().T
    batsman_sixes_perseason['Total'] = batsman_sixes_perseason.sum(axis=1)
    batsman_sixes_perseason = batsman_sixes_perseason.sort_values(by='Total', ascending=False)
    batsman_sixes_perseason = batsman_sixes_perseason.drop(columns=['Total'])

    fig = px.line(batsman_sixes_perseason[:8].T, labels={'index': 'Season', 'value': 'Number of sixes'}, title='Top 8 six Hitters in IPL')
    fig.update_layout(yaxis_title='Number of Runs')
    st.plotly_chart(fig)

    batsman_runs_to_team = df.groupby(['BattingTeam', 'batter'])['batsman_run'].sum().reset_index()

    # Find the indices of the maximum runs for each team
    max_runs_indices = batsman_runs_to_team.groupby('BattingTeam')['batsman_run'].idxmax()

    # Filter the dataframe to get the rows with maximum runs for each team
    max_runs_per_team = batsman_runs_to_team.loc[max_runs_indices]
    
    import plotly.express as px
    

    # Create a bar plot using Plotly Express
    fig = px.bar(max_runs_per_team, 
             x='BattingTeam', 
             y='batsman_run', 
             text='batter',  # Add batsman name as text label
             title='Maximum Runs Scored by a Batter for Each Team',
             labels={'BattingTeam': 'Batting Team', 'batsman_run': 'Maximum Runs Scored'}
             ,color_discrete_sequence=px.colors.qualitative.Dark24)

    # Rotate x-axis labels
    fig.update_layout(xaxis_tickangle=270)

    # Update text position to inside the bars
    fig.update_traces(textposition='inside')

    # Show the plot
    st.plotly_chart(fig)


    batsman_runs = df.groupby(['batter'])[['batsman_run','Balls_Faced']].sum().reset_index()

    batsman_runs['SR'] = round(batsman_runs.batsman_run/batsman_runs.Balls_Faced,2)*100
    sorted_df = batsman_runs.sort_values(by='SR', ascending=False)
    ass =sorted_df[sorted_df.batsman_run>=1000][:50]
 #Plotting the bar chart using Plotly Express
    fig = px.bar(ass[:10], x='batter', y='SR', title='Top Strikers', color_discrete_sequence=px.colors.qualitative.Alphabet_r)
    fig.update_layout(xaxis_title='Batsman', yaxis_title='Strike Rate')
    fig.update_xaxes(tickangle=270)
    st.plotly_chart(fig)


if st.sidebar.button('Top performers against a team'):
    
    Batsman = df[(df.bowling_team==c)]
    st.write(Batsman)

    # Assuming you already have the 'avg_against_a_team' DataFrame calculated as in your code snippet
    avg_against_a_team = Batsman.groupby(['batter','bowling_team'])['batsman_run'].sum().reset_index()
    sorted_df = avg_against_a_team.sort_values(by='batsman_run', ascending=False)

    # Define custom colors for the bars
    colors = px.colors.qualitative.Set3

    # Plotting the bar chart using Plotly
    fig = px.bar(sorted_df[:10], x='batter', y='batsman_run', title=f'Top runs scorers against {c} ', color='batter',
             color_discrete_sequence=colors)
    fig.update_layout(xaxis_title='Batsmen', yaxis_title='Total Runs', xaxis_tickangle=270)
    st.plotly_chart(fig)

    batsman_runs = Batsman.groupby(['batter'])[['batsman_run','Balls_Faced']].sum().reset_index()

    batsman_runs['SR'] = round(batsman_runs.batsman_run/batsman_runs.Balls_Faced,2)*100
    sorted_df = batsman_runs.sort_values(by='SR', ascending=False)
    ass =sorted_df[sorted_df.batsman_run>500][:20]
 #Plotting the bar chart using Plotly Express
    fig = px.bar(ass[:10], x='batter', y='SR', title='Top Strikers', color_discrete_sequence=px.colors.qualitative.Alphabet_r)
    fig.update_layout(xaxis_title='Batsman', yaxis_title='Strike Rate')
    fig.update_xaxes(tickangle=270)
    st.plotly_chart(fig)

    batsman_sixes_perseason = Batsman.groupby(['Season', 'BattingTeam', 'batter'])['No_of_sixes'].sum().reset_index()
    # Calculate total runs scored by each batter
    batsman_sixes_perseason = batsman_sixes_perseason.groupby(['Season', 'batter'])['No_of_sixes'].sum().unstack().T
    batsman_sixes_perseason['Total'] = batsman_sixes_perseason.sum(axis=1)
    batsman_sixes_perseason = batsman_sixes_perseason.sort_values(by='Total', ascending=False)
    batsman_sixes_perseason = batsman_sixes_perseason.drop(columns=['Total'])

    fig = px.line(batsman_sixes_perseason[:8].T, labels={'index': 'Season', 'value': 'Number of sixes'}, title=f'Top 8 six Hitters against {c}')
    fig.update_layout(yaxis_title='Number of Runs')
    st.plotly_chart(fig)


     #Plotting the bar chart using Plotly Express
    batsman = Batsman.groupby(['batter'])[['batsman_run']].max().reset_index()
    batsmans= batsman.sort_values(by='batsman_run',ascending=False)
    fig = px.bar(batsmans[:10], x='batter', y='batsman_run', title=f'Highest scores against {c}', color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_layout(xaxis_title='Batsman', yaxis_title='Highest scores')
    fig.update_xaxes(tickangle=270)
    st.plotly_chart(fig)




if st.sidebar.button('Top performers in a City'):

    Batsman = df[(df.City == d)]
    st.title("City with every match stats")
    st.write(Batsman)
    # Assuming you already have the 'avg_against_a_team' DataFrame calculated as in your code snippet
    avg_against_a_team = Batsman.groupby(['batter','bowling_team'])['batsman_run'].sum().reset_index()
    sorted_df = avg_against_a_team.sort_values(by='batsman_run', ascending=False)

    # Define custom colors for the bars
    colors = px.colors.qualitative.Set3

    # Plotting the bar chart using Plotly
    fig = px.bar(sorted_df[:10], x='batter', y='batsman_run', title=f'Top runs scorers in {d} ', color='batter',
             color_discrete_sequence=colors)
    fig.update_layout(xaxis_title='Batsmen', yaxis_title='Total Runs', xaxis_tickangle=270)
    st.plotly_chart(fig)

    batsman_runs = Batsman.groupby(['batter'])[['batsman_run','Balls_Faced']].sum().reset_index()

    batsman_runs['SR'] = round(batsman_runs.batsman_run/batsman_runs.Balls_Faced,2)*100
    sorted_df = batsman_runs.sort_values(by='SR', ascending=False)
    ass =sorted_df[sorted_df.batsman_run>300][:20]
 #Plotting the bar chart using Plotly Express
    fig = px.bar(ass[:10], x='batter', y='SR', title='Top Strikers', color_discrete_sequence=px.colors.qualitative.Alphabet_r)
    fig.update_layout(xaxis_title='Batsman', yaxis_title='Strike Rate')
    fig.update_xaxes(tickangle=270)
    st.plotly_chart(fig)

    batsman_sixes_perseason = Batsman.groupby(['Season', 'BattingTeam', 'batter'])['No_of_sixes'].sum().reset_index()
    # Calculate total runs scored by each batter
    batsman_sixes_perseason = batsman_sixes_perseason.groupby(['Season', 'batter'])['No_of_sixes'].sum().unstack().T
    batsman_sixes_perseason['Total'] = batsman_sixes_perseason.sum(axis=1)
    batsman_sixes_perseason = batsman_sixes_perseason.sort_values(by='Total', ascending=False)
    batsman_sixes_perseason = batsman_sixes_perseason.drop(columns=['Total'])

    fig = px.line(batsman_sixes_perseason[:8].T, labels={'index': 'Season', 'value': 'Number of sixes'}, title=f'Top 8 six Hitters in {d}')
    fig.update_layout(yaxis_title='Number of Runs')
    st.plotly_chart(fig)


     #Plotting the bar chart using Plotly Express
    batsman = Batsman.groupby(['batter'])[['batsman_run']].max().reset_index()
    batsmans= batsman.sort_values(by='batsman_run',ascending=False)
    fig = px.bar(batsmans[:10], x='batter', y='batsman_run', title=f'Highest scores in {d}', color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_layout(xaxis_title='Batsman', yaxis_title='Highest scores')
    fig.update_xaxes(tickangle=270)
    st.plotly_chart(fig)

