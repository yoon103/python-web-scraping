import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# print(indeed_result.text)

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
# print(indeed_soup)

pagination = indeed_soup.find('div', {"class":"pagination"})
# print(pagination)

links = pagination.find_all('a')  # list
# print(pages)
pages = []
for link in links[:-1]:  # 맨 마지막에는 next이기 때문에 제외함.
    # print(link.find('span'))
    # pages.append(link.find("span").string)
    pages.append(int(link.string)) # 특정 요소 하위의 요소에 string이 오직 하나만 있다면 굳이 하위 요소로 가지 않아도 beautifulsoup이 알아서 string을 찾아줌

max_page = pages[-1]
