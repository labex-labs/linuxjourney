---
lesson_id: "ubuntu"
course_id: "getting-started"
lang: "ja"
order_index: 5
title: "Ubuntu"
description: "Ubuntu が Debian の基盤と、親しみやすいデスクトップ、サーバー、リリースの選択肢をどう組み合わせるか学びます。"
meta_title: "Ubuntu Linux とは"
meta_description: "Ubuntu Linux の概要や人気の理由、リリースモデル、パッケージ管理の仕組みを解説。デスクトップからサーバーまで幅広く利用される理由を紹介します。"
meta_keywords: "Ubuntu Linux, Ubuntu ディストリビューション，Ubuntu とは，Ubuntu リリース，Ubuntu パッケージ管理，Ubuntu Debian ベース，Linux ディストリビューション"
---

## Ubuntu とは

Ubuntu は、最も広く使われる Linux ディストリビューションの1つです。Canonical が開発し、Debian を基盤に、親しみやすい設計、大きなユーザーコミュニティ、幅広いハードウェアとソフトウェアへの対応で知られます。

手動作業の多い高度な設定から始めず Linux を学びたい人の一般的な出発点です。個人用コンピューター、開発システム、クラウド、サーバーで使われ、ほかのディストロには少ない広がりを持ちます。

:::single-choice{#identify-ubuntu-base}
Ubuntu の基盤となるディストリビューションはどれですか？

::option[Debian ディストリビューション]{#debian-base .correct explanation="Ubuntu は Debian を基にし、そのパッケージ方式の多くを引き継ぎつつ、独自のリリース、既定値、サポートモデルを追加します。"}
::option[Fedora ディストリビューション]{#ubuntu-fedora-base explanation="Fedora は Red Hat エコシステムに属し、Ubuntu の基盤ではありません。Ubuntu は Debian 系です。"}
::option[Arch ディストリビューション]{#ubuntu-arch-base explanation="Arch Linux は独自のパッケージシステムとリリース方式を持つ別のディストリビューションで、Ubuntu は Debian ベースです。"}
:::

## Ubuntu が人気の理由

Ubuntu は Linux を日常利用しやすくすることを目指します。洗練されたインストーラー、充実した文書、予測可能なリリース、多数のチュートリアルとサードパーティー支援があり、多くの人にとって暮らしやすいディストロです。

ノート PC、デスクトップ、仮想マシン、サーバー、クラウドなど多様な環境で動くことも、汎用ディストリビューションとしての評価を強めています。

:::single-choice{#recognize-beginner-support}
初心者の問題解決に最も直接役立つ Ubuntu の特性はどれですか？

::option[導入する各プログラムで手動コンパイルが必須]{#manual-compilation explanation="通常はパッケージ化されたソフトウェアを提供し、毎回手動コンパイルを要求しません。追加作業は問題解決を簡単にしません。"}
::option[充実した文書と大きなユーザーコミュニティ]{#documentation-community .correct explanation="文書とコミュニティの議論から説明や問題解決方法を見つけやすく、学習の障壁を下げます。"}
::option[経験豊富な管理者だけが利用できる限定的な案内]{#limited-guidance explanation="Ubuntu は多様な技能レベル向けの豊富な案内で知られ、専門家だけに限定すると初心者向けではなくなります。"}
:::

## Ubuntu と Debian

Ubuntu は Debian ベースで、パッケージ管理モデルとソフトウェアのパッケージ化方式の多くを引き継ぎます。Ubuntu で `apt` を学ぶと、ほかの Debian ベースシステムの理解にも役立ちます。

ただし、Ubuntu は単なる「デスクトップ付き Debian」ではありません。独自のリリース日程、既定値、サポートモデル、エコシステムがあります。比較には [Linux ディストリビューションの選び方](https://labex.io/lesson/choosing-a-linux-distribution) と [Debian](https://labex.io/lesson/debian) を参照してください。

## Ubuntu のリリース

Ubuntu には主に2種類のリリースがあります。6か月ごとに新リリースを公開し、そのうち2年ごとの1つが Long Term Support（LTS）になります。より安定した基盤が必要なデスクトップ、ワークステーション、サーバーでは LTS がよく選ばれます。

信頼できる基盤が欲しい人は LTS を、新しい機能が欲しい人は短い間隔で登場する中間リリースを選べます。

:::single-choice{#choose-ubuntu-lts}
長く使え、予測可能な基盤が必要なシステムに最も適した Ubuntu リリースはどれですか？

::option[中間リリース]{#interim-release explanation="中間リリースは頻繁に登場し新機能を早く提供しますが、短いサポート期間は要件に合いません。"}
::option[LTS リリース]{#lts-release .correct explanation="LTS は長期サポートを目的とし、信頼できる基盤を重視するシステムでよく選ばれます。"}
::option[パッケージ更新]{#package-update explanation="パッケージ更新は導入済みリリース内のソフトウェアを変えるもので、OS の2つのリリース種類ではありません。"}
:::

## パッケージ管理

Debian ベースの Ubuntu は `.deb` パッケージ形式と `apt` パッケージマネージャーを使い、ソフトウェアを導入、更新、削除します。大きなソフトウェアエコシステムと、よく知られたコマンドライン作業を利用できます。

成熟した Debian のツールと、広く文書化された環境を組み合わせるパッケージ管理は、Ubuntu の実用的な強みです。

:::single-choice{#identify-ubuntu-package-tool}
Ubuntu でソフトウェアを導入するパッケージ管理ツールはどれですか？

::option[`.deb`]{#deb-format explanation=".deb は Debian ベースシステムのパッケージ形式で、コマンドラインの管理ツールではありません。"}
::option[`LTS`]{#lts-label explanation="LTS は長期サポートリリースを示し、パッケージを導入・管理しません。"}
::option[`apt`]{#ubuntu-apt-tool .correct explanation="Ubuntu は apt でパッケージを導入、更新、削除し、Debian の .deb 形式を扱います。"}
:::

## デスクトップとサーバーでの利用

デスクトップでは洗練された GNOME ベースの体験と親しみやすい既定値で知られ、サーバーでは開発、Web インフラ、クラウドへ広く配備されます。ノート PC での学習から本番ワークロードまで、1つのディストリビューションを広げて使いたい人に適します。

## 初心者が Ubuntu を選ぶ理由

多くのディストロより導入と問題解決が簡単で、大きな利用者基盤により、問題発生時に参照できるチュートリアル、フォーラム投稿、ガイドが豊富です。初心者向けでありながら将来の柔軟性も欲しい人の一般的な出発点です。

## 関連資料

- [Ubuntu Desktop](https://ubuntu.com/desktop)
- [Ubuntu Server](https://ubuntu.com/server)
- [Ubuntu のリリースサイクル](https://ubuntu.com/releaseendoflife)
- [Ubuntu リリースの文書](https://documentation.ubuntu.com/project/release-team/ubuntu-releases/)

1. **[Linux クイックスタート](https://labex.io/courses/quick-start-with-linux)** - Linux とコマンドライン技能の実用的な基礎を築きます。
2. **[初心者のための Linux](https://labex.io/courses/linux-for-noobs)** - 初心者向けの順序で Linux の基本を学びます。
3. **[ジュニアシステム管理者になる](https://labex.io/courses/become-a-junior-system-administrator)** - 基本に慣れた後、実用的な Linux 管理技能へ進みます。

## まとめ

Ubuntu が Debian を基盤にしながら、独自のリリースとユーザー体験を提供する仕組みを説明できるようになりました。

1. Ubuntu の基盤が Debian だと特定する。
2. 初心者を支える特性を見分ける。
3. Ubuntu の LTS と中間リリースを比較する。
4. Ubuntu のパッケージ管理に `apt` を使う。
