from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+%2C+Python&txtLocation=&cboWorkExp1=0').text
soup = BeautifulSoup(html_text, 'lxml')
# grab the card with a jobs info
job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
# grab a the companies name
company_name = job.find("h3", class_="joblist-comp-name").text
# remove white spaces and new-line elements
company_name = company_name.replace("  ", "")
company_name = company_name.replace("\n", "")

print(company_name)
