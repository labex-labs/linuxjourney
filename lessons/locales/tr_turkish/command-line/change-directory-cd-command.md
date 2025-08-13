# cd (Change Directory)

## Lesson Content

Şimdi nerede olduğunuzu biliyorsunuz, hadi dosya sisteminde biraz dolaşmayı deneyelim. Yolları kullanarak gezineceğimizi unutmayın. Bir yolu belirtmenin iki farklı yolu vardır: mutlak ve göreceli yollar.

<ul>
<li>Absolute path: Bu, kök dizinden başlayan yoldur. Kök dizin en üst seviyedir ve genellikle bir eğik çizgi (/) ile gösterilir. Yolunuz / ile başlıyorsa, kök dizinden başladığınız anlamına gelir. Örneğin, /home/pete/Desktop.</li>

<li>Relative path: Bu, dosya sisteminde şu anda bulunduğunuz konumdan başlayan yoldur. Eğer /home/pete/Documents konumundaysam ve Documents içindeki taxes adlı bir dizine gitmek istiyorsam, /home/pete/Documents/taxes gibi kökten başlayan tüm yolu belirtmek zorunda değilim, sadece taxes/ yazabilirim.</li>
</ul>

Yolların nasıl çalıştığını öğrendiğinize göre, şimdi istediğimiz dizine geçmemize yardımcı olacak bir şeye ihtiyacımız var. Neyse ki, bunun için cd veya "change directory" komutunu kullanabiliriz.

<pre>$ cd /home/pete/Pictures</pre>

Şimdi dizin konumumu /home/pete/Pictures olarak değiştirdim.

Bu dizinden Hawaii adında bir klasör var, bu klasöre şu şekilde gidebilirim:

<pre>$ cd Hawaii</pre>

Sadece klasör adını kullandığımı fark ettiniz mi? Çünkü zaten /home/pete/Pictures içindeydim.

Mutlak ve göreceli yollarla sürekli gezinmek oldukça yorucu olabilir, neyse ki size yardımcı olacak bazı kısayollar var.

<ul>
<li>. (mevcut dizin). Şu anda bulunduğunuz dizin.</li>
<li>.. (üst dizin). Sizi mevcut dizinin bir üst dizinine götürür.</li>
<li>~ (ev dizini). Bu dizin varsayılan olarak "ev dizininizi" gösterir. Örneğin /home/pete.</li>
<li>- (önceki dizin). Sizi az önce bulunduğunuz dizine götürür.</li>
</ul>

<pre>$ cd .
$ cd ..
$ cd ~
$ cd -
</pre>
Bunları deneyin!

## Exercise

<ol>
<li>cd komutunu herhangi bir bayrak olmadan çalıştırın, sizi nereye götürüyor?</li>
</ol>

## Quiz Question

Eğer /home/pete/Pictures konumundaysanız ve /home/pete'ye gitmek istiyorsanız, kullanabileceğiniz iyi bir kısayol nedir?

## Quiz Answer

cd ..
