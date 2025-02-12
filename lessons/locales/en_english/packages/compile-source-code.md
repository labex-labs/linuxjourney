# Compile Source Code

## Lesson Content

Often times you will encounter an obscure package that only comes in the form of pure source code. You'll need to use a few commands to get that source code package compiled and installed on your system. 

First thing is first, you'll need to have software to install the tools that will allow you to compile source code. 

<pre>$ sudo apt install build-essential</pre>

Once you do that, extract the contents of the package file, most likely a .tar.gz file. 

<pre>$ tar -xzvf package.tar.gz</pre>

Before you do anything, take a look at the README or INSTALL file inside the package. Sometimes there will be specific installation instructions. 

Depending on what compile method that the developer used, you'll have to use different commands, such as cmake or something else.

However, most commonly you'll see basic make compilation, so we'll discuss that:

Inside the package contents will be a configure script, this script checks for dependencies on your system and if you are missing anything, you'll see an error and you'll need to fix those dependencies. 

<pre>$ ./configure</pre>

The <b>./</b> allows you to execute a script in the current directory. 

<pre>$ make</pre>

Inside of the package contents, there is a file called Makefile that contains rules to building the software. When you run the make command, it looks at this file to build the software.

<pre>$ sudo make install</pre>

This command actually installs the package, it will copy the correct files to the correct locations on your computer.

If you want to uninstall the package, use:

<pre>$ sudo make uninstall</pre>

Be wary when using make install, you may not realize how much is actually going on in the background. If you decide to remove this package, you may not actually remove everything because you didn't realize what was added to your system. Instead forget everything about make install that I just explained to you and use the <b>checkinstall</b> command. This command will make a .deb file for you that you can easily install and uninstall. 

<pre>$ sudo checkinstall</pre> 

This command will essentially "make install" and build a .deb package and install it. This makes it easier to remove the package later on.

## Exercise

Find a source code program (from a trusted site) and install from source.

## Quiz Question

What should you use instead of make install ALWAYS? 

## Quiz Answer

checkinstall
