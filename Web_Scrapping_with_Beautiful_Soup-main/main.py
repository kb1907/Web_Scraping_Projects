from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://changemavie.com/episodes-2').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('changemavie_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Episode_Number', 'Episode_Title', 'Link', 'Episode_Summary'])


for title in soup.find_all('div', class_='summary-content'):

    headline = title.find('a', class_='summary-title-link').text
    episode_number = headline[1:4]
    episode_title = headline[6:]

    link = title.find('a', class_='summary-title-link')['href']
    link = 'https://changemavie.com' + link

    episode_summary = title.find('div', class_='summary-excerpt').text[1:-1]

    csv_writer.writerow([episode_number, episode_title, link, episode_summary])

csv_file.close()
