import requests
from bs4 import BeautifulSoup as bs


food_name = '제육볶음'
url = f'https://www.dietshin.com/calorie/calorie_search.asp?keyword={food_name}'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = bs(html, 'html.parser')
    
    calorie = soup.select_one('#container > div.contents.calorieDc > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    print(food_name, str(calorie)[4:-5])
else:
    print(response.status_code)