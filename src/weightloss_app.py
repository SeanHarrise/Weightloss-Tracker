import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.title("Weightloss Goals")

weight_df = pd.read_csv("/Users/seanharris/git/Weightloss-Tracker/test_input.csv")
weight_df = weight_df[['Day', 'Weight']]

weight_df['Day'] = pd.to_datetime(weight_df['Day'])

# Sidebar for user input
y_min = weight_df['Weight'].min()
y_max = weight_df['Weight'].max()

# Plotting the line chart using Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(weight_df.index, weight_df['Weight'], marker='o', linestyle='-', color='b', label='Value')
ax.set_xlabel('Day')
ax.set_ylabel('Weight')
ax.set_title('Line Chart Example')

weight_df["avg7"] = weight_df["Weight"].rolling(window=7).mean()

line = alt.Chart(weight_df).mark_line(color="mediumorchid").encode(x = alt.X("Day"), y = alt.Y("Weight", scale=alt.Scale(domain=[y_min, y_max])))
point = alt.Chart(weight_df).mark_point(size=75, filled=True, opacity=1, color="mediumorchid").encode(x = alt.X("Day"), y = alt.Y("Weight", scale=alt.Scale(domain=[y_min, y_max])))
line1 = alt.Chart(weight_df).mark_line(color="darkorange").encode(x = alt.X("Day"), y = alt.Y("avg7", scale=alt.Scale(domain=[y_min, y_max])))
# point1 = alt.Chart(weight_df).mark_point(size=75, filled=True, opacity=1).encode(x = alt.X("Day"), y = alt.Y("Weight", scale=alt.Scale(domain=[y_min, y_max])))

c = alt.layer(point, line, line1)

st.altair_chart(c, use_container_width=True)

st.dataframe(weight_df)