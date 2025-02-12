# Controlling Terminal

## Lesson Content

We discussed how there is a TTY field in the ps output. The TTY is the terminal that executed the command.

There are two types of terminals, regular <b>terminal devices</b> and <b>pseudoterminal devices</b>. A regular terminal device is a native terminal device that you can type into and send output to your system, this sounds like the terminal application you've been launching to get to your shell, but it's not. 

We're gonna segue so you can see this action, go ahead and type Ctrl-Alt-F1 to get into TTY1 (the first virtual console), you'll notice how you don't have anything except the terminal, no graphics, etc. This is considered a regular terminal device, you can exit this with Ctrl-Alt-F7. 

A pseudoterminal is what you've been used to working in, they emulate terminals with the shell terminal window and are denoted by PTS . If you look at ps again, you'll see your shell process under pts/*.

Ok, now circling back to the controlling terminal, processes are usually bound to a controlling terminal. For example, if you were running a program on your shell window such as find and you closed the window, your process would also go with it. 

There are processes such as daemon processes, which are special processes that are essentially keeping the system running. They often start at system boot and usually get terminated when the system is shutdown. They run in the background and since we don't want these special processes to get terminated they are not bound to a controlling terminal. In the ps output, the TTY is listed as a <b>?</b> meaning it does not have a controlling terminal.

## Exercise

Look at your ps output and list all the unique TTY values.

## Quiz Question

What value is given for a process that does not have a controlling terminal?

## Quiz Answer

?