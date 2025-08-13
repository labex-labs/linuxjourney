# ls (List Directories)

## Lesson Content

Artık sistemde nasıl hareket edeceğimizi biliyoruz, peki bize nelerin sunulduğunu nasıl öğreneceğiz? Şu anda karanlıkta hareket ediyormuşuz gibi. Neyse ki dizin içeriklerini listelemek için harika ls komutunu kullanabiliriz. ls komutu varsayılan olarak mevcut dizindeki dizinleri ve dosyaları listeler, ancak hangi yolun dizinlerini listelemek istediğinizi de belirtebilirsiniz.

<pre>$ ls
$ ls /home/pete</pre>

ls oldukça kullanışlı bir araçtır, ayrıca baktığınız dosya ve dizinler hakkında detaylı bilgi de gösterir.

Ayrıca bir dizindeki tüm dosyaların görünür olmayacağını unutmayın. . ile başlayan dosya adları gizlidir, ancak bunları ls komutuna -a bayrağını (all için) ekleyerek görüntüleyebilirsiniz.

<pre>$ ls -a</pre>

Bir diğer kullanışlı ls bayrağı da uzun format için kullanılan -l'dir. Bu, dosyaları uzun formatta detaylı bir liste olarak gösterir. Bu size soldan başlayarak şu detaylı bilgileri gösterecektir: dosya izinleri, bağlantı sayısı, sahibinin adı, sahibinin grubu, dosya boyutu, son değişiklik tarihi ve dosya/dizin adı.

<pre>$ ls -l</pre>

<pre>pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos</pre>

Komutların daha fazla işlevsellik eklemek için bayraklar (veya argümanlar ya da seçenekler, ne demek isterseniz) adı verilen özellikleri vardır. -a ve -l'yi nasıl eklediğimizi gördünüz, bunları -la şeklinde birlikte de ekleyebilirsiniz. Bayrakların sırası hangi sırayla gideceğini belirler, çoğu zaman bunun gerçekten bir önemi yoktur, bu yüzden ls -al şeklinde de kullanabilirsiniz ve yine çalışacaktır.

<pre>$ ls -la</pre>

## Exercise

ls komutunu farklı bayraklarla çalıştırın ve aldığınız çıktıları inceleyin.

## Quiz Question

Gizli dosyaları görmek için hangi komutu kullanırsınız?

## Quiz Answer

ls -a