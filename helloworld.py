import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
def get_data():
    url = "https://raw.githubusercontent.com/Hernan4444/MyAnimeList-Database/master/data/anime.csv"
    return pd.read_csv(url)
df_data = get_data()
st.write(f'### Here is our filtered data')
df_data = df_data.filter(
    items=['Name', 'Score', 'Type', 'Source', 'Genres', 'Episodes', 'Duration', 'scored_by', 'Completed', 'Dropped'])
df_data.head()
df_data
df_data['Completed'] = df_data['Completed'].astype(int)
tips = px.data.tips()
figure = px.histogram(df_data, y="Type", title='Distribution of anime by type')
figure
figure = px.histogram(df_data, x="Type", color="Source", title='Distribution of anime by type including the source')
figure
fig, ax = plt.subplots()
sns.scatterplot(data=df_data, x='Score', y='Completed', hue='Type', style='Type')
ax.set_ylim(bottom=0, top=1000000)
st.pyplot(fig)
score_chosen = st.slider('Completed',min_value=0, max_value=1000000)
b=df_data.sort_values(by=['Completed'])
c = b.loc[b['Completed']>score_chosen]
fig, ax=plt.subplots(1,1, figsize=(10,10))
sns.scatterplot(data=c, x="Episodes", y='Completed')
st.pyplot(fig)
st.write("Some magic right here")

start_btn = st.button('Magic button')
if start_btn:
    st.balloons()
