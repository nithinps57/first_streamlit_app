import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast menu')

streamlit.text('🥣 Omega 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale ,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado tost')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
# streamlit.text(fruityvice_response.json())--to print raw json


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)

#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#streamlit.write('The user entered ', fruit_choice)
   if not fruit_choice:
      Streamlit.error("Please select the fruit to get information")
   else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      # streamlit.text(fruityvice_response.json())--to print raw json
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)
except URL Error as e;
  Sreamlit.error()




my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.dataframe(my_data_row)

add_my_fruit=streamlit.text_input('What Fruit you ike to add');

my_cur.execute("insert into fruit_load_list values ('test streamlit');")
