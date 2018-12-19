import requests
import pprint
import time


pp = pprint.PrettyPrinter(indent=4)
# https://api.nasa.gov/api.html#apod
# This is a parameter
def func(data):
    api_key = "redW7aYXfCw0fXFF8vW9EcAkJzSr6d9GIV9DWEe7"


# We are doing a get request
#data = "2017-06-13"
    r = requests.get(f'https://api.nasa.gov/planetary/apod?date={data}&api_key={api_key}')
    print(r.status_code)
    pp.pprint(r.json())
    url = r.json()["url"]
    from IPython.display import Image, clear_output
    clear_output()
    display(Image(url = url))


list_date = ["2015-06-16", "2012-12-12", "2006-06-16", "1997-09-19", "1996-06-28"]
i = 0
while i < len(list_date):
    time.sleep(3)
    func(list_date[i])
    i += 1
