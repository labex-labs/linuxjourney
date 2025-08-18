---
index: 1
lang: "en"
title: "File Sharing Overview"
meta_title: "File Sharing Overview - Network Sharing"
meta_description: "Learn about Linux file sharing and secure copy (scp) command. Transfer files between hosts on your network. Get started with this beginner-friendly guide!"
meta_keywords: "Linux file sharing, scp command, secure copy, network file transfer, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

You are usually not the only computer on your network, especially if you're working in a commercial environment. When we want to transfer data from one machine to another, sometimes it may be easier to connect a USB drive and manually copy them. But for the most part, if you're working with machines on the same network, the way to transfer data is through network file sharing.

In this course, we'll go over a couple of different methods to copy data to and from different machines on your network. We'll discuss some simple file copies, then we'll talk about mounting entire directories on your machine that act as a separate drive.

One simple file sharing tool is the **scp** command. The scp command stands for secure copy; it works exactly the way the cp command does, but allows you to copy from one host over to another host on the same network. It works via ssh, so all your actions are using the same authentication and security as ssh.

### To copy a file from a local host to a remote host

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### To copy a file from a remote host to your local host

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### To copy a directory from your local host to a remote host

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

Try to copy a file over with scp from one machine to another.

## Quiz Question

What command can you use to securely copy files from one host to another?

## Quiz Answer

scp
