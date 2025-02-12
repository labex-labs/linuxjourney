# Systemd Overview

## Lesson Content

Systemd is slowly becoming the emerging standard for init. If you have a /usr/lib/systemd directory, you're most likely using systemd.

Systemd uses goals to get your system up and running. Basically you have a target that you want to achieve and this target also has dependencies that we need to achieve. Systemd is extremely flexible and robust, it does not follow a strict sequence to get processes started. Here's what happens during the typical systemd boot:

<ol>
<li>First, systemd loads it's configuration files, usually located in /etc/systemd/system or /usr/lib/systemd/system</li>
<li>Then it determines its boot goal, which is usually default.target</li>
<li>Systemd figures out the dependencies of the boot target and activates them</l>
</ol>

Similar to Sys V runlevels, systemd boots into different targets:

<ul>
<li>poweroff.target - shutdown system</li>
<li>rescue.target - single user mode</li>
<li>multi-user.target - multiuser with networking</li>
<li>graphical.target - multiuser with networking and GUI</li>
<li>reboot.target - restart</li>
</ul>

The default boot goal of default.target usually points to the graphical.target. 

The main object that systemd works with are known as units. Systemd doesn't just stop and start services, it can mount filesystems, monitor your network sockets, etc and because of that robustness it has different types of units it operates. The most common units are:

<ul>
<li>Service units - these are the services we've been starting and stopping, these unit files end in .service</li>
<li>Mount units - These mount filesystems, these unit files end in .mount</li>
<li>Target units - These group together other units, the files end in .target</li>
</ul>

For example, let's say we boot into our default.target, well this target groups together the networking.service unit, crond.service unit, etc, so once we activate a single unit, everything below that unit gets activated as well.

## Exercise

No exercises for this lesson.

## Quiz Question

What unit is used to group together other units?

## Quiz Answer

target
