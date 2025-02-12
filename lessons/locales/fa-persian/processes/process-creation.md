# Process Creation

## Lesson Content

Again this lesson and the next are purely information to let you see what's under the hood, feel free to circle back to this once you've worked with processes a bit more.

When a new process is created, an existing process basically clones itself using something called the fork system call (system calls will be discussed very far into the future). The fork system call creates a mostly identical child process, this child process takes on a new process ID (PID) and the original process becomes its parent process and has something called a parent process ID <b>PPID</b>. Afterwards, the child process can either continue to use the same program its parent was using before or more often use the execve system call to launch up a new program. This system call destroys the memory management that the kernel put into place for that process and sets up new ones for the new program. 

We can see this in action:

<pre>$ ps l</pre>

The l option gives us a "long format" or even more detailed view of our running processes. You'll see a column labelled <b>PPID</b>, this is the parent ID. Now look at your terminal, you'll see a process running that is your shell, so on my system I have a process running bash. Now remember when you ran the ps l command, you were running it from the process that was running bash. Now you'll see that the <b>PID</b> of the bash shell is the <b>PPID</b> of the <b>ps l</b> command.

So if every process has to have a parent and they are just forks of each other, there must be a mother of all processes right? You are correct, when the system boots up, the kernels creates a process called <b>init</b>, it has a PID of 1. The init process can't be terminated unless the system shuts down. It runs with root privileges and runs many processes that keep the system running. We will take a closer look at init in the system bootup course, for now just know it is the process that spawns all other processes.

## Exercise

Take a look at your running processes, can you see what other processes have parents?

## Quiz Question

What system call creates a new process?

## Quiz Answer

fork
