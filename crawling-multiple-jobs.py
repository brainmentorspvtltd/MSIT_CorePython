# pip install babel
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
from urllib.parse import urlencode
from babel.numbers import format_currency
from decimal import Decimal

# URL = "https://www.indeed.co.in/jobs?q=python&l="
query = input("Job title, keywords, or company: ")
minSalary = int(input("Enter minimum monthly salary you want: "))
minSalary = str(minSalary * 12)
minSalary = format_currency(Decimal(minSalary), "INR")[:-3]

query = f"{query} {minSalary}"
print(query)

URL = "https://www.indeed.co.in/jobs?"
URL = URL + urlencode({"q": query, "l": "Delhi, Delhi"})
print(URL)


response = urlopen(URL)
htmlSourceCode = BS(response, "lxml")

jobs = htmlSourceCode.find_all('div', 'jobsearch-SerpJobCard')
# for job in jobs:
for counter, job in enumerate(jobs):
    print(f"Job {counter + 1}")

    heading = job.find('h2', 'title')
    print(heading.text.strip())

    companyName = job.find('span', 'company')
    print(companyName.text.strip())

    jobLocation = job.find('div', 'location')
    if jobLocation != None:
        print(jobLocation.text.strip())
    else:
        jobLocation = job.find('span', 'location')
        print(jobLocation.text.strip())

    salary = job.find('span', 'salaryText')
    print(salary.text.strip()) if salary != None else print(
        "Salary not specified")

    summary = job.find('div', 'summary')
    jobDetails = summary.find('ul')
    listOfLIs = jobDetails.find_all('li')
    print("Job details:")
    for li in listOfLIs:
        print(" - ", li.text.strip())
    print("\n------------------------------------------\n")
