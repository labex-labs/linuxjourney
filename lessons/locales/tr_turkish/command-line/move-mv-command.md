# mv (Move)

## Lesson Content

Dosyaları taşımak ve yeniden adlandırmak için kullanılır. Bayraklar ve işlevsellik açısından cp komutuna oldukça benzer.

Dosyaları şu şekilde yeniden adlandırabilirsiniz:

<pre>$ mv oldfile newfile</pre>

Veya bir dosyayı farklı bir dizine taşıyabilirsiniz:

<pre>$ mv file2 /home/pete/Documents</pre>

Ve birden fazla dosyayı taşıyabilirsiniz:

<pre>$ mv file_1 file_2 /somedirectory</pre>

Dizinleri de yeniden adlandırabilirsiniz:

<pre>$ mv directory1 directory2</pre>

cp komutunda olduğu gibi, bir dosya veya dizini mv ile taşıdığınızda, aynı dizindeki herhangi bir şeyin üzerine yazacaktır. Bu nedenle, herhangi bir şeyin üzerine yazmadan önce sizi uyarması için -i bayrağını kullanabilirsiniz.

<pre>mv -i directory1 directory2</pre>

Diyelim ki bir dosyayı öncekinin üzerine yazacak şekilde taşımak istiyorsunuz. Bu durumda dosyanın bir yedeğini de oluşturabilirsiniz ve eski sürümü ~ ile yeniden adlandıracaktır.

<pre>$ mv -b directory1 directory2</pre>

## Exercise

Bir dosyayı yeniden adlandırın, ardından bu dosyayı farklı bir dizine taşıyın.

## Quiz Question

cat adlı bir dosyayı dog olarak nasıl yeniden adlandırırsınız?

## Quiz Answer

mv cat dog