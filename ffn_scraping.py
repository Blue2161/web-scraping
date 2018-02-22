from bs4 import BeautifulSoup
import lxml
import requests
import csv

site = 'https://www.fanfiction.net/s/4298303/1/'

##csv_file = open('story_stats.csv', 'w')
##csv_writer = csv.writer(csv_file)
##csv_writer.writerow(['title', 'author', 'chapters', 'words', 'reviews', 'favorites', 'follows', 'publish date', 'update date', 'link'])
##csv_file.close()

#ensure the address given is the correct version
if 'https://' not in site:
    site = 'https://' + site
if "m." in site:
    site = site.replace('m.', 'www.')

#obtain a copy of the html for parsing
source = requests.get(site).text
soup = BeautifulSoup(source, 'lxml')

#define an array to hold exportable values
csv_stats = list(range(0,9))

#initialize stats in case of missing info
for i in range(len(csv_stats)):
    csv_stats[i] = None
csv_stats[2] = 1

#find the desired information and divide it into a clean list
csv_stats[0] = soup.find('b', class_ = 'xcontrast_txt').text
print('Title: {}'.format(csv_stats[0]))

csv_stats[1] = soup.find_all('a', class_ = 'xcontrast_txt')[2].text
print('Author: {}'.format(csv_stats[1]))

stats = soup.find(class_="xgray xcontrast_txt")
stats = stats.text.replace('-', '').replace(',','').split()
print(stats)
for i in range(len(stats)):
    if 'Chapters:' in stats[i]:
        csv_stats[2] = stats[i+1]
    elif 'Words:' in stats[i]:
        csv_stats[3] = stats[i+1]
    elif 'Reviews:' in stats[i]:
        csv_stats[4] = stats[i+1]     
    elif 'Favs:' in stats[i]:
        csv_stats[5] = stats[i+1]
    elif 'Follows:' in stats[i]:
        csv_stats[6] = stats[i+1]
    elif 'Published:' in stats[i]:
        csv_stats[7] = stats[i+1]
    elif 'Updated:' in stats[i]:
        csv_stats[8] = stats[i+1]
print('Chapters: {}'.format(csv_stats[2]))
print('Words: {}'.format(csv_stats[3]))
print('Reviews: {}'.format(csv_stats[4]))
print('Favs: {}'.format(csv_stats[5]))
print('Follows: {}'.format(csv_stats[6]))
print('Published: {}'.format(csv_stats[7]))
print('Updated: {}'.format(csv_stats[8]))

