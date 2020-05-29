from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

URL = "https://www.indeed.co.in/jobs?q=python&l="

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
