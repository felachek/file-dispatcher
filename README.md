# File dispatcher for download directory
It provides the functionality to move the file from one location to another based on file type.

## Run cron job
Crontab is needed for scheduling python scripts on Linux
``` bash
# Install on Debian
sudo apt-get install cron

# Start the cron schedule
systemctl enable crond
```

## Editing the cron schedule
Run `crontab -e` in your terminal.
To run a task you need to run this command
``` bash
schedule python_version file_script > /tmp/cron.log 2>&1
```
### Example
``` bash
0 1 * * * /usr/bin/python3 '/home/user/index.py' > /tmp/cron.log 2>&1
```
Here is the link for creating a cron schedule expression [crontab.guru](https://crontab.guru/)