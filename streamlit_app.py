import streamlit
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)    
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
#streamlit.write('The user entered ', fruit_choice)

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()    

streamlit.title('My parents New healthy Diner')
streamlit.header('아침식사 메뉴')
streamlit.text('🥣오메가 3 & 블루베리 오트밀')
streamlit.text('🥗케일, 시금치 & 로켓 스무디')
streamlit.text('🐔완숙 방목 계란') 
streamlit.text('🥑🍞아보카도 토스트')
streamlit.header('🍌🥭 나만의 과일 스무디 만들기 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) 
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("SELECT * from fruit_load_list")
       return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.fruit_load_list values('"+ new_fruit +"')")
         return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
  
streamlit.stop()

