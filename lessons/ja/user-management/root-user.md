---
lesson_id: "root-user"
course_id: "user-management"
lang: "ja"
order_index: 2
title: "ルート"
description: "su、sudo、sudoers ポリシーが、特権を持つ識別情報への制御されたアクセスを提供する仕組みを学びます。"
meta_title: "ルート - ユーザー管理"
meta_description: "Linux における root ユーザーの役割を探ります。このレッスンでは、スーパーユーザー権限を取得するための su と sudo の違い、および/etc/sudoers ファイルがアクセスを管理する方法について解説します。"
meta_keywords: "linux root ユーザー, linux root, su, sudo, sudoers, visudo, スーパーユーザー, ユーザー管理，linux 権限"
---

伝統的に `root` と呼ばれるアカウントは UID 0 を持ち、そのセキュリティコンテキスト内で広範な権限を持ちます。日常作業には非特権アカウントを使い、理解している特定の管理目的に限って権限を昇格してください。

## su で別ユーザーのシェルを開始する

substitute user を意味する `su` は、別アカウントの識別情報でシェルまたはコマンドを開始します。ユーザー名を省略すると、既定の対象は root です。

```bash
$ su
```

認証は PAM とローカルポリシーによって制御されます。対象アカウントのパスワードを求める、`su` を使えるユーザーを制限する、root パスワードをロックしたままにするといった設定があり得ます。パスワードを知っていることだけが条件だと考えてはいけません。

単なる `su` は識別情報を変更しつつ、現在の環境を多く残します。`su - USER`、または `su --login USER` はログイン形式のシェルを開始し、対象アカウントの新規ログインに近い環境を初期化します。

```bash
$ su - operator
```

対象固有の作業が終わったら、サブシェルを終了します。

:::single-choice{#root-su-login-shell}
ユーザー `operator` としてログイン形式のシェルを要求するコマンドはどれですか？

::option[`su - operator`]{#root-su-login-operator .correct explanation="ハイフンは、`operator` 用のログインシェル動作と対象指向の環境を要求します。"}
::option[`su operator`]{#root-su-preserve-environment explanation="これは対象の識別情報へ変更しますが、ここで紹介した完全なログイン形式の初期化は要求しません。"}
::option[`sudo -l operator`]{#root-sudo-list-operator explanation="`sudo -l` はポリシーで許可されたコマンドを一覧表示し、要求されたログインシェルは開始しません。"}
:::

## sudo で特定のコマンドを実行する

`sudo COMMAND` は、一つのコマンドを対象ユーザーとして実行するため、ポリシーによる認可を要求します。既定の対象は通常 root です。別の対象には `-u USER` を使います。

```bash
$ sudo -u postgres id
```

要求が許可されるとは限りません。sudo ポリシーは、呼び出し元ユーザー、ホスト、対象識別情報、コマンドなどの条件を制御します。設定によって、呼び出し元ユーザーのパスワード、別の仕組み、またはプロンプトなしの認証が使われます。

可能なら、長時間続く特権シェルではなく、範囲を絞った一つの管理コマンドを選びます。範囲が小さければ、誤ったコマンドを昇格権限で実行する可能性も減ります。

:::single-choice{#root-sudo-target-user}
`sudo -u postgres id` は何を要求しますか？

::option[現在のアカウントを `postgres` へ恒久的に改名する。]{#root-sudo-rename explanation="`sudo` は対象の資格情報でコマンドを実行しますが、アカウント記録を改名しません。"}
::option[ポリシーに従い、`postgres` を対象ユーザーとして `id` を実行する。]{#root-sudo-postgres-id .correct explanation="`-u` オプションが対象識別情報を選び、sudoers ポリシーが要求を許可するか決めます。"}
::option[現在のユーザーより UID が大きい全ユーザーを一覧表示する。]{#root-sudo-list-uids explanation="`id` コマンドは自身のプロセスの識別情報を報告し、この構文でアカウント UID を列挙することはありません。"}
:::

## 特権シェルを維持しない

`su -`、`sudo -s`、`sudo -i` などのコマンドは、ポリシーで許可されていれば特権シェルを作成できます。そのシェルを終了するまで、それ以降のすべてのコマンドが昇格した影響を持ち得ます。パスの誤り、未確認のスクリプト、シェル展開の危険性が高まります。

監査動作は設定によって異なります。`sudo` は一般に呼び出しを記録しますが、シェル起動が一度記録されても、その中で入力した全コマンドが自動的に完全記録されるとは限りません。シェル履歴、システム監査、sudo の I/O ログは、それぞれ独立した仕組みとポリシーを持ちます。

:::single-choice{#root-persistent-shell-risk}
長時間維持する root シェルが、理解したコマンドを一つずつ昇格するより危険なのはなぜですか？

::option[root シェルがすべての監査システムから全コマンドを自動削除するから。]{#root-shell-no-audit explanation="ログ記録は設定によって異なり、全監査記録が自動的に消えるという説明は不正確です。"}
::option[シェルが複数要素から成るファイルパスを無効にするから。]{#root-shell-path-limit explanation="特権によってそのようなパス制限は生じません。問題は通常操作へ適用される権限の大きさです。"}
::option[シェルを終了するまで、後続コマンドが昇格した影響を持ち続けるから。]{#root-shell-elevated-scope .correct explanation="特権識別情報を維持すると、入力ミスや信頼できないコマンドが保護資源を変更できる時間が広がります。"}
:::

## sudo の認可を確認する

現在のアカウントが有効なポリシーの下で要求できる内容は、`sudo -l` で一覧表示します。

```bash
$ sudo -l
```

コマンドパス、許可された対象ユーザー、引数の制限を確認します。広範に見えるルールも、無関係な作業を許可するものとして扱ってはいけません。

:::single-choice{#root-list-sudo-rules}
現在の呼び出し元ユーザーが利用できる sudo 権限を一覧表示するコマンドはどれですか？

::option[`sudo -i`]{#root-sudo-login explanation="これは対象のログイン形式シェルを要求し、権限範囲を広げる可能性があります。読み取り専用のポリシー一覧ではありません。"}
::option[`sudo -l`]{#root-sudo-list .correct explanation="小文字の `-l` オプションは、現在のポリシーで許可されたコマンドの一覧を sudo へ要求します。"}
::option[`su -l`]{#root-su-login-default explanation="これは sudo の認可一覧ではなく、`su` のログインシェル動作を呼び出します。"}
:::

## sudoers ポリシーを安全に編集する

既定の sudo ポリシーは一般に `/etc/sudoers` を読み、`/etc/sudoers.d/` 以下のファイルを含める場合があります。別のポリシーソースもあり得ます。構文は、単純なユーザーとグループの一覧より多くの内容を制御します。

`visudo` はファイルをロックし、インストール前に構文を検証するため、ポリシー変更にはこのツールを使います。

```bash
$ sudo visudo
```

追加ファイルには正確なパスを指定します。

```bash
$ sudo visudo -f /etc/sudoers.d/application-admins
```

通常のリダイレクトや検証のないエディター手順で sudoers を編集してはいけません。構文や権限の誤りで管理アクセスを失う可能性があります。リモートの認可設定を変更するときは、検証済みの別の復旧経路を確保してください。

:::single-choice{#root-edit-sudoers-safely}
主要な sudoers ポリシーを編集し、構文を確認するために使うべきツールはどれですか？

::option[`cat`]{#root-cat-sudoers explanation="`cat` は読み取り可能なテキストを表示できますが、sudoers を安全に編集、ロック、検証しません。"}
::option[`visudo`]{#root-visudo .correct explanation="`visudo` は sudoers ポリシーの変更用に、ロックと構文検証を提供します。"}
::option[`echo` と `>`]{#root-echo-sudoers explanation="シェルリダイレクトはポリシーを直ちに切り詰める可能性があり、sudoers の構文検証も行いません。"}
:::

管理された環境で権限委任を練習するには、次のハンズオンラボを利用してください。

1. **[Linux でユーザーアカウントと sudo 権限を設定する](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - パスワードポリシーの適用、アカウントのロックと解除、root アカウントの保護、管理権限の付与を練習します。

## まとめ

識別情報の切り替えと、ポリシーで制御されたコマンド委任を区別できるようになりました。

1. 対象のログインシェルが必要な場合だけ `su - USER` を使う。
2. `-u USER` で特定の sudo 対象を要求する。
3. 特権シェル内で過ごす時間を最小限にする。
4. `sudo -l` で有効な sudo ルールを確認する。
5. sudoers ポリシーは `visudo` だけで編集する。
