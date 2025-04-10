# find

## Lesson Content

Sistemde bulunan tüm bu dosyalar arasında belirli birini bulmaya çalışmak biraz karmaşık olabilir. Neyse ki bunun için kullanabileceğimiz bir komut var: find!

<pre>$ find /home -name puppies.jpg</pre>

find komutunu kullanırken, arama yapacağınız dizini ve neyi aradığınızı belirtmeniz gerekir. Bu örnekte puppies.jpg adında bir dosyayı arıyoruz.

Aradığınız dosyanın türünü de belirtebilirsiniz.

<pre>$ find /home -type d -name MyFolder</pre>

Gördüğünüz gibi, aradığım dosya türünü dizin için (d) olarak belirttim ve hala MyFolder adıyla arama yapıyorum.

Dikkat edilmesi gereken güzel bir nokta, find komutunun arama yaptığınız dizinde durmayıp, o dizinin sahip olabileceği alt dizinlere de bakmasıdır.

## Exercise

<ol>
<li>Kök dizininden başlayarak içinde "net" kelimesi geçen bir dosya bulun.</li>
</ol>

## Quiz Question

İsme göre arama yapmak istiyorsam find komutunda hangi seçeneği belirtmeliyim?

## Quiz Answer

-name