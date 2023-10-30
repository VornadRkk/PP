import time

from bs4 import BeautifulSoup
import csv
import re
import requests
for year in range(1997,2024):
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
                    "day": str(year)+"-" +str(moths) +"-"+day,
                    "temp_morning": temp_morning,
                    "presure_morning": presure_morning,
                    "wind_morning": wind_morning,
                    "temp_evening": temp_evening,
                    "presure_evening": presure_evening,
                    "wind_evening": wind_evening,

                }
            )

        with open('dataset-number.csv', 'a', newline='') as csvfile:
            for item in data_table:
                writer = csv.writer(csvfile,delimiter=",")
                writer.writerow([item["day"]])
        with open('dataset-data.csv', 'a', newline='') as csvfile:
            for item in data_table:
                writer = csv.writer(csvfile,delimiter=",")
                writer.writerow([item["temp_morning"],item["presure_morning"],item["wind_morning"],item["temp_evening"],item["presure_evening"],item["wind_evening"]])