import streamlit
import pandas

streamlit.title('My parents New healthy Diner')
streamlit.header('아침식사 메뉴')
streamlit.text('🥣오메가 3 & 블루베리 오트밀')
streamlit.text('🥗케일, 시금치 & 로켓 스무디')
streamlit.text('🐔완숙 방목 계란')
streamlit.text('🥑🍞아보카도 토스트')
streamlit.header('🍌🥭 나만의 과일 스무디 만들기 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)) 
my_fruit_list = my_fruit_list.set_index("Fruit")
streamlit.dataframe(my_fruit_list)
