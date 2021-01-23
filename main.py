import gspread
from twitter import *
import json

# set credentials
gc = gspread.service_account('credentials.json')

data = json.load(open("twit_credentials.json"))

twit = Twitter(auth=OAuth(consumer_key=data["consumer_key"],
                  consumer_secret=data["consumer_secret"],
                  token=data["access_token_key"],
                  token_secret=data["access_token_secret"]))

# Open a sheet and create variables
wks = gc.open("Movies").sheet1
headers = wks.row_values('A')

# get movies
movies = []
val = 'No'

for r in range(2, wks.row_count - 1):
    row = wks.row_values(r)
    if row:
        if wks.acell(f"D{r}").value.capitalize() == val:
            movies.append(row)
            wks.update(f"D{r}", 'Yes')
    else:
        break

for i in range(len(movies)):
    tweet = f'{movies[i][0].title()} - {movies[i][2]} - {headers[1]}: {movies[i][1]}'
    twit.statuses.update(
        status = tweet
    )
    print(tweet)
