# yum and apt

## Lesson Content

Ah, the Batmans of package management, these systems come with all the fixins to make package installation, removal and changes easier, including installing package dependencies. Two of the most popular management systems is <b>yum</b> and <b>apt</b>. Yum is exclusive to the Red Hat family and apt is exclusively to the Debian family.

<b>Install a package from a repository</b>

<pre>
Debian: $ apt install package_name
RPM: $ yum install package_name
</pre>

<b>Remove a package</b>

<pre>
Debian: $ apt remove package_name
RPM: $ yum erase package_name
</pre>

<b>Updating packages for a repository</b>

It's always best practice to update your package repositories so they are up to date before you install and update a package. 

<pre>
Debian: apt update; apt upgrade
RPM: yum update
</pre>

<b>Get information about an installed package</b>

<pre>
Debian: apt show package_name
RPM: yum info package_name
</pre>

## Exercise

Run through each of these package commands and see the output you receive.

## Quiz Question

What command is used to show package information on a Debian system?

## Quiz Answer

apt show
