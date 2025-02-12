# System Logging

## Lesson Content

The services, kernel, daemons, etc on your system are constantly doing something, this data is actually sent to be saved on your system in the form of logs. This allows us to have a human readable journal of the events that are happening on our system. This data is usually kept in the /var directory, the /var directory is where we keep our variable data, such as logs!

How are these messages even getting received on your system? There is a service called syslog that sends this information to the system logger. 

Syslog actually contains many components, one of the important ones is a daemon running called syslogd (newer Linux distributions use rsyslogd), that waits for event messages to occur and filter the ones it wants to know about, and depending on what it's supposed to do with that message, it will send it to a file, your console or do nothing with it.

You would think that this system logger is the centralized place to manage logs, but unfortunately it's not. You'll see many applications that write their own logging rules and generate different log files, however in general the format of logs should include a timestamp and the event details. 

Here is an example of a line from syslog:

<pre>
pete@icebox:~$ less /var/log/syslog
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
</pre>

Here we can see that at Jan 27 07:41:32 our cron service ran the cron.weekly job. You can view all the event messages that syslog collects with in the /var/log/syslog file.

## Exercise

Look at your /var/log/syslog file and see what else is happening on your machine.

## Quiz Question

What is the daemon that manages log on newer Linux systems?

## Quiz Answer

rsyslogd
