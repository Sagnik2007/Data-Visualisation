import pandas as pd
import plotly_express as px

df = pd.read_csv(
    "C:/Users/milindo/Desktop/All Desktop Files Dad/WhiteHat Jr/Project 103/countries_aggregated.csv")
fig = px.scatter(df, x="Date", y="Confirmed Cases",
                 color="Country", title="No Of Cases Of Covid-19 Every Day")

fig.show()