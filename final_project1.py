import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('survey.csv')


data.loc[data["mental_health_consequence"]=='Yes',"mental_cons"]=1
data.loc[data["mental_health_consequence"]=='No',"mental_cons"]=0
data.loc[data["mental_health_consequence"]=='Maybe',"mental_cons"]=0
freq=data.groupby('Country')["mental_cons"].sum().reset_index()
freq.sort_values("mental_cons", ascending=False, inplace=True)