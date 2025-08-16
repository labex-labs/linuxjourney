# Setuid

## Lesson Content

There are many cases in which normal users need elevated access to do stuff. The system administrator can't always be there to enter a root password every time a user needs access to a protected file, so there are special file permission bits to allow this behavior. The Set User ID (SUID) allows a user to run a program as the owner of the program file rather than as themselves.

Let's look at an example:

Let's say I want to change my password, simple right? I just use the `passwd` command:

```bash
passwd
```

What is the `passwd` command doing? It's modifying a couple of files, but most importantly it's modifying the `/etc/shadow` file. Let's look at that file for a second:

```bash
$ ls -l /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Oh wait a minute here, this file is owned by root? How is it possible that we are able to modify a file owned by root?

Let's look at another permission set, this time of the command we ran:

```bash
$ ls -l /usr/bin/passwd

-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
```

You'll notice a new permission bit here **s**. This permission bit is the SUID. When a file has this permission set, it allows the users who launched the program to get the file owner's permission as well as execution permission, in this case root. So essentially, while a user is running the `passwd` command, they are running as root.

That's why we are able to access a protected file like `/etc/shadow` when we run the `passwd` command. Now if you removed that bit, you would see that you will not be able to modify `/etc/shadow` and therefore change your password.

### Modifying SUID

Just like regular permissions, there are two ways to modify SUID permissions.

_Symbolic way:_

```bash
sudo chmod u+s myfile
```

_Numerical way:_

```bash
sudo chmod 4755 myfile
```

As you can see, the SUID is denoted by a 4 and prepended to the permission set. You may see the SUID denoted as a capital **S**. This means that it still does the same thing, but it does not have execute permissions.

## Exercise

Look at the permissions for `/etc/passwd` in detail. Do you notice anything else? Files with SUID enabled are also easily distinguishable.

## Quiz Question

What number represents the SUID?

## Quiz Answer

4
