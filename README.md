# simple-twitter-bot-and-google
It's a twitter bot that connects to google sheets to poll recently watched movies and tweets about them

Credentials for both the Google service account and the Twitter service account are stored in seperate credential files not show in the repo

The script checks a google sheet for new movies. The google sheet is my personal watched list so it's dependent on me completing new films. If new movies are found, it updates the sheet and then tweets it.

Through the use of Cloud functions and the Cloud scheduler, the bot checks for new movies every 24 hours so please check out the result:

[Movie Bot](https://twitter.com/absolutism1123)

This was made in a series of examples used for educational purposes.
