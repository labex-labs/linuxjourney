---
title: "/etc/fstab"
description: "Linux の/etc/fstab について、起動時のファイルシステムのマウント設定方法、デバイスエントリの管理方法を学びます。初心者向けの fstab ガイドです！"
keywords: "/etc/fstab, Linux fstab, ファイルシステムのマウント，Linux 起動，fstab チュートリアル，初心者，ガイド"
---

## Lesson Content

起動時にファイルシステムを自動的にマウントしたい場合、`/etc/fstab`（「エフ・エス・タブ」と発音し、「エフ・スタブ」ではありません）というファイルに追加できます。これは filesystem table の略です。このファイルには、マウントされるファイルシステムの永続的なリストが含まれています。

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

各行は 1 つのファイルシステムを表しており、フィールドは以下の通りです。

- UUID - デバイス識別子
- Mount point - ファイルシステムがマウントされるディレクトリ
- Filesystem type
- Options - その他のマウントオプション。詳細は man ページを参照してください。
- Dump - dump ユーティリティがバックアップを作成するタイミングを決定するために使用します。通常は 0 に設定します。
- Pass - fsck がファイルシステムをチェックする順序を決定するために使用します。値が 0 の場合、チェックされません。

エントリを追加するには、上記のエントリ構文を使用して`/etc/fstab`ファイルを直接変更します。このファイルを変更する際は注意してください。間違えると、少し面倒なことになる可能性があります。

## Exercise

これまで作業してきた USB ドライブを`/etc/fstab`にエントリとして追加してください。再起動後も、それがマウントされていることを確認できるはずです。

## Quiz Question

ファイルシステムがどのようにマウントされるかを定義するために使用されるファイルは何ですか？

## Quiz Answer

/etc/fstab
