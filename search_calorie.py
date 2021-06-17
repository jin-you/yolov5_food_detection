import requests
from bs4 import BeautifulSoup as bs

# 파파고 API
def get_translate(text):
    text = text.capitalize()

    client_id = "RdYkXsVY_QfOOvVwX5vG" # <-- client_id 기입
    client_secret = "noPzgToDOJ" # <-- client_secret 기입

    data = {'text' : text,
            'source' : 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)


food_name_en = 'banana'
food_name = get_translate(food_name_en)

url = f'https://www.dietshin.com/calorie/calorie_search.asp?keyword={food_name}'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = bs(html, 'html.parser')
    
    # 검색결과 최상단 결과 가져오기
    calorie = soup.select_one('#container > div.contents.calorieDc > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    print(food_name, str(calorie)[4:-5])
else:
    print(response.status_code)
    
    