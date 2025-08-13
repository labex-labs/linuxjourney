# cp (Copy)

## Lesson Content

Hadi bu dosyaların bazı kopyalarını oluşturalım. Diğer işletim sistemlerindeki kopyala-yapıştır işlemlerine benzer şekilde, kabuk bize bunu yapmanın daha basit bir yolunu sunar.

<pre>$ cp mycoolfile /home/pete/Documents/cooldocs</pre>

mycoolfile kopyalamak istediğiniz dosya ve /home/pete/Documents/cooldocs dosyayı kopyaladığınız hedef konumdur.

Birden fazla dosya ve dizini de kopyalayabilir ve joker karakterler (wildcards) kullanabilirsiniz. Joker karakter, desen tabanlı seçim için kullanılan ve aramalarda size daha fazla esneklik sağlayan bir karakterdir. Her komutta joker karakterleri kullanabilirsiniz.

<ul>
<li>* joker karakterlerin en yaygınıdır, tek karakterleri veya herhangi bir karakter dizisini temsil etmek için kullanılır.</li>
<li>? tek bir karakteri temsil etmek için kullanılır</li>
<li>[] köşeli parantezler içindeki herhangi bir karakteri temsil etmek için kullanılır</li>
</ul>

<pre>$ cp *.jpg /home/pete/Pictures</pre>

Bu komut, mevcut dizindeki .jpg uzantılı tüm dosyaları Pictures dizinine kopyalayacaktır.

Kullanışlı bir komut olan -r bayrağı, bir dizin içindeki dosya ve dizinleri özyinelemeli (recursive) olarak kopyalar.

Bir dizini ve içindeki birkaç dosyayı Documents dizininize kopyalamayı deneyin. Çalışmadı değil mi? Bunun nedeni, dizin içindeki dosya ve dizinleri de -r komutu ile kopyalamanız gerektiğidir.

<pre>$ cp -r Pumpkin/ /home/pete/Documents</pre>

Dikkat edilmesi gereken bir nokta, aynı dosya adına sahip bir dizine bir dosya kopyalarsanız, dosya kopyaladığınız şeyle üzerine yazılacaktır. Bu, yanlışlıkla üzerine yazılmasını istemediğiniz bir dosyanız varsa iyi bir durum değildir. Bir dosyanın üzerine yazmadan önce sizi uyarması için -i (interactive) bayrağını kullanabilirsiniz.

<pre>$ cp -i mycoolfile /home/pete/Pictures</pre>

## Exercise

Birkaç dosyayı kopyalayın, önemli bir şeyin üzerine yazmamaya dikkat edin.

## Quiz Question

Bir dizini kopyalamak için hangi bayrağı belirtmeniz gerekir?

## Quiz Answer

-r