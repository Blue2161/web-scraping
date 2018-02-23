from bs4 import BeautifulSoup
import lxml
import requests
import aiohttp

def scrape(site):
    #site = 'https://www.fanfiction.net/s/4298303/1/'
    error = False

    #ensure the address given is the correct version for parsing
    if 'https://' not in site:
        site = 'https://' + site
    if "m." in site:
        site = site.replace('m.', 'www.')

    #obtain a copy of the html for parsing
    try:
        source = aiohttp.get(site).text
        soup = BeautifulSoup(source, 'lxml')
    except:
        print('connection error')
        error = True

    #define an array to hold exportable values
    csv_stats = list(range(0,10))

    #initialize stats in case of missing info
    for i in range(len(csv_stats)):
        csv_stats[i] = None
    csv_stats[2] = 1

    #find the desired information and divide it into a clean list
    csv_stats[0] = soup.find('b', class_ = 'xcontrast_txt').text
##    print('Title: {}'.format(csv_stats[0]))

    csv_stats[1] = soup.find_all('a', class_ = 'xcontrast_txt')[2].text
##    print('Author: {}'.format(csv_stats[1]))

    stats = soup.find(class_="xgray xcontrast_txt")
    stats = stats.text.replace('-', '').replace(',','').split()

    csv_stats[9] = site
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
            
##    print('Chapters: {}'.format(csv_stats[2]))
##    print('Words: {}'.format(csv_stats[3]))
##    print('Reviews: {}'.format(csv_stats[4]))
##    print('Favs: {}'.format(csv_stats[5]))
##    print('Follows: {}'.format(csv_stats[6]))
##    print('Published: {}'.format(csv_stats[7]))
##    print('Updated: {}'.format(csv_stats[8]))
##    print('Link: {}'.format(csv_stats[9]))

    return {'1': csv_stats, '2': error}
