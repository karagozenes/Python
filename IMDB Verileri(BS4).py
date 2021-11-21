import requests
from bs4 import BeautifulSoup



def IMDB():
    url = "https://www.imdb.com/chart/top/"
    response = requests.get(url)
    icerik = response.content

    soup = BeautifulSoup(icerik,"html.parser")

    for film in soup.find_all("td",{"class":"titleColumn"}):
        film = film.text
        film = film.strip()
        film = film.replace("\n"," ")
        film = film.replace("       ", "")
        print(film)


IMDB()