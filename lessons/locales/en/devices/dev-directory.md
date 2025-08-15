# /dev directory

## Lesson Content

When you connect a device to your machine, it generally needs a device driver to function properly. You can interact with device drivers through device files or device nodes, these are special files that look like regular files. Since these device files are just like regular files, you can use programs such as ls, cat, etc to interact with them. These device files are generally stored in the /dev directory. Go ahead and ls the /dev directory on your system, you'll see a large amount of devices files that are on your system.

<pre>$ ls /dev </pre>

Some of these devices you've already used and interacted with such as /dev/null. Remember when we send output to /dev/null, the kernel knows that this device takes all of our input and just discards it, so nothing gets returned.

In the old days, if you wanted to add a device to your system, you'd add the device file in /dev and then probably forget about it. Well repeat that a couple of times and you can see where there was a problem. The /dev directory would get cluttered with static device files of devices that you've long since upgraded, stopped using, etc. Devices are also assigned device files in the order that the kernel finds them. So if everytime you rebooted your system, the devices could have different device files depending on when they were discovered.

Thankfully we no longer use that method, now we have something that we use to dynamically add and remove devices that are currently being used on the system and we'll be discussing this in the coming lessons.

## Exercise

Check out the contents of the /dev directory, do you recognize any familiar devices?

## Quiz Question

Where are device files stored on the system?

## Quiz Answer

/dev
