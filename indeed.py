import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', {"class":"pagination"})
    links = pagination.find_all('a')  # list
    pages = []
    for link in links[:-1]:  # 맨 마지막에는 next이기 때문에 제외함.
        # print(link.find('span'))
        # pages.append(link.find("span").string)
        pages.append(int(link.string)) # 특정 요소 하위의 요소에 string이 오직 하나만 있다면 굳이 하위 요소로 가지 않아도 beautifulsoup이 알아서 string을 찾아줌
    #
    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    for result in results:
        title = result.find("h2", {"class": "title"}).find("a")["title"]
        print(title)
    return jobs