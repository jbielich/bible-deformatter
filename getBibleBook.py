#!/usr/bin/python

import urllib
import urllib2
import sys
import re
from BeautifulSoup import BeautifulSoup, Comment

chapters = { "Genesis" : 50, "Exodus" : 40, "Leviticus" : 27, "Numbers" : 36, "Deuteronomy" : 34, \
"Joshua" : 24, "Judges" : 21, "Ruth" : 4, "1 Samuel" : 31, "2 Samuel" : 24, \
"1 Kings" : 22, "2 Kings" : 25, "1 Chronicles" : 29, "2 Chronicles" : 36, "Ezra" : 10, \
"Nehemiah" : 13, "Esther" : 10, "Job" : 42, "Psalms" : 150, "Proverbs" : 31, \
"Ecclesiastes" : 12, "Song of Songs" : 8, "Song of Solomon" : 8, "Isaiah" : 66, \
"Jeremiah" : 52, "Lamentations" : 5, "Ezekiel" : 48, "Daniel" : 12, "Hosea" : 14, \
"Joel" : 3, "Amos" : 9, "Obadiah" : 1, "Jonah" : 4, "Micah" : 7, "Nahum" : 3, \
"Habakkuk" : 3, "Zephaniah" : 3, "Haggai" : 2, "Zechariah" : 14, "Malachi" : 4, \
"Matthew" : 28, "Mark" : 16, "Luke" : 24, "John" : 21, "Acts" : 28, "Romans" : 16, \
"1 Corinthians" : 16, "2 Corinthians" : 13, "Galatians" : 6, "Ephesians" : 6, \
"Philippians" : 4, "Colossians" : 4, "1 Thessalonians" : 5, "2 Thessalonians" : 3, \
"1 Timothy" : 6, "2 Timothy" : 4, "Titus" : 3, "Philemon" : 1, "Hebrews" : 13, \
"James" : 5, "1 Peter" : 5, "2 Peter" : 3, "1 John" : 5, "2 John" : 1, "3 John" : 1, \
"Jude" : 1, "Revelation" : 22 }

c = raw_input("Type in book to download:")

if c not in chapters.keys():
    sys.exit("I don't recognize the book " + c + ". Please check your spelling")

book = ''

for i in range(chapters[c]):
    url = "http://www.biblegateway.com/passage/?search=" + urllib.quote_plus(c) + "+" + str(i + 1) + "&version=ESV"

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    soup = soup.find('div', "result-text-style-normal text-html ")

    subtree = soup.findAll("div")
    [div.extract() for div in subtree]

    subtree = soup.findAll("h4")
    [tmp.extract() for tmp in subtree]

    subtree = soup.findAll("h5")
    [tmp.extract() for tmp in subtree]

    sups = soup.findAll("sup")
    [sup.extract() for sup in sups] 

    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]

    passage = soup.findAll(text=True)
    passage = ''.join(passage)
    passage = passage.encode('ascii', 'ignore')

    p = re.compile('&nbsp;')
    passage = p.sub('',passage)

    p = re.compile(' +')
    passage = p.sub(' ', passage)

    p = re.compile('^ ')
    passage = p.sub('', passage)

    passage = passage.strip()

    book = book + " " + passage

f = open('book.txt', 'w')
f.write(book)
f.close()
