from bs4 import BeautifulSoup
import requests
URL = "https://www.gismeteo.ru"
headers = {
"Accept":"*/*",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition Yx GX)"
}
req = requests.get(URL,headers = headers)
src = req.text
print(src)