import csv
import re
from re import search

from googlesearch import search
with open("C:\\Users\\CHRISTY BIJU\\Downloads\\Company.lst","r+") as f:
    for line in f:
        line = line.strip()
        query = line
        print(query)
        for j in search(query, tld="co.in", num=30, stop=30, pause=2):
          if (re.search('linkedin', j)):
            print(j)
            row = [query,j]
            f = open('Company_links1.csv', 'a', newline='')
            writer = csv.writer(f)
            writer.writerow(row)
            continue
          # close the file
        f.close()