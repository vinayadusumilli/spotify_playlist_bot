import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4


class WebDataManager:
    """
    WebDataManager class takes the billboard url and scrap the data and finds and
    return top songs of the requested week
    """
    def __init__(self, url) -> None:
        self.url = url
        self.songs_list = []

    def get_songs(self) -> list:
        """
        >get_songs
        :return: list of top songs of the week
        """
        response = requests.get(self.url)
        web_data = response.text
        soup = BeautifulSoup(web_data, features="html.parser")
        titles = soup.find_all(name="ul", class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-"
                                                 "100p lrv-u-flex-direction-column@mobile-max")
        for title in titles:
            self.songs_list.append(title.select_one(selector="li h3").get_text().strip())
        return self.songs_list
