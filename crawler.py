import requests
from bs4 import BeautifulSoup

#url = "https://www.turo.com"
url = "https://turo.com/us/en/search?country=US&defaultZoomLevel=11&deliveryLocationType=city&endDate=10%2F14%2F2024&endTime=10%3A00&isMapSearch=false&itemsPerPage=200&latitude=47.6061389&location=Seattle%2C%20WA%2C%20USA&locationType=CITY&longitude=-122.3328481&pickupType=ALL&placeId=ChIJVTPokywQkFQRmtVEaUZlJRA&region=WA&sortType=RELEVANCE&startDate=10%2F11%2F2024&startTime=10%3A00&useDefaultMaximumDistance=true"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')

#articles = soup.find_all('div', class_="")
#print(articles)

with open('output.html', 'w', encoding='utf-8') as f:
     f.write(response.text)