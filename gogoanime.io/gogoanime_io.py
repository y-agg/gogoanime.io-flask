import requests 
from bs4 import BeautifulSoup

def newanime(url="https://www9.gogoanimehub.tv/new-season.html"):
    link=[i.find("a").get("href") for i in BeautifulSoup(requests.get(url).text,features="lxml").select('ul.pagination-list > li')]
    new_release=[i.get("title") for i in link for i in BeautifulSoup(requests.get(url+i).text,features="lxml").select('div.last_episodes > ul > li > p > a')]
    print(new_release)   
    return {'New Release': "New Release", 'List': new_release}
def search(word:str):
    if len(word) <=2:
        raise Exception("Word Entered lenght should be greater then 2")
    soup=BeautifulSoup(requests.get("https://www9.gogoanimehub.tv/search.html?keyword="+word).text,features="lxml")
    search_result=[i.get("title") for i in soup.select('div.last_episodes > ul > li > p > a')]
    if (len(search_result)==0):
        return {'Searched': word, 'List': 'No Result found // Try differnt keywords for better result'}
    else:
        return {'Searched': word, 'List': search_result}
if __name__=="__main__":
    print(search('Motto for'))
