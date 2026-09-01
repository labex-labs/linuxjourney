---
lesson_id: "filesystem-hierarchy"
course_id: "filesystem"
lang: "ja"
order_index: 1
title: "ファイルシステム階層"
description: "Linux の主要ディレクトリが意図する役割と、現代の統合された構成が異なる場合を学びます。"
meta_title: "ファイルシステム階層 - ファイルシステム"
meta_description: "標準的な Linux ファイルシステム階層（FSH）を探求します。このガイドでは、/bin、/etc、/home、/var などの主要なディレクトリの目的を説明し、Linux におけるファイルシステム階層の明確な概要を提供します。"
meta_keywords: "Linux ファイルシステム階層，Linux のファイルシステム階層，Linux ファイル階層構造，Linux ファイル階層，FSH, Linux ディレクトリ構造"
---

Linux は、マウントしたファイルシステムを `/` を根とする1つのディレクトリツリーとして示します。Filesystem Hierarchy Standard（FHS）は多くのディレクトリへ慣例的な役割を与えますが、ディストリビューション、コンテナ、immutable システム、ローカル方針で異なる場合があります。パスを前提にする前に実際のホストを調べてください。

```bash
$ ls -ld /*
```

## ルートと必須システムパス

- `/`：見えるファイルシステムツリーのルート。
- `/etc`：ホスト固有のシステム設定。実行可能な補助・起動スクリプトを含む場合があり、実行可能内容を一切含まないという説明は不正確。
- `/boot`：ブートローダーデータ、多くのシステムではカーネルと初期 RAM ファイルシステムイメージなど、起動関連ファイル。
- `/bin` と `/sbin`：従来、必須のユーザー用・システム管理用コマンド。
- `/lib` とアーキテクチャ固有の派生パス：従来、必須の共有ライブラリとローダー部品。

現在の多くのディストリビューションは merged `/usr` 構成を使い、`/bin`、`/sbin`、`/lib` が対応する `/usr` 内ディレクトリへのシンボリックリンクです。物理ディレクトリかリンクかを決め付けず、コマンド検索とパッケージ記録を使ってください。

:::single-choice{#filesystem-hierarchy-configuration-directory} ホスト固有のシステム設定を慣例的に含むディレクトリはどれですか？

::option[`/proc`]{#filesystem-hierarchy-proc-config explanation="procfs は永続的なホスト設定ではなく、実行中のプロセスとカーネルのインターフェースを示します。"}
::option[`/etc`]{#filesystem-hierarchy-etc .correct explanation="システムとサービスの設定は慣例上 /etc の下に整理されます。"}
::option[`/dev`]{#filesystem-hierarchy-dev-config explanation="/dev は実行時のデバイス向けオブジェクトを含み、一般設定階層ではありません。"}
:::

## ディストリビューションとローカルソフトウェア

- `/usr`：コマンド、ライブラリ、アーキテクチャ非依存データなど、共有可能でほぼ読み取り専用の OS・アプリケーション階層。
- `/usr/local`：ディストリビューションの通常の `/usr` 管理外で、ローカル管理者が導入するソフトウェアとデータ。
- `/opt`：自己完結したサブツリーとして追加アプリケーションパッケージを置ける場所。

名前に反して `/usr` は個々の利用者の個人ファイル用ではありません。大部分をパッケージマネージャーが所有するため、ローカルでコンパイルしたファイルを `/usr/bin` へコピーすると管理パッケージと競合できます。

:::single-choice{#filesystem-hierarchy-local-software} ディストリビューション管理の `/usr` 外で、ローカル導入ソフトウェア用に予約された接頭辞はどれですか？

::option[`/usr/local`]{#filesystem-hierarchy-usr-local .correct explanation="ローカル階層は管理者導入ソフトウェアをディストリビューションの主な /usr ツリーから分離します。"}
::option[`/proc/local`]{#filesystem-hierarchy-proc-local explanation="procfs は仮想カーネルインターフェースで、永続ソフトウェア用接頭辞ではありません。"}
::option[`/dev/local`]{#filesystem-hierarchy-dev-local explanation="デバイスノードの場所はローカルアプリケーション用ではありません。"}
:::

## ユーザーとサービスのデータ

- `/home`：慣例上、root 以外のユーザーのホーム。ディレクトリサービスやローカル方針で別の場所にも置ける。
- `/root`：root アカウントの慣例的なホーム。
- `/srv`：このシステムが提供するサイト固有データ。

ホームパスは単に `/home` とユーザー名を結合せず、アカウント情報から得ます。`getent passwd USER` またはシェルが解決したホームを使ってください。

:::single-choice{#filesystem-hierarchy-root-home} root アカウントの慣例的なホームディレクトリはどれですか？

::option[`/home/root`]{#filesystem-hierarchy-home-root explanation="通常ユーザーのホームは /home 下が一般的ですが、root には別の慣例的パスがあります。"}
::option[`/root`]{#filesystem-hierarchy-root .correct explanation="特権アカウントのホームは慣例上、ファイルシステムルートの直下です。"}
::option[`/usr/root`]{#filesystem-hierarchy-usr-root explanation="/usr はソフトウェアと共有データの階層で、root のホームではありません。"}
:::

## 可変、実行時、一時データ

- `/var`：ログ、キャッシュ、スプール、アプリケーション状態などの可変データ。ログは一般に `/var/log` だが、主に journal を使うシステムもある。
- `/run`：ソケット、サービス状態、PID ファイルなど、現在の起動に対する揮発性の実行時状態。通常は起動時に再作成。
- `/tmp`：一時ファイル。sticky bit 保護付きで全ユーザーが書き込めることが一般的。
- `/var/tmp`：`/tmp` より長く残すべき一時ファイル。

`/tmp` の整理方針は環境ごとに異なり、再起動まで必ず残る、または再起動時に必ず消えるとは限りません。アプリケーションは予測可能な名前を避け、安全な一時ファイル作成方法を使います。

:::single-choice{#filesystem-hierarchy-log-path} システムログファイルを慣例的に保存するパスはどれですか？

::option[`/etc/log`]{#filesystem-hierarchy-etc-log explanation="/etc は通常、増え続けるログではなく設定用です。"}
::option[`/var/log`]{#filesystem-hierarchy-var-log .correct explanation="ログは変化するシステムデータで、可変データ階層の下に整理されます。"}
::option[`/boot/log`]{#filesystem-hierarchy-boot-log explanation="/boot は一般サービスログではなく、起動関連の成果物用です。"}
:::

## デバイス、カーネルインターフェース、マウントポイント

- `/dev`：デバイスノードと関連する実行時リンク。
- `/proc`：procfs を通じたプロセスとカーネルのインターフェース。
- `/sys`：sysfs を通じたカーネルオブジェクト、デバイス、ドライバー、属性。
- `/media`：自動マウントされるリムーバブルメディアによく使う。
- `/mnt`：管理者の一時マウントに使う慣例的な場所。

これらは慣例で、権限を付与するものではありません。空でないディレクトリへ別ファイルシステムをマウントすると、アンマウントまで元の内容が一時的に隠れます。

:::single-choice{#filesystem-hierarchy-sysfs-path} sysfs を通じてカーネルのデバイスモデルを通常公開するパスはどれですか？

::option[`/srv`]{#filesystem-hierarchy-srv explanation="/srv はシステムが提供するデータ用です。"}
::option[`/sys`]{#filesystem-hierarchy-sys .correct explanation="sysfs は通常 /sys にマウントされ、デバイス、ドライバー、バス、属性を示します。"}
::option[`/opt`]{#filesystem-hierarchy-opt explanation="/opt は追加アプリケーションのツリー用です。"}
:::

[Linux でファイルシステムを移動する](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971) でこれらのパスを調べ、[Linux でファイルとコマンドを探す](https://labex.io/labs/comptia-find-files-and-commands-in-linux-590834) で推測した場所に頼らない方法を練習できます。

## まとめ

実システムの違いを考慮しながら、主要な Linux パスを意図された役割へ関連付けられるようになりました。

1. `/` を根とする統一ツリーから始める。
2. 設定、管理ソフトウェア、ローカルソフトウェア、可変データを分ける。
3. ホームとサービスデータを実行時状態から区別する。
4. `/dev`、`/proc`、`/sys` を特別な実行時インターフェースとして理解する。
5. 構成を決め付ける前に、リンク、マウント、アカウント情報、ディストリビューション方針を調べる。
