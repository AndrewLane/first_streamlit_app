import streamlit
import pandas
import requests

streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Favorites ")

streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach, and Rocket Smoothie")
streamlit.text("🐔Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display table on the page
streamlit.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header("Fruityvice Fruit Advice!")
# streamlit.text(fruityvice_response.json())

# put the data into a df
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# spit out the df to the screen
streamlit.dataframe(fruityvice_normalized)
