from datetime import date
from datetime import datetime
from datetime import timedelta
import urllib.request
from bs4 import BeautifulSoup

SCHEDULE_URL = "http://www.bbc.co.uk/schedules/p00fzl7j"

def getSpoiler( pDate, pURL ):

    try:
        with urllib.request.urlopen( pURL) as f:
            txt_content = f.read().decode('utf-8')
    except urllib.error.HTTPError:
        return ""

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
    spoiler = getSpoiler( day, dateURL )

    if spoiler.startswith("Contemporary drama in a rural setting") == True:
        break
    elif spoiler != "":
        print( "%s: %s" % (day.strftime("%a %d/%m/%Y"), spoiler ))

input("Press a key to exit.")
