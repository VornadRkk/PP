from bs4 import BeautifulSoup
import requests
Url = "https://www.gismeteo.ru/diary/4368/2023/9/"
headers = {
"Accept":"*/*",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX)"
}
req = requests.get(Url,headers = headers)
src = req.text
with open("index.html","w")as file:
    file.write(src)
print(src)
# with open("index.hutml") as file:
#     src = file.read()
# soup = BeautifulSoup(src,"lxml")
# all_days = soup.find_all(class_ ="current-time")
# for item in all_days:
#     item_text = item.text
#     print(item_text)