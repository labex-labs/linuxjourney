# Process Threads

## Lesson Content

You may have heard of the terms single-threaded and multi-threaded processes. Threads are very similar to processes, in that they are used to execute the same program, they are often referred to as lightweight processes. If a process has one thread it is single-threaded and if a process has more than one thread it is multi-threaded. However, all processes have at least one thread. 

Processes operate with their own isolated system resources, however threads can share these resources among each other easily, making it easier for them to communicate among each other and at times it is more efficient to have a multi-threaded application than a multi-process application.

Basically, let's say you open up LibreOffice Writer and Chrome, each is it's own separate process. Now you go inside Writer and start editing text, when you edit the text it gets automatically saved. These two parallel "lightweight processes" of saving and editing are threads. 

To view process threads, you can use: 

<pre>
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
</pre>

The processes are denoted with each PID and underneath the processes are their threads (denoted by a --). So you can see that the processes above are both single-threaded.

## Exercise

Run the <b>ps m</b> command and see what processes you have running are multi-threaded.

## Quiz Question

True or false, all processes start out single-threaded.

## Quiz Answer

True
