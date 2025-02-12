# Process Permissions

## Lesson Content

Let's segway into process permissions for a bit, remember how I told you that when you run the passwd command with the SUID permission bit enabled you will run the program as root? That is true, however does that mean since you are temporarily root you can modify other user's passwords? Nope fortunately not!

This is because of the many UIDs that Linux implements. There are three UIDS associated with every process:

When you launch a process, it runs with the same permissions as the user or group that ran it, this is known as an <b>effective user ID</b>. This UID is used to grant access rights to a process. So naturally if Bob ran the touch command, the process would run as him and any files he created would be under his ownership.

There is another UID, called the <b>real user ID</b> this is the ID of the user that launched the process. These are used to track down who the user who launched the process is.

One last UID is the <b>saved user ID</b>, this allows a process to switch between the effective UID and real UID, vice versa. This is useful because we don't want our process to run with elevated privileges all the time, it's just good practice to use special privileges at specific times. 

Now let's piece these all together by looking at the passwd command once more. 

When running the passwd command, your effective UID is your user ID, let's say its 500 for now. Oh but wait, remember the passwd command has the SUID permission enabled. So when you run it, your effective UID is now 0 (0 is the UID of root). Now this program can access files as root.

Let's say you get a little taste of power and you want to modify Sally's password, Sally has a UID of 600. Well you'll be out of luck, fortunately the process also has your real UID in this case 500. It knows that your UID is 500 and therefore you can't modify the password of UID of 600. (This of course is always bypassed if you are a superuser on a machine and can control and change everything).

Since you ran passwd, it will start the process off using your real UID, and it will save the UID of the owner of the file (effective UID), so you can switch between the two. No need to modify all files with root access if it's not required. 

Most of the time the real UID and the effective UID are the same, but in such cases as the passwd command they will change.

## Exercise

We haven't discussed processes yet, we can still take a look at this change happening in real time: 

<ol>
<li>Open one terminal window, and run the command: <b>watch -n 1 "ps aux | grep passwd"</b>. This will watch for the passwd process.</li>
<li>Open a second terminal window and run: <b>passwd</b></li>
<li>Look at the first terminal window, you'll see a process come up for passwd. The first column in the process table is the effective user ID, lo and behold it's the root user!</li>
</ol>

## Quiz Question

What UID decides what access to grant?

## Quiz Answer

effective
