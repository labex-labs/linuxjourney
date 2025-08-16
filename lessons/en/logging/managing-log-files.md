# Managing Log Files

## Lesson Content

Log files generate lots of data and they store this data on your hard disks, however there are lots of issues with this, for the most part we just want to be able to see newer logs, we also want to manage our disk space efficiently, so how do we do all of this? The answer is with logrotate.

The logrotate utility does log management for us. It has a configuration file that allows us to specify how many and what logs to keep, how to compress our logs to save space and more. The logrotate tool is usually run out of cron once a day and the configuration files can be found in /etc/logrotate.d.

There are other logrotating tools you can use to manage your logs, but logrotate is the most common one.

## Exercise

Look at your logrotate configuration file and see how it manages some of your logs.

## Quiz Question

What utility is used to manage logs?

## Quiz Answer

logrotate
