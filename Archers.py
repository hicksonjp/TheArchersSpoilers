#!/usr/bin/python3

# The Archers Spoilers
# ====================
#
#   By John Hickson
#
# Use the BBC R4 website to list upcoming Archers episodes 
#
# This software is written on Python 3. makes use of the 
# BeautifulSoup (v4.4.1), a Python library which is used to "scrape" 
# the one-line spoiler text from the BBC Radio 4 schedules website.  
# BeautifulSoup can be found here: 
# 
# https://www.crummy.com/software/BeautifulSoup/
#
# In the file Archers.py, the variable SCHEDULE_URL holds the URL for 
# the BBC radio 4 schedules.  The "random" charachers in the last part of 
# the URL may need updating from time to time.  The latest URL can found 
# by going to the website using a browser.
#

from datetime import date
from datetime import datetime
from datetime import timedelta
import urllib.request
import ssl

from bs4 import BeautifulSoup

SCHEDULE_URL = "https://www.bbc.co.uk/schedules/p00fzl7j"

def getSpoiler( pDate, pURL ):

    try:
        with urllib.request.urlopen( pURL, context=ssl._create_unverified_context()) as f:
            txt_content = f.read().decode('utf-8')
            #txt_content = f.read()
    except urllib.error.HTTPError:
        return ""
    except UnicodeDecodeError:
        # print( "UnicodeDecodeError with %s, %s" % (pDate, pURL ))
        return "UnicodeDecodeError with %s, %s" % (pDate, pURL )

    soup = BeautifulSoup( txt_content, 'html.parser')

    search_points = soup.find_all(string="The Archers")

    if len(search_points) > 0:

        prog_root    = search_points[-1].parent.parent.parent.parent.parent.parent.parent
        prog_spoiler = prog_root.p.span.text
        return prog_spoiler;

    else:
        return ""
    

date_list = [date.today() + timedelta(days=x) for x in range(0, 30)]

for day in date_list:

    dateURL = SCHEDULE_URL + "/%02d/%02d/%02d" % (day.year, day.month, day.day)
    spoiler = getSpoiler( day, dateURL ).replace(u"\u2019","'")

#    if spoiler.startswith("Contemporary drama in a rural setting") == True:
#        break
#    elif spoiler != "":
#        print( "%s: %s" % (day.strftime("%a %d/%m/%Y"), spoiler ))
    print( "%s: %s" % (day.strftime("%a %d/%m/%Y"), spoiler ))

input("Press a key to exit.")

