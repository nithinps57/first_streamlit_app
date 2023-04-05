import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast menu')

streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale ,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado tost')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
