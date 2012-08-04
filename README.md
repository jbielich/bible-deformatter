# Summary

If you are doing an inductive Bible study in a book, or using a method like in *[How to Read the Bible for All Its Worth](http://amzn.com/0310246040)* by Gordon D. Fee, the #1 thing you need is a copy of the Bible text without verse numbers, paragraph breaks, etc.

Copy and pasting can be very cumbersome. This script will scrape a book from <http://www.biblegateway.com> and strip out all the extras and output it to a **book.txt** file. It is not 100% perfect, but it does the job with minimal post-processing.


# Prerequisites

You need to install BeautifulSoup:

    sudo pip install BeautifulSoup


# Usage

Run the script, and type in the name of the book you want to download (make sure it's spelled correctly):

    ./getBibleBook.py
    Type in book to download:Jude

The bigger the book, the longer it takes. Be patient. ;)
