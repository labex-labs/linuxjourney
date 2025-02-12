# Subnetting Cheats

## Lesson Content

I hate to have to add this section, in the real world you would most likely never have to do subnet math by hand, however if you were getting interviewed on this, you'll have to know how to convert to and from binary form for subnetting. Luckily there are some arithmetic cheats you can memorize. 

First memorize your base-2 calculations, just do it:

<ul>
<li>2^1 = 2</li>
<li>2^2 = 4</li>
<li>2^3 = 8</li>
<li>2^4 = 16</li>
<li>2^5 = 32</li>
<li>2^6 = 64</li>
<li>2^7 = 128</li>
<li>2^8 = 256</li>
<li>2^9 = 512</li>
<li>2^10 = 1024</li>
<li>2^11 = 2048</li>
<li>2^12 = 4096</li>
</ul>

<b>Decimal to Binary Chart</b>

<pre>
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
</pre>

There are lots of reasons why the following chart looks the way it does, if you're curious how it works there are lots of resources online.

Ok, got these memorized? Let's do a quick decimal to binary conversion:

<b>Convert 192.168.23.43 to Binary</b>

Remember: 128 / 64 / 32 / 16 / 8 / 4 / 2 / 1

Let's walk through converting the first octet to binary and you'll understand how the rest works.

<ol>
<li>Can you subtract 192 - 128? Yes, so the first bit is 1</li>
<li>192 - 128 = 64, the next number in the chart is 64, can you subtract 64 - 64? Yes, so the second bit is 1</li>
<li>We've run out of numbers to subtract from, so our binary form of 192 is 11000000</li>
</ol>

<b>Convert Binary 11000000 to Decimal</b>

For binary to decimal conversion you add up the numbers that have a 1, so:

128 + 64 + 0 + 0 + 0 + 0 + 0 + 0 = 192!

## Exercise

Look at your IP address and subnet mask and see how many hosts you can have on your subnet.

## Quiz Question

What is the binary conversion of 123?

## Quiz Answer

1111011