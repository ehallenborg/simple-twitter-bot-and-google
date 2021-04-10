import gspread
from twitter import *
import json
import time

def send_tweet(event, context):
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
    number = list(range(2, wks.row_count))
    batches = [number[x:x+10] for x in range(0, len(number), 10)]

    run_throughs = 0

    empty = False
    for batch in batches:
        for r in batch:
            row = wks.row_values(r)
            if row:
                if wks.acell(f"D{r}").value.capitalize() == val:
                    movies.append(row)
                    wks.update(f"D{r}", 'Yes')
            else:
                empty = True
                break
        if empty:
            break
        else:
            time.sleep(30)
            run_throughs += 1

        if run_throughs == 5:
            time.sleep(30)
            run_throughs = 0

    if movies:
        for i in range(len(movies)):
            tweet = f'{movies[i][0].title()} - {movies[i][2]} - {headers[1]}: {movies[i][1]} - Rating : {movies[i][4]}'
            twit.statuses.update(
                status = tweet
            )
            print(tweet)

    else:
        print("No new movies found")
