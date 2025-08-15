# pwd (Print Working Directory)

## Lesson Content

Everything in Linux is a file, as you journey deeper into Linux you’ll understand this, but for now just keep that in mind. Every file is organized in a hierarchical directory tree. The first directory in the filesystem is aptly named the root directory. The root directory has many folders and files which you can store more folders and files, etc. Here is an example of what the directory tree looks like:

<pre>/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
</pre>

The location of these files and directories are referred to as paths. If you had a folder named home with a folder inside of it named pete and another folder in that folder called Movies, that path would look like this: /home/pete/Movies, pretty simple huh?

Navigation of the filesystem, much like real life is helpful if you know where you are and where you are going. To see where you are, you can use the pwd command, this command means “print working directory” and it just shows you which directory you are in, note the path stems from the root directory.

<pre>$ pwd</pre>

Where are you? Where am I? Give it a try.

## Exercise

No exercises for this lesson.

## Quiz Question

How do I find what directory you are currently in?

## Quiz Answer

pwd
