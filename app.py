import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("IPL Exploratory Data Analysis")

# Load datasets
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

# Fill missing values
matches.fillna(0, inplace=True)
deliveries.fillna(0, inplace=True)

# -----------------------------------
# Most Winning Teams
# -----------------------------------

st.subheader("Most Winning IPL Teams")

winning_teams = matches['winner'].value_counts().head(10)

fig1, ax1 = plt.subplots(figsize=(10, 6))

sns.barplot(
    x=winning_teams.values,
    y=winning_teams.index,
    palette="viridis",
    ax=ax1
)

ax1.set_xlabel("Number of Wins")
ax1.set_ylabel("Teams")

st.pyplot(fig1)

# -----------------------------------
# Top Run Scorers
# -----------------------------------

st.subheader("Top IPL Run Scorers")

top_scorers = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots(figsize=(10, 6))

sns.barplot(
    x=top_scorers.values,
    y=top_scorers.index,
    palette="magma",
    ax=ax2
)

ax2.set_xlabel("Total Runs")
ax2.set_ylabel("Players")

st.pyplot(fig2)

# -----------------------------------
# Stadium Trends
# -----------------------------------

st.subheader("Most Used IPL Stadiums")

stadium_trends = matches['venue'].value_counts().head(10)

fig3, ax3 = plt.subplots(figsize=(12, 6))

sns.barplot(
    x=stadium_trends.values,
    y=stadium_trends.index,
    palette="coolwarm",
    ax=ax3
)

ax3.set_xlabel("Number of Matches")
ax3.set_ylabel("Stadium")

st.pyplot(fig3)

# -----------------------------------
# Dataset Preview
# -----------------------------------

st.subheader("Matches Dataset Preview")
st.write(matches.head())

st.subheader("Deliveries Dataset Preview")
st.write(deliveries.head())

# -----------------------------------
# Success Message
# -----------------------------------

st.success("IPL Exploratory Data Analysis Completed Successfully!")