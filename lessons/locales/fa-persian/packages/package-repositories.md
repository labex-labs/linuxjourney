# Package Repositories

## Lesson Content

How do packages that get uploaded to the internet somehow end up on our computers? Do you go to the download page of each package you want and click download and install? Well, actually you can do that, but there is something better called package repositories. Repositories are just a central storage location for packages. There are tons of repositories that hold lots of packages and best of all they are all found on the internet, no silly installation disks. Your machine doesn't know where to look for these repositories unless you explicitly tell it where to look.

For example, let's say I want WackyWidgets Software on my machine. Well WackyWidgets manages their own repositories for their widget packages, inside this repository are 10 packages, the CoolWidget package, the SuperWidget package, etc. WackyWidgets hosts this repository at a source link called: http://download.widgets/linux/deb/

Now instead of going to their website to download the package directly, you can tell your machine to find WackyWidgets software from the source link. 

Your distribution already comes with pre-approved sources to get packages from and this is how it installs all the base packages you see on your system. On a Debian system, this sources file is the <b>/etc/apt/sources.list</b> file. Your machine will know to look there and check for any source repositories you added. 

## Exercise

No exercises for this lesson.

## Quiz Question

Where is the sources file in a Debian system?

## Quiz Answer

/etc/apt/sources.list