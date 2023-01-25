
import streamlit

streamlit.title('My parents New Healtly DIner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Let´s put list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:",list(my_fruits_list.index))

#Display the table on the page
streamlit.dataframe(my_fruit_list)
