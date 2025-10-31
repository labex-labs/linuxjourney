---
index: 11
lang: "ja"
title: "インデックスノード"
meta_title: "インデックスノード - ファイルシステム"
meta_description: "Linux のインデックスノード（inode）の概念を探る。i-node とは何か、Linux の inode がファイルメタデータをどのように管理するか、そして`df -i`や`ls -li`で inode 使用量をチェックする方法を学ぶ。"
meta_keywords: "linux inode, linux inode, i node, inode, inode linux, inode 番号，ファイルシステム，df -i, ls -li, stat"
---

## Lesson Content

ファイルシステムが実際のファイル全体と、それらを管理するデータベースで構成されていることを思い出してください。このデータベースは inode テーブルとして知られており、`linuxにおけるinode`が機能する基本的な部分です。

### Linux Inode とは何か

Inode（インデックスノードの略）は、このテーブルのエントリです。すべてのファイルとディレクトリには独自の`inode`があります。これは、次のようなファイルに関するすべての情報を記述します。

- ファイルタイプ（例：通常ファイル、ディレクトリ、文字デバイス）
- 所有者
- グループ
- アクセス権限
- タイムスタンプ：mtime（最終変更）、ctime（最終属性変更）、atime（最終アクセス）
- ファイルへのハードリンクの数
- ファイルサイズ
- ファイルに割り当てられたブロック数
- ファイルのデータブロックへのポインタ（最も重要！）

本質的に、`i node`はファイル名と実際のコンテンツを除き、ファイルに関するすべてのメタデータを格納します。

## Exercise

練習あるのみです！Linux ファイルシステムとファイル管理の理解を深めるための実践的なラボを次に示します。

1. **[Linux でファイルとディレクトリを管理する](https://labex.io/ja/labs/comptia-manage-files-and-directories-in-linux-590835)** - ファイルとディレクトリの作成、削除、コピー、移動を練習し、シンボリックリンクとハードリンクの作成を調査しながら inode を分析します。
2. **[Linux でファイルシステムをナビゲートする](https://labex.io/ja/labs/comptia-navigate-the-filesystem-in-linux-590971)** - `pwd`、`cd`、`ls`などの基本的なシェルコマンドを使用して、Linux ファイルシステムをナビゲートするための基本的なスキルを学びます。
3. **[Linux でファイルとコマンドを見つける](https://labex.io/ja/labs/comptia-find-files-and-commands-in-linux-590834)** - `find`、`locate`、`whereis`、`which`、`type`を使用して、Linux でファイルとコマンドを見つけるための重要なテクニックを習得します。

これらのラボは、実際のシナリオで概念を適用し、Linux ファイルシステム管理への自信を築くのに役立ちます。

## Quiz Question

システムに残っている inode の数を確認するにはどうすればよいですか？（大文字と小文字を区別することに注意して、英語で回答してください。）

## Quiz Answer

df -i
