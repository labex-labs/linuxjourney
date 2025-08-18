---
index: 5
lang: "ja"
title: "カーネルの場所"
meta_title: "カーネルの場所 - Kernel"
meta_description: "/boot ディレクトリ内の Linux カーネルの場所について学び、vmlinuz、initrd、System.map を理解します。カーネルファイルを探索し、スペースを効果的に管理します。"
meta_keywords: "Linux カーネル，/boot ディレクトリ，vmlinuz, initrd, System.map, Linux 初心者，カーネルチュートリアル，Linux ガイド"
---

## Lesson Content

新しいカーネルをインストールするとどうなるでしょうか？実際には、いくつかのファイルがシステムに追加されます。これらのファイルは通常、`/boot` ディレクトリに追加されます。

異なるカーネルバージョンの複数のファイルが表示されます。

- `vmlinuz` - これが実際の Linux カーネルです
- `initrd` - 以前に説明したように、`initrd` はカーネルをロードする前に使用される一時的なファイルシステムとして使用されます
- `System.map` - シンボリックルックアップテーブル
- `config` - カーネル設定。独自のカーネルをコンパイルしている場合、どのモジュールをロードできるかを設定できます

`/boot` ディレクトリの容量が不足した場合は、これらのファイルの古いバージョンを削除するか、パッケージマネージャーを使用することができます。ただし、このディレクトリでメンテナンスを行う際は注意し、現在使用しているカーネルを誤って削除しないようにしてください。

## Exercise

Go into your boot directory and see what files are in there.

## Quiz Question

`/boot` 内のカーネルイメージは何と呼ばれていますか？

## Quiz Answer

vmlinuz
