# Discord Custom Status Logger

## Description

It's become a habit of mine to update my Discord custom status with something witty or silly for the day. When it expires at midnight, I write something new, usually whatever happened to be on my mind at that time. I figured it would be nice to record these custom statuses in some kind of history log so I can look back on what my mind was up to on a certain day.

## Implementation

This project uses [Python Selenium](https://pypi.org/project/selenium/) to headlessly navigate the Discord web application and extract the custom status, both emoji and text, of my logged in user. The emoji and text are then appended along with a timestamp to a CSV file on my local machine. The header of the CSV file is:

```csv
Date,Time,Emoji,Text
```

I hooked this program up to the Windows Task Scheduler on my local machine to run daily just before midnight at 11:55 PM to save what my status happens to be at that time, which is assumed to be what my status was for that day.

The scheduler action is set up as follows:

- Action: Start a program
- Program/script: `path\to\this\repo\.venv\Scripts\python.exe`
- Add arguments: `-m package`
- Start in: `path\to\this\repo`

And the task is configured to run only when a network connection is available.

## Environment Recovery

As usual, this project makes uses of environment variables set up in a `.env` file at the project root. The required key names are:

- `DISCORD_EMAIL`: Email address associated with my Discord account.
- `DISCORD_PASSWORD`: Password to my Discord account.
- `ERROR_EMAIL`: Email to send and receive error reports.
- `ERROR_EMAIL_PASSWORD`: Password to the email used to send and receive error reports.

As usual, the dependencies are tracked with [`requirements.txt`](requirements.txt):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## What Next

At the moment, this program is only concerned with saving history. In the future, maybe I'll want to parse/filter the CSV file for some other purpose. I might also make this program distributable as a learning exercise but also so others can take part in this silly habit. Also, the execution of this program relies entirely on the Windows Task Scheduler, so if my PC happens to be powered off at 11:55 PM or other conditions cause it to fail, then the history will miss a day. I might add more features or countermeasures to combat this.
