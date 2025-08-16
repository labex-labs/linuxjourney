---
lang: "ja"
title: "カーネルモジュール"
description: "Linux カーネルモジュールについて学びましょう：ロード、アンロード、管理方法。カーネル機能を拡張するための`modprobe`と`lsmod`コマンドを理解しましょう。あなたの Linux の旅を始めましょう！"
keywords: "Linux カーネルモジュール，modprobe, lsmod, カーネル管理，Linux チュートリアル，Linux 初心者，Linux ガイド"
---

## Lesson Content

私が素晴らしい車を持っているとしましょう。私はそれに多くの時間とお金を投資します。スポイラー、ヒッチ、自転車ラック、その他のランダムなものを追加します。これらのコンポーネントは、車のコア機能を実際には変更せず、非常に簡単に取り外したり追加したりできます。カーネルは、カーネルモジュールと同じ概念を使用しています。

カーネル自体はモノリシックなソフトウェアです。新しい種類のキーボードのサポートを追加したい場合、このコードをカーネルコードに直接書き込むことはありません。自転車ラックを車に溶接しないのと同じです（まあ、そうする人もいるかもしれませんが）。カーネルモジュールは、オンデマンドでカーネルにロードおよびアンロードできるコードの断片です。これらにより、コアカーネルコードに追加することなく、カーネルの機能を拡張できます。また、モジュールを追加してもシステムを再起動する必要はありません（ほとんどの場合）。

### View a list of currently loaded modules

```bash
lsmod
```

### Load a module

```bash
sudo modprobe bluetooth
```

`modprobe`は、`/lib/modules/(kernel version)/kernel/drivers`からモジュールをロードします。カーネルモジュールには依存関係がある場合もあります。`modprobe`は、まだロードされていない場合、モジュールの依存関係をロードします。

### Remove a module

```bash
sudo modprobe -r bluetooth
```

### Load on bootup

`modprobe`で一時的にロードする（再起動時にアンロードされる）代わりに、システム起動時にモジュールをロードすることもできます。`/etc/modprobe.d`ディレクトリを変更し、次のように設定ファイルを追加するだけです。

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

options peanut_butter type=almond
```

少し奇抜な例ですが、`peanut_butter`という名前のモジュールがあり、`type=almond`のカーネルパラメータを追加したい場合、この設定ファイルを使用して起動時にロードさせることができます。また、カーネルモジュールには独自のカーネルパラメータがあるため、詳細についてはモジュールについて具体的に読むことをお勧めします。

### Do not load on bootup

次のように設定ファイルを追加することで、モジュールが起動時にロードされないようにすることもできます。

```plaintext
pete@icebox:~$ /etc/modprobe.d/peanutbutter.conf

blacklist peanut_butter
```

## Exercise

`modprobe`で Bluetooth モジュールをアンロードして、何が起こるか見てみましょう。これをどのように修正しますか？

## Quiz Question

モジュールをアンロードするために使用されるコマンドは何ですか？

## Quiz Answer

modprobe -r
