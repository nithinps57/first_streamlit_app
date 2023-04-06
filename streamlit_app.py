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

def get_fruitvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
   # streamlit.text(fruityvice_response.json())--to print raw json
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#streamlit.write('The user entered ', fruit_choice)
   if not fruit_choice:
      streamlit.error("Please select the fruit to get information")
   else:
      back_from_function=get_fruitvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
except URLError as e:
   Sreamlit.error()

def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from fruit_load_list")
      #my_data_row = my_cur.fetchone()
      my_cnx.close()
      return my_cur.fetchall()
   
if streamlit.button('Get Fruit Load List'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows=get_fruit_load_list()
      streamlit.dataframe(my_data_rows)
      

def insert_row_to_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"');")
      my_cnx.close()
      return "Thanks for adding "+ add_my_fruit
      
add_my_fruit=streamlit.text_input('What Fruit you ike to add');
if streamlit.button('Add Fruit to List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function=insert_row_to_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
   

