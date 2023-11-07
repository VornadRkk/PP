import time

from bs4 import BeautifulSoup
import csv
import datetime
import os
import re
import requests

for year in range(2020,2024):
     for moths in range(1,13):
         Url = "https://www.gismeteo.ru/diary/4618/" + str(year) + "/" + str(moths) + "/"
         headers = {
         "Accept":"*/*",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX)"
         }
         req = requests.get(Url,headers = headers)
         src = req.text
         try:
             with open("index.html", "w") as file:
                 file.write(src)
         except Exception:
             continue
         # with open("index.html")as file:
         #     src = file.read()
         soup = BeautifulSoup(src,"lxml")
         try:
             table = soup.find("table").find("tbody").find_all("tr")
         except Exception:
             continue
         data_table = []
         if (moths < 10):
             moun = '0' + str(moths)
         else:
             moun = str(moths)
         for item in table:
             data_td = item.find_all('td')
             day = data_td[0].text
             temp_morning = data_td[1].text
             presure_morning = data_td[2].text
             wind_morning = data_td[5].text
             temp_evening = data_td[6].text
             wind_evening = data_td[10].text
             presure_evening = data_td[7].text
             data_table.append(
                 {
                     "day": str(year)+"-" +str(moun) +"-"+day,
                     "temp_morning": temp_morning,
                     "presure_morning": presure_morning,
                     "wind_morning": wind_morning,
                     "temp_evening": temp_evening,
                     "presure_evening": presure_evening,
                     "wind_evening": wind_evening,

                 }
             )
         with open('dataset.csv', 'a', newline='') as csvfile:
              for item in data_table:
                 writer = csv.writer(csvfile,delimiter=",")
                 writer.writerow([item["day"],item["temp_morning"],item["presure_morning"],item["wind_morning"],item["temp_evening"],item["presure_evening"],item["wind_evening"]])

with open('dataset.csv', newline='') as f:
    fieldnames = ['data', 'temp_morning', 'presure_morning','wind_morning', 'temp_evening', 'presure_evening', 'wind_evening']
    reader = csv.DictReader(f, fieldnames=fieldnames)
    for row in reader:
        file_writer = csv.writer(open('dataset-number.csv', 'a', newline=''), lineterminator="\r")
        file_writer.writerow([row['data']])
        file_writer = csv.writer(open('dataset-data.csv', 'a', newline=''), lineterminator="\r")
        file_writer.writerow([row["temp_morning"],row["presure_morning"],row["wind_morning"],row["temp_evening"],row["presure_evening"],row["wind_evening"]])

for year in range(2020, 2024):
    output_file = f'dataset-{year}0101_{year}1231.csv'


    with open('dataset.csv', newline='') as f:
        fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening',
                      'wind_evening']
        reader = csv.DictReader(f, fieldnames=fieldnames)


        with open(output_file, 'w', newline='') as file_writer:
            writer = csv.writer(file_writer, lineterminator="\r")



            for row in reader:
                year_in_row = row['data'].split('-')[0]
                if year_in_row == str(year):
                    writer.writerow([row['data'], row["temp_morning"], row["presure_morning"], row["wind_morning"],row["temp_evening"], row["presure_evening"], row["wind_evening"]])


for year in range(2020, 2024):
    input_file = f'dataset-{year}0101_{year}1231.csv'

    with open(input_file, 'r', newline='') as file:
        fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening',
                      'wind_evening']
        reader = csv.DictReader(file, fieldnames=fieldnames)
        first_row = next(reader)
        year = first_row['data'][:4]
        first_date = first_row['data'][5:10]

        last_date = None
        for row in reader:
            last_date = row['data'][5:10]

        if last_date:
            output_file = f'dataset-{year}{first_date}_{year}{last_date}.csv'
            file.close()
            os.rename(input_file, output_file)

with open('dataset.csv', newline='') as f:
    fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening',
                  'wind_evening']
    reader = csv.DictReader(f, fieldnames=fieldnames)

    current_week_start = None
    current_week_number = 1
    current_week_data = []

    for row in reader:


        date = datetime.datetime.strptime(row['data'], '%Y-%m-%d')
        day_of_week = date.weekday()


        if current_week_start is None:
            current_week_start = date - datetime.timedelta(days=day_of_week)

        if day_of_week == 6:

            output_folder = 'week'
            os.makedirs(output_folder, exist_ok=True)
            output_file = os.path.join(output_folder, f'dataset-week-{current_week_number}.csv')

            with open(output_file, 'w', newline='') as file_writer:
                writer = csv.writer(file_writer, lineterminator="\r")

                for week_data in current_week_data:
                    writer.writerow(week_data)

            current_week_number += 1
            current_week_start = None
            current_week_data = []

        current_week_data.append(
            [row['data'], row["temp_morning"], row["presure_morning"], row["wind_morning"], row["temp_evening"],row["presure_evening"], row["wind_evening"]])
def get_data_for_date(csv_filename, target_date):
    with open(csv_filename, newline='') as f:
        fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening', 'wind_evening']
        reader = csv.DictReader(f, fieldnames=fieldnames)

        for row in reader:
            date = row['data']
            if date == target_date:
                return {
                    "data": row['data'],
                    "temp_morning": row['temp_morning'],
                    "presure_morning": row['presure_morning'],
                    "wind_morning": row['wind_morning'],
                    "temp_evening": row['temp_evening'],
                    "presure_evening": row['presure_evening'],
                    "wind_evening": row['wind_evening']
                }
    return None
csv_filename = 'dataset.csv'
target_date = '2023-10-27'
data = get_data_for_date(csv_filename, target_date)

if data:
    print("Данные для даты", target_date, "найдены:")
    print(data)
else:
    print("Данные для даты", target_date, "не найдены.")


class DataIterator:
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename
        self.data_iter = self.data_generator()

    def data_generator(self):
        with open(self.csv_filename, newline='') as f:
            fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening', 'wind_evening']
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for row in reader:
                date = row['data']
                data = {
                    "data": date,
                    "temp_morning": row['temp_morning'],
                    "presure_morning": row['presure_morning'],
                    "wind_morning": row['wind_morning'],
                    "temp_evening": row['temp_evening'],
                    "presure_evening": row['presure_evening'],
                    "wind_evening": row['wind_evening']
                }
                yield data

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.data_iter)
        except StopIteration:
            raise StopIteration


csv_filename = 'dataset.csv'
data_iter = DataIterator(csv_filename)


try:
    next_data = next(data_iter)
    if next_data:
        print(next_data)
    else:
        print("Данных больше нет.")
except StopIteration:
    print("Данных больше нет.")
try:
    next_data = next(data_iter)
    if next_data:
        print(next_data)
    else:
        print("Данных больше нет.")
except StopIteration:
    print("Данных больше нет.")


