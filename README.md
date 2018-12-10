# QuickAdd-with-Write.as-
Create a Google Calendar Event from the cmd line using a Write.as post


This app is an extension of Google's Calendar API quickstart.py script that can be found <a href='https://github.com/gsuitedevs/python-samples/blob/master/calendar/quickstart/quickstart.py'> here</a>. 

Since I enjoy the Write.as text editor so much, I wanted to be able to quickly jot down an event from Write.as and add it to my Google calendar. This script is an attempt of such a feature.

<strong>Using the script</strong>

1) Before anything, register your app with Google. This is how you'll be able to get the 'client_secret.json' file needed to authorize your app and access your calendar.

2) Once registered, download the 'client_secret.json' file and replace it with the one in the directory. This is the file the app accesses to go through the oAuth2.0 process.

3) Then create a post through Write.as. No sign in required. Something like 'Walk the dog December 10th at 10:00am' will do.

4) Once published, you will see a link like this: https://write.as/jfdas332sdfffg. The end string is your post id. Copy this as you will need it for the script to work.

5) Run the script... 

```
quickadd $ python quickadd.py

```

6) Put in your post id...

```
Give post id here:

```

7) Check your Google calendar and see if it worked!

```
Success? Check your calendar to see: https://calendar.google.com/calendar/r

```
