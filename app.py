import pandas as pd
import streamlit as st
import plotly.express as px


# Reading the preprocessed DataFraame
df = pd.read_csv('baseball_hitting_pp.csv')



#creates a title for our app
st.title('Major Leauge Baseball Hitting Stats Throughout History')
st.write('')
st.subheader('Introduction')
st.write("Have you ever wondered who has the most homeruns in MLB history or where your favorite player ranks on the all-time hits list? This is app will help you find out. Simply choose the stat you want to see.")
st.write('')
st.divider()
st.write('')


#Showing the DataFrame 
st.header('MLB Hitting Stats')
st.divider()
st.write('')
st.subheader('DataFrame We Are Using')
st.dataframe(df)
st.write()
st.divider()





st.subheader('Select a stat to show the amount each player had with the amount of games played')
# Creating our radio selection.
radio_selection = []
stat = st.radio('Choose a stat', ('at bats', 'hits', 'doubles', 'triples', 'home runs', 'runs', 'walks', 'strikeouts', 'batting average'))
# loop to determine what radio_selection =
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


# Creates a scatter plot based on our radio selection.
fig = px.scatter(df, x= radio_selection , y  ='games', color ='player_name')
fig.plotly_chart(fig, use_container_width=True)

st.write('')
st.divider()
st.write('')
st.write('')
st.subheader('You can also click the box below to show a histogram of the stat by position')


#Gives an option to select a checkbox to view our radio selection stat as a histogram by position.
fig2= px.histogram(df, x= radio_selection, color='position')

checkbox = st.checkbox('Click to view a histogram by position')

if checkbox:
    st.plotly_chart(fig2, use_container_width=True)
   




