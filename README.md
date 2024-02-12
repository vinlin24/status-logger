# Discord Custom Status Logger

## Description

It's become a habit of mine to update my Discord custom status with something witty or silly for the day. When it expires at midnight, I write something new, usually whatever happened to be on my mind at that time. I figured it would be nice to record these custom statuses in some kind of history log so I can look back on what my mind was up to on a certain day.

> [!WARNING]
>
> **UPDATE:** This repository has been *deprecated* as the status logging
> functionality has been merged into my
> [counters](https://github.com/vinlin24/counters) project.

## Implementation

This project uses [Python Selenium](https://pypi.org/project/selenium/) to headlessly navigate the Discord web application and extract the custom status, both emoji and text, of my logged in user. The emoji and text are then appended along with a timestamp to a CSV file on my local machine. The header of the CSV file is:

```csv
Date,Time,Emoji,Text
```

I hooked this program up to the [Windows Task Scheduler](#task-scheduler-setup) on my local machine to run daily just before midnight at 11:00 PM to save what my status happens to be at that time, which is assumed to be what my status was for that day.

If the program raises an Exception at any point, such as in the webscraping part due to outdated XPaths, it will log it and the traceback to a local `status-logger.log` file as well as send it as an email to myself.

## Task Scheduler Setup

### General

- Security options
  - Run whether user is logged on or not

### Triggers

- New...
  - Begin the task: On a schedule
  - Settings
    - Daily
    - Start: 9/9/2022 11:00:00 PM
    - Synchronize across time zones
    - Recur every: 1 days
  - Advanced settings
    - Enabled

### Actions

- New...
  - Action: Start a program
  - Program/script: path\to\this\repo\\.venv\Scripts\python.exe
  - Add arguments: -m package
  - Start in: path\to\this\repo

### Conditions

- Power
  - Wake the computer to run this task
- Network
  - Start only if the following network connection is available: Any connection

### Settings

- Allow task to be run on demand
- If the task fails, restart Every: 15 minutes, Attempt to restart up to: 3 times
- Stop the task if it runs longer than: 1 hour
- If the running task does not end when requested, force it to stop
- If the task is already running, then the following rule applies: Stop the existing instance

## Development

### Environment Recovery

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

### Limitations

The program is designed to be run by an external scheduler, like the Windows Task Scheduler, so if some condition stops the task from running, then the history will miss a day. I might add more features or countermeasures to combat this. At the moment, I use some [options provided by the Task Scheduler itself](#task-scheduler-setup) to reduce this risk.

### What Next

At the moment, this program is only concerned with saving history. In the future, maybe I'll want to parse/filter the CSV file for some other purpose. I might also make this program distributable as a learning exercise but also so others can take part in this silly habit. I imagine that distribution would entail:

- Making the package itself more configurable by supporting different browsers, customizing history file location, etc.
- Using [setuptools](https://github.com/pypa/setuptools) or the like to automatically install the package for the end user.
- Writing a helper script to hook up the installed package to the Windows Task scheduler using [PowerShell](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/?view=windowsserver2022-ps).
