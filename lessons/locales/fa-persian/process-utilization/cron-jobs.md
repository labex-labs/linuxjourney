# Cron Jobs

## Lesson Content

Although we have been talking about resource utilization, I think this would be a good point to mention a neat tool in Linux that is used to schedule tasks using cron. There is a service that runs programs for you at whatever time you schedule. This is a really useful if you have a script you want to run once a day that needs to execute something for you. 

For example, let's say I have a script located in /home/pete/scripts/change_wallpaper. I use this script every morning to change the picture I use for my wallpaper, but each morning I have to manually execute this script. Instead what I can do is create a cron job that executes my script through cron. I can specify the time I want this cron job to run and execute my script. 

<pre>30 08 * * * /home/pete/scripts/change_wallpaper</pre>

The fields are as follows from left to right:
<ul>
<li>Minute - (0-59)</li>
<li>Hour - (0-23)</li>
<li>Day of the month - (1-31)</li>
<li>Month - (1-12)</li>
<li>Day of the week - (0-7). 0 and 7 are denoted as Sunday</li>
</ul>

The asterisk in the field means to match every value. So in my above example, I want this to run every day in every month at 8:30am.

To create a cronjob, just edit the crontab file:

<pre>crontab -e</pre>

## Exercise

Create a cronjob that you want to run at a scheduled time.

## Quiz Question

What is the command to edit your cronjobs?

## Quiz Answer

crontab -e