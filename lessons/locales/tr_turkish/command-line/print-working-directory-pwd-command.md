# pwd (Print Working Directory)

## Lesson Content

Linux'ta her şey bir dosyadır, Linux'un derinliklerine indikçe bunu anlayacaksınız, ancak şimdilik bunu aklınızda tutun. Her dosya hiyerarşik bir dizin ağacında düzenlenmiştir. Dosya sistemindeki ilk dizin, yerinde bir isimle kök dizin (root directory) olarak adlandırılır. Kök dizinin içinde, daha fazla klasör ve dosya depolayabileceğiniz birçok klasör ve dosya bulunur. İşte dizin ağacının nasıl göründüğüne dair bir örnek:

<pre>/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
</pre>

Bu dosya ve dizinlerin konumları yol (path) olarak adlandırılır. Eğer içinde pete adında bir klasör ve onun içinde de Movies adında başka bir klasör bulunan home adında bir klasörünüz varsa, bu yol şöyle görünecektir: /home/pete/Movies, oldukça basit, değil mi?

Dosya sisteminde gezinmek, tıpkı gerçek hayatta olduğu gibi, nerede olduğunuzu ve nereye gittiğinizi biliyorsanız yardımcı olur. Nerede olduğunuzu görmek için pwd komutunu kullanabilirsiniz. Bu komut "print working directory" (çalışma dizinini yazdır) anlamına gelir ve size hangi dizinde olduğunuzu gösterir. Yolun kök dizinden başladığını unutmayın.

<pre>$ pwd</pre>

Neredesiniz? Ben neredeyim? Bir deneyin.

## Exercise

Bu ders için alıştırma yok.

## Quiz Question

Şu anda hangi dizinde olduğunuzu nasıl öğrenebilirsiniz?

## Quiz Answer

pwd