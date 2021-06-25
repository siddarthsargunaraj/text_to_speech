import text_to_speech as speech
from datetime import datetime
import calendar

def main():
    months = {
    'Jan' : 0,
    'Feb' : 31,
    'Mar' : 59,
    'Apr' : 90,
    'May' : 120,
    'Jun' : 151,
    'Jul' : 181,
    'Aug' : 212,
    'Sep' : 243,
    'Oct' : 273,
    'Nov' : 304,
    'Dec' : 334
    }

    month = calendar.month_abbr[datetime.now().month]
    date = datetime.now().day
    result = months[month] + date
    with open('quoteOfTheDay.txt') as f:
        lines = f.readlines()
    speech.speak(lines[result], "en")

if __name__ == '__main__':
    main()