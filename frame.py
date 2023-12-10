import pandas as pd
import numpy as np
from datetime import datetime
def process_df(csvfile:str):
    df = pd.read_csv(
            csvfile,
            names=[
                "date",
                "temp_morning",
                "presure_morning",
                "wind_morning",
                "temp_evening",
                "presure_evening",
                "wind_evening",
            ],
            dtype=str,
        )
    if not ((df.isnull().sum()).eq(0).all()):
        df.dropna(inplace=True, ignore_index=True)
    df["temp_morning_f"] = df["temp_morning"].apply(celsius_to_fahrenheit)
    df["temp_evening_f"] = df["temp_evening"].apply(celsius_to_fahrenheit)
    return df

def group_by_month(df: pd.DataFrame):
    df["date"] = pd.to_datetime(df["date"])
    month_data = []
    for name, group in df.set_index("date").groupby(pd.Grouper(freq='M')):
        month_data.append(group)
    return month_data

def calculated_average(df: pd.DataFrame, parametr: str):
    month_data = group_by_month(df)
    averages = []
    for month_df in month_data:
        month_df[parametr] = pd.to_numeric(month_df[parametr], errors='coerce')
        avg_temperature = month_df[parametr].mean()
        averages.append(avg_temperature)
    return averages

def calculated_static_information(df: pd.DataFrame, parametr: str):
    try:
        return print(df[parametr].describe())
    except KeyError:
        print ("Error")

def filtered_temperature(df: pd.DataFrame , parametr:int, parametr2:str):
    df[parametr2] = pd.to_numeric(df[parametr2], errors='coerce')
    return df[df[parametr2]>= parametr]

def filtered_for_date(df:pd.DataFrame , start_date:str,end_date:str):
    return df[(pd.to_datetime(df["date"]) >= start_date) &  (pd.to_datetime(df["date"]) <= end_date)]

def celsius_to_fahrenheit(celsius:str):
    if celsius == "0":
        return "0"
    else:
        return (float(celsius) * 9/5) + 32




df = process_df("dataset.csv")
print(calculated_average(df,'temp_morning'))

# print(filtered_for_date(df,'2009-01-15','2015-01-15'))
# filtered_temperature(df,5,'temp_morning')
calculated_static_information(df,'temp_morning')
# calculated_static_information(df,'temp_morning_f')
# calculated_static_information(df,'temp_evening')
# calculated_static_information(df,'temp_evening_f')

print(df)