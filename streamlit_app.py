import streamlit
streamlit.title( 'My Parents New Heathy Diner' )


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

fruit_listed = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(fruit_listed)
streamlit.multiselect("Pick some fruits:", list(fruit_listed.index))

#fruit_listed = fruit_listed.set_index('Fruit')
#streamlit.multiselect("Pick some fruits:",list(fruit_listed.index),['Avocado','Strawberries'])
#fruits_to_show = fruit_listed.loc[fruits_selected]
#streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit advice!')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
