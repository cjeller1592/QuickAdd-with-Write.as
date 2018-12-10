import requests
import json

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# These scopes allow us to add events to our calendar
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.events'

def quickadd():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()

    # Make sure to register your app in the Google developer's console
    # By doing so you will retrieve your 'credentials.json' file needed to authorize your request
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    calendar = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Write.as API to fetch the post
    # When you run the script in the cmd line, it will ask you for the post id
    headers = {'Content-Type': 'application/json'}
    url = 'https://write.as/api/posts/' + raw_input("Give post id here: ")
    
    # Now with the necessary parts of the request we will call the Write.as API
    post = requests.get(url, headers=headers)
    
    # Once the request is complete, we'll grab the post body
    post_body = post.json()['data']['body']

    # Call the Google Calendar API and feed in the post body
    create_event = calendar.events().quickAdd(calendarId='primary',text=post_body).execute()
    print('Success? Check your calendar to see: https://calendar.google.com/calendar/r')

if __name__ == '__main__':
    main()
