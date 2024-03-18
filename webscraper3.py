from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+%2C+Python&txtLocation=&cboWorkExp1=0').text
soup = BeautifulSoup(req, 'lxml')

my_skills = input('Enter the skills you have >> ')

job_cards = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job_card in job_cards:
    post_date = job_card.find('span', class_='sim-posted').text
    if 'few days' in post_date:
        job_title = job_card.header.h2.a.text
        job_skills = job_card.find('span', class_='srp-skills').text

        skill_matched = False
        for my_skill in my_skills.split(','):
            if my_skill in job_skills:
                skill_matched = True

        if skill_matched:
            print(f'Job Title: {job_title.strip()}')
            print(f'Required skills: {job_skills.strip()}')
            print('\n')