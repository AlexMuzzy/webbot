from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class EdgeWebBot:
    """
    Class. Initiates Microsoft Edge web browser and provides various functions for its sites interactivity.
    """

    def __init__(self):
        """
        Constructor. Initiates the Edge browser and navigates to the Amazon website.
        """
        self.driver = webdriver.Edge(executable_path=r'C:\Users\AlexMuzzy\PycharmProjects\amazon_bot\msedgedriver.exe')
        self.driver.get('https://amazon.co.uk')

    def search_amazon(self, url: str):
        """
        Selects the Amazon websites search box, and searches the given input string provided via `url`.
        :param url: URL of the website.
        """
        elem = self.driver.find_element_by_id("twotabsearchtextbox")
        elem.clear()
        elem.send_keys(url)
        elem.send_keys(Keys.RETURN)

    def close_edge_webdriver(self):
        """
        Closes the edge web browser.
        """
        self.driver.close()


# --- SCRIPT ---
seconds = 10

bot = EdgeWebBot()
bot.search_amazon('rtx 3070')
time.sleep(seconds)
bot.close_edge_webdriver()
