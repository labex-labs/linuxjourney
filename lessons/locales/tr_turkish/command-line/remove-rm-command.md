# rm (Remove)

## Lesson Content

Şimdi çok fazla dosyamız olduğunu düşünüyorum, hadi bazı dosyaları kaldıralım. Dosyaları kaldırmak için rm komutunu kullanabilirsiniz. rm (remove - kaldır) komutu dosya ve dizinleri silmek için kullanılır.

<pre>$ rm file1</pre>

rm komutunu kullanırken dikkatli olun, kaldırılan dosyaları geri alabileceğiniz sihirli bir çöp kutusu yoktur. Bir kez gittiklerinde, tamamen giderler, bu yüzden dikkatli olun.

Neyse ki bazı güvenlik önlemleri alınmıştır, böylece sıradan bir kullanıcı önemli dosyaları kolayca kaldıramaz. Yazma korumalı dosyalar, silinmeden önce sizden onay isteyecektir. Bir dizin yazma korumalıysa, kolayca kaldırılamaz.

Eğer bunların hiçbirini umursamıyorsanız, kesinlikle bir grup dosyayı kaldırabilirsiniz.

<pre>$ rm -f file1</pre>

-f veya force seçeneği, rm'ye kullanıcıya sormadan (uygun izinlere sahip olduğunuz sürece) yazma korumalı olsun veya olmasın tüm dosyaları kaldırmasını söyler.

<pre>$ rm -i file</pre>

Diğer birçok komutta olduğu gibi -i bayrağını eklemek, dosyaları veya dizinleri gerçekten kaldırmak isteyip istemediğiniz konusunda size bir onay isteyecektir.

<pre>$ rm -r directory</pre>

Varsayılan olarak bir dizini sadece rm ile kaldıramazsınız, içindeki tüm dosyaları ve sahip olabileceği alt dizinleri kaldırmak için -r (recursive - özyinelemeli) bayrağını eklemeniz gerekir.

Bir dizini rmdir komutu ile de kaldırabilirsiniz.

<pre>$ rmdir directory</pre>

## Exercise

<ol>
<li>-file adında bir dosya oluşturun (tireyi unutmayın!).</li>
<li>Bu dosyayı kaldırın.</li>
</ol>

## Quiz Question

myfile adlı bir dosyayı nasıl kaldırırsınız?

## Quiz Answer

rm myfile