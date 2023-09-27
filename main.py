from bs4 import BeautifulSoup
import csv
import requests
# Url = "https://www.gismeteo.ru/diary/4618/2023/9/"
# headers = {
# "Accept":"*/*",
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX)"
# }
# req = requests.get(Url,headers = headers)
# src = req.text
with open("index.html")as file:
    src = file.read()
soup = BeautifulSoup(src,"lxml")
table = soup.find("table").find("tbody").find_all("tr")
data_table = []
for item in table:
    data_td = item.find_all('td')
    day = data_td[0].text+soup.find("div",class_="header").text
    temp_morning = data_td[1].text
    presure_morning = data_td[2].text
    wind_morning = data_td[5].text
    temp_evening = data_td[6].text
    wind_evening = data_td[10].text
    presure_evening = data_td[7].text

    data_table.append(
        {
            "day": day,
            "temp_morinng": temp_morning,
            "presure_morning": presure_morning,
            "wind_morning": wind_morning,
            "temp_evening": temp_evening,
            "presure_evening": presure_evening,
            "wind_evening": wind_evening,

        }
    )

with open('dataset.csv', 'w', newline='') as csvfile:
    for item in data_table:
        file_writer = csv.writer(csvfile)
        file_writer.writerow([item])
