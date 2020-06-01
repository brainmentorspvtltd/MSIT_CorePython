from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
from urllib.request import urlretrieve

response = urlopen("https://www.imdb.com")

htmlSourceCode = BS(response, "lxml")

images_list = htmlSourceCode.find_all('img')

# for i, image in enumerate(iamges_list):
#     print(i, image)
#     print("--------------------------------")

for i, image in enumerate(images_list):
    imageLink = image['src']
    urlretrieve(imageLink, f"image_{i+1}.jpg")
