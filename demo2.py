from turtle import width
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

from vega_datasets import data

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

x_limit = 100
x_axis = np.arange(0,x_limit,1)
y_data = np.random.rand(100)
df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter = alt.Chart(df).mark_point().encode(x='x:Q',
    y='y:Q')
st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Change 1 : Added tooltip to the data points 
- Change 2 : Added title to the Scatter plot
- Change 3 : Modified data points size and color using y values
- Change 4 : Changed mark_point to mark_circle function to display data points in circles 
- Change 5 : Used Interactive function to zoom in and zoom out plot 
""")

scatter = alt.Chart(df).mark_circle().encode(
    x='x:Q', y='y:Q', size='y', color='y', 
    tooltip=['x', 'y']).properties(
    title='Sctter plot of X vs Y'
).interactive()

st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
The graph I have choosen is Simple Scatter plot with tooltip https://altair-viz.github.io/gallery/scatter_tooltips.html

The 2 changes I made were:
- Change 1 : Changed the mark circle function to mark point to change the shape of the points based on the Origin 
- Change 2 : Created another chart to display miles in ascending order of origin and concatinated both the charts to display 
"""
)

source = pd.read_json('imdb.json').astype(str)

st.dataframe(source)

bar = alt.Chart(source).mark_bar(color = '#03cffc').encode(
    alt.X("IMDB_Rating:Q", bin = True , title  = "yty"),
    alt.Y('count()', title = 'Records')
)

st.altair_chart(bar , use_container_width= True)

st.write(source)

