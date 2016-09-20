from bs4 import BeautifulSoup
import requests

url = 'http://www.moneysmart.sg/credit-cards/anz-optimum-world-mastercard-credit-card'
r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, "html.parser")

