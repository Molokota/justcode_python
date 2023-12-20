import requests
from bs4 import BeautifulSoup
import json

url = f"https://api.technodom.kz/katalog/api/v1/products/category/smartfony?city_id=5f5f1e3b4c8a49e692fefd70&limit=24&brands=apple&sorting=score&price=0"
data = requests.get(url)
json_data = json.loads(data.text)

# Сохраняем данные в файл в формате JSON для просмотра словаря
with open("otus.json", "w", encoding="utf-8") as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

# Python  словарь
apple = dict()

# Счетчик
count = 1

# Цикл перебора словаря
for i in json_data["payload"]:
    for j in i["variants"]["colors"]:
        if "256gb" in j["uri"] and count <= 20:
            apple[f"{count}"] = f"https://www.technodom.kz/p/{j['uri']}"    # добавляем ключь и значение в словарь python
            count += 1

# Сохраняем данные в файл в формате JSON
with open("apple.json", "w", encoding="utf-8") as file:
    json.dump(apple, file, ensure_ascii=False, indent=4)

print(apple)



