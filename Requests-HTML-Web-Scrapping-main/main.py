import csv
from requests_html import HTML, HTMLSession

csv_file = open("changemavie2.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow((['Episode_Number', 'Episode_Title', 'Link', 'Episode_Summary']))


session = HTMLSession()
response = session.get('https://changemavie.com/episodes-2')

contents = response.html.find('.summary-content')

for summary in contents:
    headline = summary.find('.summary-title-link', first=True).text
    episode_number = headline[1:4]
    episode_title = headline[6:]

    link = summary.find('.summary-title-link', first=True).attrs['href']
    link = f'https://changemavie.com{link}'

    episode_summary = summary.find('.summary-excerpt', first=True).text

    csv_writer.writerow([episode_number, episode_title, link, episode_summary])

csv_file.close()





