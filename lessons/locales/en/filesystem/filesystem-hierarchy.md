# Filesystem Hierarchy

## Lesson Content

At this point, you're probably well familiar with the directory structure of your system, if not you will be soon. Filesystems can vary with how they are structured, but for the most part they should conform to the Filesystem Hierarchy Standard.

Go ahead and do an <b>ls -l /</b> to see the directories listed under the root directory, yours may look different than mine, but the directories should for the most part look like the following:

<ul>
<li>/ - The root directory of the entire filesystem hierarchy, everything is nestled under this directory.</li>
<li>/bin - Essential ready-to-run programs (binaries), includes the most basic commands such as ls and cp.</li>
<li>/boot - Contains kernel boot loader files.</li>
<li>/dev - Device files.</li>
<li>/etc - Core system configuration directory, should hold only configuration files and not any binaries.</li>
<li>/home - Personal directories for users, holds your documents, files, settings, etc. </li>
<li>/lib - Holds library files that binaries can use.</li>
<li>/media - Used as an attachment point for removable media like USB drives.</li>
<li>/mnt - Temporarily mounted filesystems.</li>
<li>/opt - Optional application software packages.</li>
<li>/proc - Information about currently running processes.</li>
<li>/root - The root user's home directory.</li>
<li>/run - Information about the running system since the last boot.</li>
<li>/sbin - Contains essential system binaries, usually can only be ran by root.</li>
<li>/srv - Site-specific data which are served by the system.</li>
<li>/tmp - Storage for temporary files</li>
<li>/usr - This is unfortunately named, most often it does not contain user files in the sense of a home folder. This is meant for user installed software and utilities, however that is not to say you can't add personal directories in there. Inside this directory are sub-directories for /usr/bin, /usr/local, etc.</li>
<li>/var - Variable directory, it's used for system logging, user tracking, caches, etc. Basically anything that is subject to change all the time.</li>
</ul>

## Exercise

Look inside your /usr directory, what kind of information is located there?

## Quiz Question

What directory is used to store logs?

## Quiz Answer

/var
