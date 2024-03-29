import streamlit
import pandas as pd
import requests


streamlit.title('My Parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 &Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Eggs')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
selected_fruits = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[selected_fruits]

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruitvice Fruit Advise')

#to get what fruit information is needed
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered', fruit_choice)

#display fruityvice api response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response)

#streamlit.text(fruityvice_response.json())
#normalize the json verson of the response 
fruitvice_normalized = pd.json_normalize(fruityvice_response.json())
#display as dataframe

streamlit.dataframe(fruitvice_normalized)


