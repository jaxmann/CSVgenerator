import csv
import random
import datetime
from datetime import datetime
from datetime import timedelta
from random import randint
import sys

# args are 0: numLines, 1: output file

website_arr = [
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://www.somebank.com/',
    'http://01hw621078:8080',
    'http://localhost:8090',
    'http://localhost:8080'
]

page_arr = [
    'Bank Accounts',
    'Bank Accounts',
    'Credit Cards',
    'Credit Cards',
    'Home',
    'Loans',
    'NRI Services',
    'Special Offers and Discounts',
    'Home',
    'Loans',
    'NRI Services',
    'Special Offers and Discounts',
    'null'
]

page_access_arr = [
    'Clickthrough',
    'Exit',
]

referrer_arr = [
    'Yahoo',
    'Facebook',
    'Google Search',
    'Bank Website URL',
    'Google Ads',
    'Bing Search',
    'Credit Cards',
    'Home',
    'Bank Accounts',
    'Special Offers and Discounts',
    'Loans',
    'NRI Services',
    'null',
    'adsense',
    'google',
    'bing',
    'dlbank'
]

ip_address_arr = [
    '111.111.111.111',
    
   
    #'172.17.121.154', only for 01hw... url
    # '0:0:0:0:0:0:0:1' only for localhost
]

user_agent_string_browser_arr = [
    'IE',
    'Mozilla',
    'Chrome',
    'Opera',
    'Safari',
    'Edge',
    'Microsoft Internet Explorer'
]   

user_agent_string_operating_system_arr = [
    'Windows',
    'Mac OS X',
    'Android',
    'Windows Mobile',
    'iOS'
]

user_id_arr = [
    689516673,
    587130381,
    169645803,
    199311986,
    778710357,
    443565142,
    406109528,
    467668192,
    731164739,
    813879271,
    457557186,
    811980663,
    261943026,
    558972072,
    158179924,
    385401771,
    728109364,
    265192627,
    565210447,
    857959,
    111111,
    88888888,
    2847356,
    456123,
    789456,
    7894566,
    7894566,
    45612398,
    5678905
]
user_name_arr = [
    'Anthony James',
    'Arthur Hawkins',
    'Brian Morris',
    'Carolyn Bell',
    'David George',
    'Harry Frazier',
    'Jason Long',
    'Jonathan Stone',
    'Jose Berry',
    'Judith Montgomery',
    'Kevin Sanders',
    'Larry Coleman',
    'Laura Coleman',
    'Louis Williams',
    'Robin Austin',
    'Sara Mills',
    'Steve Hart',
    'Wayne Burton',
    'William Grant',
    'Lakshmi Shankwalker',
    'Oprah Winfrey',
    'Vivian Richards',
    'Siddhant',
    'Jack Ronson',
    'Meryl Streep',
    'Ted Baker',
    'Melissa Jones',
    'Henry James',
    'James Brown'
]

city_arr = [ #state
    'North Carolina',
    'Texas',
    'North Dakota',
    'Iowa',
    'Ohio',
    'Connecticut',
    'New York',
    'California',
    'Colorado',
    'Florida',
    'Tennessee',
    'Minnesota',
    'South Carolina',
    'Indiana',
    'Utah',
    'Maryland',
    'Michigan',
    'Illinois',
    'Missouri',
    'Kansas',
    'Mississippi',
    'Louisiana',
    'Georgia',
    'District of Columbia',
    'West Virginia',
    'Idaho',
    'New Jersey',
    'Hawaii',
    'New Mexico',
    'Alabama',
    'Oklahoma',
    'Pennsylvania',
    'Arkansas',
    'Maine',
    'Massachusetts',
    'Oregon',
    'Washington',
    'Nevada',
    'Virginia',
    'Arizona',
    'Kentucky',
    'New Hampshire',
    'Delaware',
    'Wisconsin',
    'Montana',
    'Wyoming',
    'Nebraska',
    'South Dakota',
    'Alaska',
    'Rhode Island',
]


if (len(sys.argv) < 3): print 'invalid num of arguments: arg1: num lines, arg2; output file'

# yyyy/mm/dd
start_date= datetime(2016,01,06) #lower limit for random datetime
end_date= datetime(2016,03,02) #upper limit for random datetime

def random_date(start, end):
    return start + timedelta(seconds=randint(0, int((end - start).total_seconds())))

g=open(sys.argv[2],"w")
w=csv.writer(g, lineterminator='\n')
w.writerow(('website','page','page_access_type','referrer','year','month_of_year', 'day_of_month','hour_of_day','minute_of_hour','second_of_minute','ip_address','user_agent_string_browser','user_agent_string_operating_system',
'user_id','user_name','duration_of_page_visit','timestamp', 'city', 'txn_flag','txn_amount'))
for i in xrange(int(sys.argv[1])):

    randUser = random.randrange(0,29,1)

    ##### build fields
    website = random.choice(website_arr)
    if (website == "http://www.somebank.com/"): ip_address = random.choice(ip_address_arr)
    elif (website == "http://abc:8080"): ip_address = "222.222.222.222"
    else: ip_address = "0:0:0:0:0:0:0:1"

    page = random.choice(page_arr)
    if (page == "Bank Accounts"): page_access_type = random.choice(["Clickthrough", "Exit", "Entry"])
    elif (page == "null"): page_access_type = "null"
    else: page_access_type = random.choice(page_access_arr)

    referrer = random.choice(referrer_arr)
    year = "2016" #always 2016
    randDate = random_date(start_date, end_date) #generate a random date
    month_of_year = randDate.month
    day_of_month = randDate.day
    hour_of_day = random.randrange(0,24,1)
    minute_of_hour = random.randrange(0,60,1)
    second_of_minute = random.randrange(0,60,1)
    user_agent_string_operating_system = random.choice(user_agent_string_operating_system_arr)

    if (user_agent_string_operating_system == "Windows"): user_agent_string_browser = random.choice(["IE","Mozilla","Chrome","Opera","Edge","Microsoft Internet Explorer"])
    elif (user_agent_string_operating_system == "Mac OS X"): user_agent_string_browser = random.choice(["Chrome","Safari","Opera"])
    elif (user_agent_string_operating_system == "Android"): user_agent_string_browser = random.choice(["Chrome"])
    elif (user_agent_string_operating_system == "Windows Mobile"): user_agent_string_browser = random.choice(["IE"])
    elif (user_agent_string_operating_system == "iOS"): user_agent_string_browser = random.choice(["Opera","Safari"])

    user_id = user_id_arr[randUser]
    user_name = user_name_arr[randUser]
    duration_of_page_visit = random.randrange(0,300,1)
    timestamp = str(day_of_month) + "/" + str(month_of_year) + "/" + str(year) + " " + str(hour_of_day).zfill(2) + ":" + str(minute_of_hour).zfill(2) #csv has european format...
    city = random.choice(city_arr) #state
    txn_flag = random.choice(["Y","N"])
    txn_amount = round(random.uniform(1.0, 99.9), 6) if txn_flag == "Y" else 0

    w.writerow((
        website,
        page,
        page_access_type,
        referrer,
        year,
        month_of_year,
        day_of_month,
        hour_of_day,
        minute_of_hour,
        second_of_minute,
        ip_address,
        user_agent_string_browser,
        user_agent_string_operating_system,
        user_id,
        user_name,
        duration_of_page_visit,
        timestamp,
        city, #state
        txn_flag,
        txn_amount
    ))

   