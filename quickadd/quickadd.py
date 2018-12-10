import requests
import json
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.events'

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    calendar = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Write.as API to fetch the post
    headers = {'Content-Type': 'application/json'}
    url = 'https://write.as/api/posts/' + raw_input("Give post id here: ")
    post = requests.get(url, headers=headers)
    post_body = post.json()['data']['body']

    # Call the Google Calendar API and feed in the post body
    create_event = calendar.events().quickAdd(calendarId='primary',text=post_body).execute()
    print('Success? Check your calendar to see: https://calendar.google.com/calendar/r')

if __name__ == '__main__':
    main()
