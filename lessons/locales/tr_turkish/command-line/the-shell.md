# The Shell

## Lesson Content

Dünya sizin istiridyenizdir, ya da aslında kabuk (shell) sizin istiridyenizdir. Kabuk nedir? Kabuk, temel olarak klavyenizden komutlarınızı alıp işletim sistemine gönderen bir programdır. Eğer daha önce bir GUI kullandıysanız, muhtemelen "Terminal" veya "Console" gibi programları görmüşsünüzdür, bunlar sizin için bir kabuk başlatan programlardır. Bu kurs boyunca kabuğun harikalarını öğreneceğiz.

Bu kursta bash (Bourne Again shell) kabuk programını kullanacağız, neredeyse tüm Linux dağıtımları varsayılan olarak bash kabuğunu kullanır. ksh, zsh, tsch gibi başka kabuklar da mevcuttur, ancak bunlara girmeyeceğiz.

Hadi hemen başlayalım! Dağıtımınıza bağlı olarak kabuk istemi değişebilir, ancak çoğunlukla aşağıdaki formata uymalıdır:
<pre>username@hostname:current_directory
pete@icebox:/home/pete $</pre>

İstemin sonundaki $ işaretini fark ettiniz mi? Farklı kabukların farklı istemleri vardır, bizim durumumuzda $ normal bir kullanıcının Bash, Bourne veya Korn kabuğunu kullandığını gösterir. Komutu yazarken istem sembolünü eklemezsiniz, sadece orada olduğunu bilin.

Basit bir komutla başlayalım, echo. echo komutu sadece metin argümanlarını ekrana yazdırır.

<pre>$ echo Hello World</pre>

## Exercise

Bazı diğer Linux komutlarını deneyin ve ne çıktı verdiklerini görün:

<ol>
<li>$ date</li>
<li>$ whoami</li>
</ol>

## Quiz Question

echo Hello World yazdığınızda ekrana ne çıktılanmalıdır?

## Quiz Answer

Hello World