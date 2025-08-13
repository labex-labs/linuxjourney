# alias

## Lesson Content

Bazen komutları yazmak oldukça tekrarlayıcı olabilir veya uzun bir komutu birçok kez yazmanız gerekiyorsa, bunun için bir alias (takma ad) kullanmak en iyisidir. Bir komut için alias oluşturmak için, sadece bir alias adı belirleyip bunu komuta atamanız yeterlidir.

<pre>$ alias foobar='ls -la'</pre>

Artık `ls -la` yazmak yerine, `foobar` yazarak aynı komutu çalıştırabilirsiniz, oldukça kullanışlı bir özellik. Ancak bu komut yeniden başlatmadan sonra alias'ınızı kaydetmeyecektir, bu yüzden kalıcı bir alias eklemek istiyorsanız bunu şu dosyaya eklemeniz gerekir:

<pre>~/.bashrc</pre>

veya benzer dosyalara ekleyebilirsiniz.

Alias'ları kaldırmak için unalias komutunu kullanabilirsiniz:

<pre>$ unalias foobar</pre>

## Exercise

Birkaç alias oluşturun ve sonra bunları kaldırın.

## Quiz Question

Alias oluşturmak için hangi komut kullanılır?

## Quiz Answer

alias