import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from babel.numbers import format_currency

st.header('MTX BIKE :rage: ')
st.subheader('The Only Place you can Rent A BIKE :triumph: :triumph:')

day_df = pd.read_csv("https://raw.githubusercontent.com/felixb177/analisisdata/main/Bike-sharing-dataset/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/felixb177/analisisdata/main/Bike-sharing-dataset/hour.csv")

datetime_columns = ["dteday"]
for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])
    hour_df[column] = pd.to_datetime(hour_df[column])

# Visualize comparison of casual and registered users
last_ten = day_df.tail(50)
last_ten['dteday'] = pd.to_datetime(last_ten['dteday'])

st.subheader('Our service will gave you the best service!!')
st.subheader('even if you are not a registered user')

# Create a figure and axes for line plot
fig, ax = plt.subplots(figsize=(12, 5))

# Add lines to the axes with labels and colors
ax.plot(last_ten['dteday'], last_ten['casual'], label='casual', color='red')
ax.plot(last_ten['dteday'], last_ten['registered'], label='registered', color='blue')

# Set labels and title directly on the axes
ax.set_title('Casual Vs Registered', size=20)
ax.set_xlabel('Date', size=15)
ax.set_ylabel('Pengguna', size=15)
ax.legend()

# Display the plot in Streamlit, passing the created figure
st.pyplot(fig)

st.subheader('You can trust us')  

# Visualize data from the last 72 hours
last_two_days = hour_df.tail(72)
st.subheader('Affraid That You Missing Out on Our Bikes ?')
st.subheader('We Got You Cover !!!')

bike_rentals_by_hour = last_two_days.groupby(by='hr')['cnt'].mean().reset_index()

# Create a figure and axes for Seaborn bar plot
fig, ax = plt.subplots(figsize=(10, 6))

# Create the bar plot with Seaborn on the specified axes
sns.barplot(ax=ax, data=bike_rentals_by_hour, x="hr", y="cnt")

# Set plot labels and title directly on the axes
ax.set_xlabel('Hour')
ax.set_ylabel('Average Bikes Rented')
ax.set_title('Average Bikes Rented per Hour (Last 2 Days)', size=20)

# Display the plot in Streamlit, passing the created figure
st.pyplot(fig)

st.subheader('You can choose the best timming for riding a Bike :sparkles:')

st.subheader('What are you waiting for ?')
st.subheader('Rent Our Bikes')
st.subheader('Only at MTX BIKE :rage: ')