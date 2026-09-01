---
lesson_id: "boot-process-bootloader"
course_id: "boot-system"
lang: "ja"
order_index: 3
title: "ブートプロセス：ブートローダー"
description: "ブートローダーが Linux の起動成果物を選び、カーネルコマンドラインを構築して制御を渡す仕組みを学びます。"
meta_title: "ブートプロセス：ブートローダー - システムの起動"
meta_description: "Linux におけるブートローダーのガイド。Linux ブートローダーとは何か、その主な機能、GRUB が initrd や root などのカーネルパラメータを使用してシステムを起動する方法を学びます。"
meta_keywords: "linux ブートローダー, linux ブートローダー, linux ブートローダー, grub, linux ブートローダーとは，カーネルパラメータ，initrd, root ファイルシステム，linux ブートプロセス"
---

ブートローダーは、ファームウェアによる検出とカーネル実行を橋渡しします。Linux PC では GRUB が一般的ですが、systemd-boot、U-Boot、ファームウェアによる EFI stub カーネルの直接読み込みなど、別の設計はこの役割の異なる部分を実装します。

## ブート成果物の選択

ローダーのエントリでは、次のものを指定できます。

- Linux カーネルイメージ
- 任意の initramfs または従来型 initrd イメージ
- カーネルコマンドライン
- プラットフォーム固有のメタデータや、別 OS のローダー

GRUB は複数のカーネルや復旧エントリを提示できます。予備カーネルが役立つのは、対応するモジュールと initramfs が残り、動作確認されている場合だけです。ローダーは自身が対応するストレージ・ファイルシステムモジュールを通じてファイルを読み、まだ動いていない Linux VFS には依存しません。

:::single-choice{#bootloader-primary-handoff} Linux のブートローダーは通常、何へ制御を渡しますか？

::option[全サービスが起動済みの対話型ユーザーシェル。]{#bootloader-user-shell explanation="ユーザー空間のシェルは、カーネルと init システムが起動した後に現れます。"}
::option[必要なブート成果物を読み込んだ後の、選択済みカーネルイメージ。]{#bootloader-selected-kernel .correct explanation="ローダーはカーネル、パラメータ、多くの場合 initramfs を準備し、カーネルのエントリポイントを実行します。"}
::option[依存関係を解決するファイルシステムのパッケージマネージャー。]{#bootloader-package-manager explanation="パッケージ管理は、ブート時に次にプロセッサ制御を受け取る段階ではありません。"}
:::

## カーネルコマンドラインパラメータ

ローダーは、カーネルと初期ユーザー空間が解析するテキストのコマンドラインを渡します。代表例は次のとおりです。

- `root=...`：最終的に使うルートファイルシステム、または初期ユーザー空間向けの指定を識別する
- `ro` / `rw`：ルートの初期マウントモードを要求する
- `quiet`：カーネルのコンソールメッセージを減らす
- `init=...`：特殊な復旧向けに別の最初のユーザー空間プログラムを要求する
- ディストリビューション固有の initramfs ツールが解釈する `rd.*` パラメータ

`initrd` は通常、イメージを指定するローダー指令であり、一般的なカーネルパラメータではありません。一部の GRUB 設定が生成するコマンドラインに `BOOT_IMAGE=` が現れることはありますが、カーネルを読み込む仕組みそのものではありません。

現在のブートで使われたコマンドラインは次で確認できます。

```bash
$ cat /proc/cmdline
```

:::single-choice{#bootloader-root-parameter} カーネルコマンドラインの `root=` パラメータは何のために使いますか？

::option[ブートが最終的に使うルートファイルシステムを識別する。]{#bootloader-root-filesystem .correct explanation="カーネルまたは initramfs がこの値を解釈し、実際のルートの検出と構築に使います。"}
::option[root アカウントのログインパスワードを設定する。]{#bootloader-root-password explanation="認証用の秘密情報を通常のカーネルコマンドラインへ渡してはいけません。"}
::option[PID 1 の名前を `root` に変更する。]{#bootloader-root-pid explanation="プロセス名はこのストレージパラメータと無関係です。"}
:::

:::single-choice{#bootloader-quiet-parameter} `quiet` パラメータは通常、何を要求しますか？

::option[マウント済み全ファイルシステムを読み取り専用にする。]{#bootloader-quiet-readonly explanation="ルートの初期書き込み方針には `ro` などを使い、`quiet` は使いません。"}
::option[ブート中に表示されるカーネルメッセージを減らす。]{#bootloader-quiet-console .correct explanation="多くの情報メッセージを抑制しますが、全ブートコンポーネントの完全な無表示を保証するものではありません。"}
::option[ハードウェアの全冷却ファンを無効にする。]{#bootloader-quiet-fans explanation="このパラメータが扱うのはメッセージ量であり、ハードウェアの動作音ではありません。"}
:::

## 一時編集と復旧

GRUB では、権限のあるコンソール利用者が、メニューに示された編集キーなどを使って一回のブートだけエントリを変更できるのが一般的です。`quiet` の削除、復旧パラメータの選択、誤ったルート識別子の修正に便利です。操作方法と認証は、Secure Boot やパスワード保護された GRUB 設定によっても異なります。

コマンドラインの機密文字列は `/proc/cmdline`、ブートログ、クラッシュ報告に露出し得ます。また、パラメータによってセキュリティを弱めたり、起動不能にしたりもできます。秘密情報は置かず、既知の正常なエントリとコンソールからの復旧手段を維持してください。

:::single-choice{#bootloader-temporary-edit} GRUB メニューのエントリを対話的に編集して一度ブートするとき、一般的に当てはまるものはどれですか？

::option[インストール済みの全カーネルイメージを自動的に書き換える。]{#bootloader-rewrites-kernels explanation="コマンド文字列を変えても、カーネルのバイナリは変更されません。"}
::option[全ディスクのファームウェア検証を恒久的に無効にする。]{#bootloader-disables-firmware explanation="ファームウェアポリシーは別の層であり、一つのエントリ編集で一律に変更されるものではありません。"}
::option[別途設定へ保存しない限り、変更はそのブートだけに適用される。]{#bootloader-one-boot-change .correct explanation="メニュー編集は通常、永続的な設定元ではなく、メモリ上のエントリだけを変更します。"}
:::

## GRUB の永続設定

ディストリビューションは一般に、テンプレート、既定値、スクリプト、検出したカーネルから最終的な GRUB 設定を生成します。ディストリビューションが明示的にその手順を定めていない限り、生成済み `grub.cfg` を直接編集しないでください。再生成によって上書きされる可能性があります。

対象を絞って設定元を変更し、ディストリビューション指定の再生成コマンドを実行して出力を確認します。既知の正常な旧エントリと起動可能な復旧メディアを残したままテストしてください。Debian、Fedora、UEFI、BIOS の各環境では、コマンドと出力先が異なります。

:::single-choice{#bootloader-generated-config} 生成済みの `grub.cfg` を直接編集する方法が通常は信頼できないのはなぜですか？

::option[ファイルの内容は決して読めるテキストではないから。]{#bootloader-config-binary explanation="GRUB の設定はテキストですが、生成物であることが重要です。"}
::option[GRUB は各ユーザーのホームディレクトリにあるファイルしか読まないから。]{#bootloader-grub-home explanation="ブート設定はシステム全体のもので、ユーザーのホームセッションより前に利用できる必要があります。"}
::option[後の再生成によって手動変更が上書きされるから。]{#bootloader-regeneration-overwrites .correct explanation="永続設定は通常、ディストリビューションの設定元と生成手順で管理します。"}
:::

[GRUB2 ブートメニューのカスタマイズ](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)は、復旧可能なラボ環境だけで利用してください。

## まとめ

これで、ローダー指令とカーネルコマンドラインパラメータを区別できます。

1. カーネル、initramfs、コマンドライン、代替エントリを識別する。
2. `root=`、`ro`、`quiet` を実際の役割に沿って使う。
3. `/proc/cmdline` から稼働中ブートのパラメータを確認する。
4. 対話的な編集を一時的かつセキュリティに関わる操作として扱う。
5. 永続的な生成設定はディストリビューションの手順で変更する。
