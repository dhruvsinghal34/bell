import random 
import csv
import pandas as p
import plotly.figure_factory as ff

df = p.read_csv("data.csv")

fiqure = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Result"])
fiqure.show()
    