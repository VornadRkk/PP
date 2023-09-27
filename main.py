from bs4 import BeautifulSoup
import csv
import requests
Url = "https://www.gismeteo.ru/diary/4368/2023/9/"
headers = {
"Accept":"*/*",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX)"
}
req = requests.get(Url,headers = headers)
src = req.text
with open("index.html")as file:
    src = file.read()
soup = BeautifulSoup(src,"lxml")
table = soup.find("table").text
with open('dataset.csv', 'w', newline='') as csvfile:
    for item in table:
        tabledata = soup.find("table").find("tbody").find("tr").find("td", class_="first").text
        tabletemp = soup.find("table").find("tbody").find("tr").find("td",class_ ="first_in_group positive").text
        tablepresure = soup.find("table").find("td",class_ ="first_in_group positive").find_next().text
        table_wind = soup.find("table").find("span").text
        file_writer = csv.writer(csvfile, delimiter=",", lineterminator="\r")
        file_writer.writerow([tabledata,tabletemp,tablepresure,table_wind])
