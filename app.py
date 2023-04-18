import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('C:/Users/jason_ef59wex/anaconda3/envs/myenv/projects/baseball_hitting.csv')


df = df.rename(columns ={'Player name' : 'player_name', 'At-bat' : 'at_bats', 'Games' : 'games', 'Runs' : 'runs', 'Hits' : 'hits', 'Double (2B)' : 'doubles', 'third baseman' : 'triples', 'home run': 'home_runs',
'run batted in' : 'RBI', 'a walk' : 'walks', 'Strikeouts' : 'strikeouts', 'stolen base' : 'stolen_bases', 'Caught stealing' : 'caught_stealing', 'On-base Percentage' : 'on_base_%', 'Slugging Percentage' : 'slugging_%',
'On-base Plus Slugging' : 'OPS'})

df = df.dropna()


df['strikeouts'] = df['strikeouts'].astype('int')


st.header('MLB Hitting Stats')
st.divider()
st.write('')
st.subheader('DataFrame We Are Using')
st.dataframe(df)
st.write()
st.divider()


st.subheader('Select a stat to show the amount each player had with the amount of games played')

radio_selection = []
stat = st.radio('Choose a stat', ('at bats', 'hits', 'doubles', 'triples', 'home runs', 'runs', 'walks', 'strikeouts', 'batting average'))

if stat == 'at bats':
    radio_selection = df['at_bats'] 
elif stat == 'hits':
    radio_selection = df['hits']    
elif stat == 'doubles':
    radio_selection = df['doubles']
elif stat == 'triples':
    radio_selection = df['triples']
elif stat == 'home runs':
    radio_selection = df['home_runs']
elif stat == 'runs':
    radio_selection = df['runs']
elif stat == 'walks':
    radio_selection = df['walks']
elif stat == 'strikeouts':
    radio_selection = df['strikeouts']
else:
    radio_selection = df['AVG']
                           
fig = px.scatter(df, x= radio_selection , y  ='games', color ='player_name')
st.plotly_chart(fig, use_container_width=True)

st.write('')
st.divider()
st.write('')
st.write('')
st.subheader('You can also click the box below to show a histogram of the stat by position')

checkbox = st.checkbox('Click to view a histogram by position')

if checkbox:
    fig = px.histogram(df, x= radio_selection, color='position')
    st.plotly_chart(fig, use_container_width=True)
   




