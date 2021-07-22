import requests
from bs4 import BeautifulSoup
import time

print('type your unfamiliar skill')
unfamiliar_skill = input('>')
def find_jobs():
    html = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=React&txtLocation=").text
    soup = BeautifulSoup(html, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More info: {more_info}')
                print(f'File saved: {index}')

find_jobs()
# if __name__ == '__main__':
#     while True:
#         find_jobs()
#         time_wait = 10
#         print(f'waiting for {time_wait} minutes...')
#         time.sleep(time_wait * 60)