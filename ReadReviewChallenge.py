import csv
import datetime
import os
import ffn_scraping

##f = open("ffn_stats.csv", "rwb")
##reader = csv.reader(f)
##writer = csv.writer(f)
##if not os.path.isfile("ffn_stats.csv"):
##    writer.writerow(['title', 'author', 'chapters', 'words', 'reviews', 'favorites', 'follows', 'publish date', 'update date', 'link', 'discord ID', 'opt-in', 'reserved', 'reserved', ])
##
link = 'https://www.fanfiction.net/s/4298303/1/'
stats = ffn_scraping.scrape(link)['1']
error = ffn_scraping.scrape(link)['2']
print(stats)

##def rand(exclude):
##    r = None
##    while r in exclude or r is None:
##         r = random.randrange(1,10)
##    return r
