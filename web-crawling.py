# pip install bs4
# pip install lxml
# import bs4
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
# import urllib.request as req

URL = "https://www.indeed.co.in/jobs?q=python&l="

response = urlopen(URL)
# print(response)
# htmlSourceCode = bs4.BeautifulSoup(response, "lxml")
htmlSourceCode = BS(response, "lxml")
# print(htmlSourceCode)

heading = htmlSourceCode.find('h2', 'title')
print(heading.text.strip())
companyName = htmlSourceCode.find('span', 'company')
print(companyName.text.strip())
jobLocation = htmlSourceCode.find('div', 'location')
print(jobLocation.text.strip())
salary = htmlSourceCode.find('span', 'salaryText')
print(salary.text.strip())
summary = htmlSourceCode.find('div', 'summary')
jobDetailsList = summary.find('ul')
# li = jobDetailsList.find('li')
# print(li.text.strip())
listOfLIs = jobDetailsList.find_all('li')
for li in listOfLIs:
    print(li.text.strip())
