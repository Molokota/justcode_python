import requests
from bs4 import BeautifulSoup

for i in range(1, 4):
    url = f"https://www.olx.kz/list/q-%D0%B5%D0%BB%D0%BA%D0%B8/?page={i}"
    response = requests.get(url)
    olx = BeautifulSoup(response.text, "lxml")
    page = olx.find_all("div", class_="css-1sw7q4x")
    count_page = 1
    count = 1
    for page in page:
        # Выводит не более 5-ти объявлений на страницу
        if count_page <= 5:
            # Исключение ошбики по url адресу возникающей после 52-го объявления на странице
            try:
                url_num = page.a["href"]
            except:
                print("Ошибка по url")
            response_2 = requests.get(f"https://www.olx.kz{url_num}")
            olx_ful = BeautifulSoup(response_2.text, "lxml")
            soup = olx_ful.find("div", class_="css-1t507yq er34gjf0")
            # Выводится объявление если в описании есть текст
            if len(soup.text) > 0:
                print(f"""
--------------------------ПАРСИМ {i}-Ю СТРАНИЦУ---------------------
--------------------------ОБЪЯВЛЕНИЕ № {count}--------------------------
{soup.text}
            """)
                count += 1
                count_page += 1
            else:
                print(f"есть описание {i}-я страница / № {count}")
                count += 1
        else:
            print("нет описания")
            break
        # olx = BeautifulSoup(response.text, "lxml")
        # page = olx.find_all("div", class_="css-qfzx1y")