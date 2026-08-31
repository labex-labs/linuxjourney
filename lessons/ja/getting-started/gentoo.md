---
lesson_id: "gentoo"
course_id: "getting-started"
lang: "ja"
order_index: 8
title: "Gentoo"
description: "Gentoo が Portage、ソースベースの構築、USE フラグを使い、システムを細かく制御する仕組みを学びます。"
meta_title: "Gentoo Linux ディストリビューション"
meta_description: "Gentoo Linux ディストリビューションの概要、Portage パッケージマネージャーの仕組み、そしてソースベースのカスタマイズと制御を求める上級ユーザーに Gentoo が選ばれる理由を解説します。"
meta_keywords: "Gentoo ディストリビューション，Gentoo Linux, Gentoo とは，Portage パッケージマネージャー, Gentoo ソースベース，上級者向け Linux"
---

## Gentoo とは

Gentoo は、システムの構築方法を深く制御したい人向けの Linux ディストリビューションです。多くの主流ディストロと異なり、構築済みバイナリを導入するだけでなく、ローカルマシンでソフトウェアをコンパイルするソースベースの方式で知られます。

細かな調整、学習、カスタマイズを楽しむ上級者に特に魅力的です。

:::single-choice{#match-gentoo-user}
Gentoo に最もよく合う利用者はどれですか？

::option[システムを細かく制御したい、意欲的な学習者]{#committed-system-builder .correct explanation="詳細な構築と設定を選びたい利用者に応えますが、その制御には時間と関与も必要です。"}
::option[設定作業を最小限にしたい初心者]{#minimal-setup-beginner explanation="多くの設定と保守を利用者へ求めるため、準備済みの既定値が多いディストリビューションの方が適します。"}
::option[ソフトウェアに関する判断を一切したくない利用者]{#no-software-decisions explanation="機能とソフトウェアの選択が設計の中心で、それを避けると Gentoo を選ぶ理由の多くが失われます。"}
:::

## Gentoo の違い

Gentoo はカスタマイズを追加機能ではなく、ディストリビューションの中心として扱います。任意機能、依存関係、構築時の動作について、ほかの多くのディストロより直接的で細かな選択ができます。

強力な一方、利用者へ多くを求め、Linux への最も簡単な入口を主目的にはしていません。

## Portage

Gentoo の中心にはパッケージ管理システム **Portage** があります。ソフトウェアの導入と保守を扱い、ソースベースの設計と密接に結び付きます。

特徴的な **USE フラグ**により、ソフトウェアを構築する前に任意機能を有効または無効にでき、完成するシステムを非常に細かく制御できます。

:::single-choice{#identify-portage-role}
Gentoo における Portage の役割は何ですか？

::option[グラフィカルデスクトップとアプリケーションメニューだけを提供する]{#portage-desktop explanation="デスクトップ環境はグラフィカル画面を扱います。Portage は Gentoo 全体のソフトウェアを管理します。"}
::option[ソフトウェアの導入、依存関係、保守を管理する]{#portage-package-manager .correct explanation="Portage はパッケージと、その構築・保守に関わる選択を調整する Gentoo のパッケージ管理システムです。"}
::option[Linux カーネルを別の OS へ置き換える]{#portage-kernel-replacement explanation="カーネル関連パッケージも扱えますが、Linux を別 OS へ置き換えるものではありません。"}
:::

:::single-choice{#explain-use-flags}
Gentoo の USE フラグは何を制御しますか？

::option[コンピューターに搭載された物理メモリの量]{#physical-memory explanation="搭載メモリはハードウェアの特性で、USE フラグはソフトウェア機能を設定します。"}
::option[パッケージ構築時に含める任意機能と依存関係]{#package-features .correct explanation="対応させる任意機能を表し、その選択によって Portage が導入する依存関係も変わる場合があります。"}
::option[ログイン時に表示するユーザー名]{#login-username explanation="アカウント名はユーザー設定で管理し、USE フラグは任意のパッケージ機能を表します。"}
:::

## ソースベースのカスタマイズ

ソフトウェアをローカルで構築するため、特定の必要条件や好みに合わせられます。不要な機能を取り除き、特定の作業へ最適化したい人に魅力的です。

依存関係、コンパイル、システム設計について主流ディストロ以上に学べる、教育的な側面もあります。

:::single-choice{#recognize-source-build-tradeoff}
Gentoo のソースベースのカスタマイズには、どのようなトレードオフがありますか？

::option[制御が増える代わりに、構築時間と利用者の判断も増える]{#control-for-time .correct explanation="ローカル構築と機能選択は細かな制御を提供しますが、時間と注意も必要です。"}
::option[制御が減るため、依存関係を理解する必要がなくなる]{#less-control explanation="依存関係と構築の選択は減るのではなく増え、その理解も学習上の価値です。"}
::option[自動設定により継続的なパッケージ保守が不要になる]{#automatic-maintenance explanation="自動設定で保守をなくすものではなく、カスタマイズしたシステムにも能動的な管理が必要です。"}
:::

## 性能と制御

Gentoo は性能や効率と結び付けられますが、より大きな利点は制御です。細部までシステムを形作れることが、小さな性能向上だけより重要です。

## Gentoo を使うべき人

詳細な設定を楽しみ、導入と保守に時間をかけられる上級者や意欲的な学習者に適します。穏やかな出発点には [Ubuntu](https://labex.io/lesson/ubuntu) や [Linux Mint](https://labex.io/lesson/linux-mint)、コンパイルを減らしつつ手を動かす体験には [Arch Linux](https://labex.io/lesson/arch-linux) が近い選択です。

## 関連資料

- [Gentoo](https://www.gentoo.org/)
- [Gentoo Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page)
- [Portage](https://wiki.gentoo.org/wiki/Portage)
- [USE フラグ](https://wiki.gentoo.org/wiki/USE_flag)

1. **[Linux コマンドのオンライン練習](https://labex.io/courses/linux-basic-commands-practice-online)** - 手を動かす Linux 作業に必要なコマンドライン習慣を伸ばします。
2. **[シェルスクリプトの基礎](https://labex.io/courses/shell-scripting-fundamentals)** - シェル自動化を通じて環境をより制御します。
3. **[ジュニアシステム管理者になる](https://labex.io/courses/become-a-junior-system-administrator)** - Linux 管理の幅広い基礎を築きます。

## まとめ

Gentoo が利便性と引き換えに Linux システムの細かな制御を提供する理由を説明できるようになりました。

1. Gentoo が対象とする利用者を見分ける。
2. Portage を Gentoo のパッケージマネージャーとして特定する。
3. USE フラグが任意のパッケージ機能をどう制御するか説明する。
4. ソースベースのカスタマイズのトレードオフを説明する。
