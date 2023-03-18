""" Python scraping of one job page. """
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, Timeout

URL = 'https://remote.co/remote-jobs/developer/'

# checking the correctness of the page URL
try:
    response = requests.get(URL, timeout=15)
    response.raise_for_status()
except HTTPError as http_error:
    print(f'An HTTP error occurred \n{http_error}')
except Timeout:
    print('The request timed out')
except Exception as exc:
    print(f'One of the errors occurred \n{exc}')
else:
    find_by_keyword = input('\tEnter a job keyword: ')

    # The .content attribute holds raw bytes, which can be decoded better than the text representation page.text
    soup = BeautifulSoup(response.content, 'html.parser')

    results = soup.find(class_='card bg-white m-0')
    jobs_list = results.find_all('a', class_='card m-0 border-left-0 border-right-0 border-top-0 border-bottom')

    counter_vacancies = 1
    for job in jobs_list:
        vacancy_title = job.find('span', class_='font-weight-bold larger')
        company_name = job.find('img', class_='card-img')
        company_tags = job.find('p', class_='m-0 text-secondary')
        time_from_publish = job.find('span', class_='float-right d-none d-md-inline text-secondary')
        if find_by_keyword.lower() in vacancy_title.text.lower():
            print(f'№{counter_vacancies} Title: ', vacancy_title.text)
            print('Company: ', company_name["alt"])
            print('Company tags:')
            for tag in company_tags.find_all('span', class_='badge badge-success'):
                print('\t' + tag.text)
            print('Time from job posting: ', time_from_publish.text.strip())
            print("Link to the vacancy ->  ", 'https://remote.co' + job["href"])
            print()
            counter_vacancies += 1

    print(f"""
    We have checked {len(jobs_list)} vacancies.
    These are all matches at the moment.""")
