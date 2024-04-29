import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(
    page_title="Ipl Statistics",
    page_icon="👋",
)
st.header("IpL")
st.title("Analysis of Auction stats ")

import pandas as pd
df = pd.read_csv("datasets\\auction (1).csv")

df = df.drop("Unnamed: 0",axis=1)
df['Year'] = df['Year'].astype(str).apply(lambda x: x.replace(",", ""))
df.Country =df.Country.str.strip()
maps ={'Rising Pune Supergiant':'Rising Pune Supergiants','Delhi Daredevils':'Delhi Capitals',
      'Delhi Dardevils':'Delhi Capitals','Kings XI Punjab':'Punjab Kings'}
df['Team'] = df['Team'].map(maps).fillna(df['Team'])

df['Winning bid']=df['Winning bid'].str.replace(",","")
df['Winning bid']=df['Winning bid'].astype("float64")

df.drop_duplicates(keep='first', inplace=True)

selected_year = st.sidebar.selectbox('Select Season', sorted(df['Year'].unique()))

if st.sidebar.button('Auction stats by a Year'):
   
        # Filter the data based on the selected season
    df_year = df[df['Year'] == selected_year]

        # Display the filtered DataFrame

    df_year_bid = df_year.sort_values(by="Winning bid",ascending=False)

# Define a list of colors
    colors = ['skyblue', 'orange', 'green', 'red', 'purple']

# Create a bar plot using Plotly Express with custom colors
    fig = px.bar(df_year_bid[:20], 
             x='Player', 
             y='Winning bid', 
             text='Team',
             color='Player',  # Color by BattingTeam to assign different colors
             title='Top winning bidders',
             color_discrete_sequence=colors)

# Rotate x-axis labels
    fig.update_layout(xaxis_tickangle=270)

# Update text position to inside the bars
    fig.update_traces(textposition='inside')

# Show the plot
    st.plotly_chart(fig)


    a = df_year['Team'].value_counts().reset_index()
    a.columns = ['Team', 'Players_Buy']
    fig = px.bar(a, x='Team', y='Players_Buy', title='Players Bought by Team',
             labels={'Players_Buy': 'Number of Players Bought', 'Team': 'Team Names'},color='Team')
    fig.update_layout(xaxis_tickangle=270)
    st.plotly_chart(fig)
    a=df_year.Country.value_counts().reset_index()
    a.columns = ['Country', 'No_Players_Buy']
    fig = px.bar(a, x='Country', y='No_Players_Buy', title='Players Bought by Country',
             labels={'Players_Buy': 'Number of Players Bought', 'Country': 'Country'},color='Country')

    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)

    #Grouping the data by country and finding the maximum winning bid within each group
    top_bidders = df_year.groupby('Country').apply(lambda x: x.loc[x['Winning bid'].idxmax()]).reset_index(drop=True)

    # Displaying the top winning bidder from each country
    top_bidders[['Country', 'Player', 'Team', 'Winning bid','Year']]

    fig = px.bar(top_bidders, x='Country', y='Winning bid', color='Country',
             title='Top Winning Bidder from Each Country',text='Player',
             labels={'Winning bid': 'Winning Bid Amount (in USD)', 'Country': 'Country'},
             hover_data={'Player': True, 'Team': True, 'Year': True})

    fig.update_layout(xaxis_tickangle=270)
    st.plotly_chart(fig)

    cross_data=pd.crosstab(df_year.Country,df_year.Team)
    fig = px.bar(cross_data, x=cross_data.index, y=cross_data.columns,
             title='Number of Players per Country and Team',
             labels={'x': 'Country', 'y': 'Number of Players'})
    fig.update_layout(barmode='group',xaxis_tickangle=270)
    st.plotly_chart(fig)

    a=df_year['Base price'].value_counts().reset_index()
    a.columns=["Base price","No_people"]

    fig = px.pie(a, values='No_people', names='Base price', title='Distribution of Base Prices')
    st.plotly_chart(fig)
    # Plotting histogram
    fig = px.histogram(df_year, x='Winning bid', title='Histogram of Base Prices')
    st.plotly_chart(fig)


    cross_data=pd.crosstab(df_year.Country,df_year.Team)
    fig = px.bar(cross_data, x=cross_data.index, y=cross_data.columns,
             title='Number of Players per Country and Team',
             labels={'x': 'Country', 'y': 'Number of Players'})
    fig.update_layout(barmode='group',xaxis_tickangle=270)
    st.plotly_chart(fig)








Country = st.sidebar.selectbox('Select Country', sorted(df['Country'].unique()))
if st.sidebar.button('Auction stats by a Country'):
    df_year = df[df['Country'] == Country]

        # Display the filtered DataFrame

    df_year_bid = df_year.sort_values(by="Winning bid",ascending=False)

# Define a list of colors
    colors = ['skyblue', 'orange', 'green', 'red', 'purple']

# Create a bar plot using Plotly Express with custom colors
    fig = px.bar(df_year_bid[:20], 
             x='Player', 
             y='Winning bid', 
             text='Team',
             color='Player',  # Color by BattingTeam to assign different colors
             title='Top winning bidders',
             color_discrete_sequence=colors)

# Rotate x-axis labels
    fig.update_layout(xaxis_tickangle=270)

# Update text position to inside the bars
    fig.update_traces(textposition='inside')

# Show the plot
    st.plotly_chart(fig)
    a=df_year['Base price'].value_counts().reset_index()
    a.columns=["Base price","No_people"]

    fig = px.pie(a, values='No_people', names='Base price', title='Distribution of Base Prices')
    st.plotly_chart(fig)
    # Plotting histogram
    fig = px.histogram(df_year, x='Winning bid', title='Histogram of Base Prices')
    st.plotly_chart(fig)


    a = df_year['Team'].value_counts().reset_index()
    a.columns = ['Team', 'Players_Buy']
    fig = px.bar(a, x='Team', y='Players_Buy', title='Players Bought by Team',
             labels={'Players_Buy': 'Number of Players Bought', 'Team': 'Team Names'},color='Team')
    fig.update_layout(xaxis_tickangle=270)
    st.plotly_chart(fig)
    #Grouping the data by country and finding the maximum winning bid within each group
    top_bidders = df_year.groupby('Team').apply(lambda x: x.loc[x['Winning bid'].idxmax()]).reset_index(drop=True)

    # Displaying the top winning bidder from each country
    top_bidders[['Player', 'Team', 'Winning bid','Year']]

    fig = px.bar(top_bidders, x='Team', y='Winning bid',
             title=f'Top Winning Bidder from {Country} from a Team',text='Player',
             labels={'Winning bid': 'Winning Bid Amount (in USD)', 'Team': 'Team'},
             hover_data={'Player': True, 'Team': True, 'Year': True},color='Team')

    fig.update_layout(xaxis_tickangle=270)
    st.plotly_chart(fig)


Team =st.sidebar.selectbox("Select a Team",sorted(df['Team'].unique()))

if st.sidebar.button('Auction stats by a Team'):
    df_team = df[df['Team'] == Team]

        # Display the filtered DataFrame

    df_team_bid = df_team.sort_values(by="Winning bid",ascending=False)

# Define a list of colors
    colors = ['skyblue', 'orange', 'green', 'red', 'purple']

# Create a bar plot using Plotly Express with custom colors
    fig = px.bar(df_team_bid[:20], 
             x='Player', 
             y='Winning bid', 
             text='Country',
             color='Player',  # Color by BattingTeam to assign different colors
             title='Top winning bidders',
             color_discrete_sequence=colors)

# Rotate x-axis labels
    fig.update_layout(xaxis_tickangle=270)

# Update text position to inside the bars
    fig.update_traces(textposition='inside')

# Show the plot
    st.plotly_chart(fig)

    a = df_team['Country'].value_counts().reset_index()
    a.columns = ['Country', 'Players_Buy']
    fig = px.bar(a, x='Country', y='Players_Buy', title=f'Players Bought by {Team}',
             labels={'Players_Buy': 'Number of Players Bought', 'Country': 'Country names'},color='Country')
    fig.update_layout(xaxis_tickangle=270)
    st.plotly_chart(fig)


    a = df_team['Year'].value_counts().reset_index()
    a.columns = ['Year', 'Players_Buy']
    fig = px.bar(a, x='Year', y='Players_Buy', title=f'Players Bought Year by {Team}',
             labels={'Players_Buy': 'Number of Players Bought', 'Year': 'Year'},color='Year')
    fig.update_layout(xaxis_tickangle=270)
    st.plotly_chart(fig)


    a=df_team['Base price'].value_counts().reset_index()
    a.columns=["Base price","No_people"]

    fig = px.pie(a, values='No_people', names='Base price', title='Distribution of Base Prices')
    st.plotly_chart(fig)

    fig = px.histogram(df_team, x='Winning bid', title='Histogram of Winning Bids')
    st.plotly_chart(fig)

    #Grouping the data by country and finding the maximum winning bid within each group
    top_bidders = df_team.groupby('Country').apply(lambda x: x.loc[x['Winning bid'].idxmax()]).reset_index(drop=True)

    # Displaying the top winning bidder from each country
    top_bidders[['Country', 'Player', 'Team', 'Winning bid','Year']]

    fig = px.bar(top_bidders, x='Country', y='Winning bid', color='Country',
                title='Top Winning Bidder from Each Country',text='Player',
                labels={'Winning bid': 'Winning Bid Amount (in USD)', 'Country': 'Country'},
                hover_data={'Player': True, 'Team': True, 'Year': True})

    fig.update_traces(textposition='inside')

    fig.update_layout(xaxis_tickangle=270)
    st.plotly_chart(fig)

    cross_data=pd.crosstab(df_team.Country,df_team.Year)
    fig = px.bar(cross_data, x=cross_data.index, y=cross_data.columns,
                title='Number of Players per Country and Year',
                labels={'x': 'Country', 'y': 'Number of Players'})
    fig.update_layout(barmode='group',xaxis_tickangle=270)

    st.plotly_chart(fig)

    df_team_invest = df_team.groupby(['Country'])['Winning bid'].sum().reset_index()
    fig = px.bar(df_team_invest, x=df_team_invest.Country, y=df_team_invest['Winning bid'],
                title='Invest on a Country',
                labels={'x': 'Country', 'y': 'Invest on a Country'},color='Country')
    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)




#Player Analysis
player =st.sidebar.selectbox("Select a player",sorted(df.Player.unique()))
if st.sidebar.button('Auction stats by a Player'):
    df_player = df[df['Player']==player]
    st.write(df_player)

    a=df_player.Team.value_counts().reset_index()
    a.columns = ['Team', 'No_of_Buy']
    fig = px.bar(a, x='Team', y='No_of_Buy', title='Team with most times Buy',
             labels={'Team': 'Team', 'No_of_Buy': 'No_of_times Buy'},color='Team')

    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)


    df_player_earns =df_player.groupby("Team")['Winning bid'].sum().reset_index()
    fig = px.bar(df_player_earns, x='Team', y='Winning bid', title=f'Earnings by {player} from a Team',
             labels={'Team': 'Teams Played', 'Winning bid': 'Winning bid'},color='Team')

    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)


    df_player_earns =df_player.groupby("Year")['Base price'].sum().reset_index()
    fig = px.bar(df_player_earns, x='Year', y='Base price', title=f'Bidded by {player} in a Year',
             labels={'Year': 'Bidded year', 'Base price': 'Base price'},color='Year')

    fig.update_layout(xaxis_tickangle=270)
    st.write(fig)











st.sidebar.write("### Overall Auction stats")
st.sidebar.write(" $ 💰 $"*5)



if st.sidebar.button('Overall Stats'):
    st.write(df)


    df_top_bid = df.sort_values(by="Winning bid",ascending=False)

# Define a list of colors
    colors = ['skyblue', 'orange', 'green', 'red', 'purple']

# Create a bar plot using Plotly Express with custom colors
    fig = px.bar(df_top_bid[:20], 
             x='Player', 
             y='Winning bid', 
             text='Team',
             color='Player',  # Color by BattingTeam to assign different colors
             title='Top winning bidders',
             color_discrete_sequence=colors)

# Rotate x-axis labels
    fig.update_layout(xaxis_tickangle=270)

# Update text position to inside the bars
    fig.update_traces(textposition='inside')

# Show the plot
    st.plotly_chart(fig)


    a = df['Team'].value_counts().reset_index()
    a.columns = ['Team', 'Players_Buy']
    fig = px.bar(a, x='Team', y='Players_Buy', title='Players Bought by Team',
             labels={'Players_Buy': 'Number of Players Bought', 'Team': 'Team Names'},color='Team')
    fig.update_layout(xaxis_tickangle=270)
    st.plotly_chart(fig)


    a=df.Country.value_counts().reset_index()
    a.columns = ['Country', 'No_Players_Buy']
    fig = px.bar(a, x='Country', y='No_Players_Buy', title='Players Bought by Country',
             labels={'Players_Buy': 'Number of Players Bought', 'Country': 'Country'},color='Country')

    fig.update_layout(xaxis_tickangle=270)

    st.plotly_chart(fig)


    cross_data=pd.crosstab(df.Country,df.Team)
    fig = px.bar(cross_data, x=cross_data.index, y=cross_data.columns,
             title='Number of Players per Country and Team',
             labels={'x': 'Country', 'y': 'Number of Players'})
    fig.update_layout(barmode='group',xaxis_tickangle=270)
    st.plotly_chart(fig)



    a=df['Base price'].value_counts().reset_index()
    a.columns=["Base price","No_people"]

    fig = px.pie(a, values='No_people', names='Base price', title='Distribution of Base Prices')
    st.plotly_chart(fig)
    # Plotting histogram
    fig = px.histogram(df, x='Winning bid', title='Histogram of Winning Prices')
    st.plotly_chart(fig)



















