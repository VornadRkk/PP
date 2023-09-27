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
        file_writer = csv.writer(csvfile, delimiter=",", lineterminator="\r")
        file_writer.writerow([(soup.find("table").text)])
# for item in table:
#         file.write(soup.find("table").find(class_ = "td.first").text)
# with open(" dataset.csv","w")as file:
#     file.write()

# for item in table:
