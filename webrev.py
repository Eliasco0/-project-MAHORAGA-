import  requests

from bs4 import BeautifulSoup

url ='https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296776-extrayez-et-transformez-des-donnees-avec-lextraction-web '

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.head)

soupi = soup.find_all("p", class_='gem-c-document-list__item-description')
