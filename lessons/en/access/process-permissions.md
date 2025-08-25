---
index: 7
lang: "en"
title: "Process Permissions"
meta_title: "Process Permissions - Permissions"
meta_description: "Learn about Linux process permissions, including Real, Effective, and Saved User IDs. Understand how UIDs impact security and command execution. Start learning today!"
meta_keywords: "Linux process permissions, Real UID, Effective UID, Saved UID, Linux security, passwd command, Linux tutorial, beginner Linux"
---

## Lesson Content

Let's segue into process permissions for a bit. Remember how I told you that when you run the `passwd` command with the SUID permission bit enabled, you will run the program as root? That is true. However, does that mean since you are temporarily root, you can modify other users' passwords? Nope, fortunately not!

This is because of the many UIDs that Linux implements. There are three UIDs associated with every process:

When you launch a process, it runs with the same permissions as the user or group that ran it. This is known as an **effective user ID**. This UID is used to grant access rights to a process. So, naturally, if Bob ran the `touch` command, the process would run as him, and any files he created would be under his ownership.

There is another UID, called the **real user ID**. This is the ID of the user that launched the process. These are used to track down who the user who launched the process is.

One last UID is the **saved user ID**. This allows a process to switch between the effective UID and real UID, and vice versa. This is useful because we don't want our process to run with elevated privileges all the time; it's just good practice to use special privileges at specific times.

Now let's piece these all together by looking at the `passwd` command once more.

When running the `passwd` command, your effective UID is your user ID; let's say it's 500 for now. Oh, but wait, remember the `passwd` command has the SUID permission enabled. So when you run it, your effective UID is now 0 (0 is the UID of root). Now this program can access files as root.

Let's say you get a little taste of power, and you want to modify Sally's password. Sally has a UID of 600. Well, you'll be out of luck. Fortunately, the process also has your real UID, in this case 500. It knows that your UID is 500, and therefore you can't modify the password of UID 600. (This, of course, is always bypassed if you are a superuser on a machine and can control and change everything).

Since you ran `passwd`, it will start the process off using your real UID, and it will save the UID of the owner of the file (effective UID), so you can switch between the two. No need to modify all files with root access if it's not required.

Most of the time, the real UID and the effective UID are the same, but in such cases as the `passwd` command, they will change.

## Exercise

Practice makes perfect! Understanding user IDs and process permissions is crucial for Linux security and administration. Here are some hands-on labs to reinforce your understanding of user and group management, which forms the basis of how UIDs function:

1. **[Linux User Group and File Permissions](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002)** - Learn essential Linux user and group management concepts, including creating and managing users, exploring group memberships, understanding file permissions, and manipulating file ownership. This lab provides practical experience in securing a multi-user Linux environment.
2. **[Add New User and Group](https://labex.io/labs/linux-add-new-user-and-group-17987)** - In this challenge, you'll simulate adding new team members to a server environment by creating new user accounts, setting up custom groups, and managing group memberships. This will test your skills in Linux user and group administration, essential for system administrators and DevOps professionals.

These labs will help you apply the concepts of user and group management in real scenarios, building a strong foundation for understanding how UIDs control access and permissions in Linux.

## Quiz Question

What UID decides what access to grant?

## Quiz Answer

effective
