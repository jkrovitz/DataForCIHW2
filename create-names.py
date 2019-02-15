#!/usr/bin/python3

import csv
import gzip
from urllib.request import urlopen

def create_names(category):
    print("creating: "+ category)
    url = 'http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/meta_' + category + '.json.gz'
    with urlopen(url) as url_file, open(category + '.csv', 'w', newline='') as csvfile:
        csvw = csv.writer(csvfile)
        csvw.writerow(['id', 'title'])
        for line in gzip.open(url_file, 'r'):
            record = eval(line)
            csvw.writerow([record.get('asin'), record.get('title')])


if __name__ == '__main__':
    create_names('Amazon_Instant_Video')
    create_names('Musical_Instruments')
    create_names('Digital_Music')
    create_names('Baby')
    create_names('Patio_Lawn_and_Garden')
    create_names('Grocery_and_Gourmet_Food')
    create_names('Automotive')
    create_names('Pet_Supplies')
    create_names('Office_Products')
    create_names('Apps_for_Android')
    create_names('Beauty')
    create_names('Tools_and_Home_Improvement')
    create_names('Video_Games')
    create_names('Toys_and_Games')
    create_names('Health_and_Personal_Care')
    create_names('Cell_Phones_and_Accessories')
    create_names('Sports_and_Outdoors')
    create_names('Kindle_Store')
    create_names('Home_and_Kitchen')
    create_names('Clothing_Shoes_and_Jewelry')
    create_names('CDs_and_Vinyl')
    create_names('Movies_and_TV')
    create_names('Electronics')
    create_names('Books')
