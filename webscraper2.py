from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+%2C+Python&txtLocation=&cboWorkExp1=0').text

soup = BeautifulSoup(req, 'lxml')

job_cards = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job_card in job_cards:
    post_date = job_card.find('span', class_='sim-posted').text
    post_date = post_date.replace('\n', '')
    print(post_date)

    if 'Posted few days ago' in post_date:
        job_title = job_card.find('a').text
        job_title = job_title.replace('  ', '')
        job_title = job_title.replace('\n', '')
        print(job_title)