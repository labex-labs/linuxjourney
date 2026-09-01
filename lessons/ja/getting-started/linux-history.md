---
lesson_id: "linux-history"
course_id: "getting-started"
lang: "ja"
order_index: 1
title: "Linux の歴史"
description: "UNIX、GNU、Linux カーネルが現代の Linux システムへどのように貢献したか学びます。"
meta_title: "Linux の歴史 - 入門ガイド"
meta_description: "Linux の歴史を学び、Linux の旅を始めましょう。UNIX から続く起源、GNU プロジェクト、リーナス・トーバルズによる Linux カーネルの誕生について解説します。"
meta_keywords: "Linux の歴史，Linux 入門，UNIX, GNU プロジェクト，リーナス・トーバルズ，Linux カーネル，Linux 初心者"
---

**Linux Journey** へようこそ。強力な Linux の世界へ飛び込む準備ができたなら、ここが出発点です。案内役のペンギン・ピートと一緒に、まずは **Linux の歴史**を簡単にたどりましょう。

## Linux の前身

Linux がどのように生まれたかを理解するには、ベル研究所の Ken Thompson と Dennis Ritchie が UNIX オペレーティングシステムを開発した1969年までさかのぼります。UNIX は後に C プログラミング言語で書き直され、移植性が高まったことで広く採用されました。

![UNIX の系譜](https://file.labex.io/images/ed9c245d-e8be-4287-bf34-67750b042542.jpg)

:::single-choice{#understand-unix-portability} UNIX を C で書き直した重要な結果は何ですか？

::option[GNU システム用に作られた自由なカーネルになった。]{#unix-became-gnu-kernel explanation="UNIX は GNU プロジェクトより前から存在し、GNU のカーネルではありません。GNU は後に Hurd という別のカーネルの開発を始めました。"}
::option[異なるハードウェアシステムへ移しやすくなった。]{#portable-across-hardware .correct explanation="UNIX を C で記述したことで移植性が高まり、元のハードウェア以外にも普及しました。"}
::option[ベル研究所だけで使うコマンドシェルになった。]{#unix-became-shell explanation="UNIX は単なるシェルではなくオペレーティングシステムです。C への書き直しにより、ベル研究所以外にも普及しました。"}
:::

それから10年以上後、Richard Stallman が GNU プロジェクトを始めました。GNU は「GNU's Not UNIX」の再帰的頭字語で、完全に自由でオープンソースな UNIX 風オペレーティングシステムを作ることが目標でした。プロジェクトは多くの必須コンポーネントと GNU General Public License（GPL）を生み出しましたが、独自のカーネル GNU Hurd は、Linux が利用可能になった時点で一般利用できる状態ではありませんでした。

:::single-choice{#identify-gnu-missing-component} Linux が利用可能になった時点で、準備できていなかった GNU の主要コンポーネントはどれですか？

::option[実用に耐えるカーネル]{#gnu-kernel .correct explanation="GNU は多くのシステムコンポーネントを作っていましたが、独自のカーネル GNU Hurd は一般利用できる状態ではありませんでした。"}
::option[自由ソフトウェアライセンス]{#gnu-license explanation="GNU プロジェクトはすでに GNU General Public License を生み出していました。不足していたシステムコンポーネントは利用可能なカーネルです。"}
::option[必須のシステムツール]{#gnu-tools explanation="GNU はすでに多くの必須ツールを作っていました。カーネルが未完成の主要部分として残っていました。"}
:::

## カーネルの役割

カーネルはオペレーティングシステムの中核コンポーネントです。橋渡し役となり、ハードウェアとソフトウェアの通信を可能にします。CPU、メモリ、周辺機器などのシステムリソースを管理します。完全なオペレーティングシステムには、人が使うツールやアプリケーションに加え、このリソース管理の中核が必要です。

:::single-choice{#recognize-kernel-role} オペレーティングシステムのカーネルが担う役割はどれですか？

::option[シェルへ入力されるすべてのコマンドを書く。]{#write-shell-commands explanation="シェルコマンドを与えるのは人またはスクリプトです。カーネルは、プログラムがコマンドを実行するときに必要な低水準リソースを提供します。"}
::option[インストール済みの全アプリケーションのライセンスを選ぶ。]{#choose-software-licenses explanation="アプリケーションのライセンスを選ぶのは作者や配布者であり、カーネルのリソース管理タスクではありません。"}
::option[CPU、メモリ、接続されたデバイスを管理する。]{#manage-system-resources .correct explanation="カーネルはハードウェアリソースを管理し、ソフトウェアが利用できるようにします。CPU 時間、メモリ、デバイスが代表例です。"}
:::

## Linux カーネルの誕生

1991年、フィンランドの学生 Linus Torvalds が個人プロジェクトとして新しいカーネルの開発を始めました。これが Linux カーネルとなります。Linux が1992年に自由ソフトウェアとして公開されると、ほぼ完成していた GNU システムと組み合わせ、一般に GNU/Linux と呼ばれる完全で自由なオペレーティングシステムを構成できるようになりました。これは **Linux の歴史**における重要な転機です。

![2018年の Linus Torvalds](https://file.labex.io/images/3e1311fd-b8ca-45e7-8d02-9aac6377bb36.jpg)

_2018年の Linus Torvalds（出典：[Wikipedia](https://en.wikipedia.org/wiki/Linus_Torvalds)）_

:::single-choice{#identify-linux-kernel-creator} 1991年に Linux カーネルの開発を始めたのは誰ですか？

::option[Richard Stallman]{#richard-stallman explanation="Richard Stallman は GNU プロジェクトを始めました。GNU は多くのシステムコンポーネントを提供しましたが、Linux カーネルを始めたのは Linus Torvalds です。"}
::option[Dennis Ritchie]{#dennis-ritchie explanation="Dennis Ritchie は UNIX と C プログラミング言語の開発に貢献しました。Linux カーネルは後に Linus Torvalds が始めました。"}
::option[Linus Torvalds]{#linus-torvalds .correct explanation="Linus Torvalds は1991年にカーネルプロジェクトを始め、それが Linux カーネルになりました。"}
:::

**Linux の旅**を続けるため、次のハンズオンラボで基本コマンドを練習し、コマンドライン環境への自信を付けましょう。

1. **[Linux 入門](https://labex.io/labs/linux-getting-started-with-linux-446315)** - `echo`、`date`、基本的な計算など、必須の端末コマンドから Linux の学習を始めます。まったくの初心者に最適です。
2. **[初めての Linux ラボ](https://labex.io/labs/linux-your-first-linux-lab-270253)** - 定番の「Hello, World!」プログラムを Linux で実行し、いくつかの基本コマンドを学びます。
3. **[自分用の端末挨拶を作る](https://labex.io/labs/linux-create-personalized-terminal-greeting-446322)** - 基本的な Linux 端末コマンドを使い、楽しいウェルカムメッセージを作る短いチャレンジです。

## まとめ

UNIX、GNU、Linux カーネルが現代の Linux システムへどう貢献したか説明できるようになりました。

1. UNIX の移植性が重要だった理由を説明する。
2. GNU に不足していた主要コンポーネントがカーネルだったと特定する。
3. システムリソースを管理するカーネルの役割を説明する。
4. Linux カーネルの作者が Linus Torvalds だと特定する。
