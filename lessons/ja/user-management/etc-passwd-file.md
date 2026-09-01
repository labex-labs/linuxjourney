---
lesson_id: "etc-passwd-file"
course_id: "user-management"
lang: "ja"
order_index: 3
title: "/etc/passwd"
description: "ローカルの passwd レコードを読み、それを NSS が解決する完全なアカウントビューと区別する方法を学びます。"
meta_title: "/etc/passwd - ユーザー管理"
meta_description: "Linux における/etc/passwd ファイルに関する包括的なガイド。ユーザーデータフィールドの解釈方法、UID の理解、および root:x:0:0:root:/root:/bin/bash のような例を学びます。"
meta_keywords: "/etc/passwd, Linux の/etc/passwd, root:x:0:0:root:/root:/bin/bash, ユーザーID, UID, ユーザー管理，Linux チュートリアル"
---

`/etc/passwd` は、ローカルアカウントのレコードをコロン区切りのテキスト形式で保存します。ログイン名を数値 UID に対応付け、プライマリ GID、説明フィールド、ホームパス、ログインプログラムを記録します。

## ローカルレコードと解決済みアカウント

ローカルファイルは読み取り専用コマンドで表示します。

```bash
$ cat /etc/passwd
```

ここにあるのが、システムに認識されるすべてのアカウントとは限りません。Name Service Switch（NSS）は、ファイル、ディレクトリサービス、システムデータベースなど、設定された複数の情報源からアカウントを解決できます。解決済みの passwd データベースを問い合わせるには `getent` を使います。

```bash
$ getent passwd
$ getent passwd root
```

最初のコマンドではアカウント名とメタデータが開示される可能性があるため、出力を公開する前に確認してください。

:::single-choice{#passwd-query-resolved-database} ローカルファイルだけを読むのではなく、NSS が解決する passwd データベースを問い合わせるコマンドはどれですか？

::option[`cat /etc/passwd`]{#passwd-cat-local explanation="これはローカルファイルだけを表示し、別の NSS 情報源だけが提供するアカウントは含みません。"}
::option[`cat /etc/shadow`]{#passwd-cat-shadow explanation="shadow ファイルには保護されたローカルのパスワード有効期限情報が含まれ、この目的で表示すべきではありません。"}
::option[`getent passwd`]{#passwd-getent-all .correct explanation="`getent` は NSS を通じて設定済みの passwd データベース情報源を参照します。"}
:::

## 7個のフィールドを読む

ローカルレコードは一般に次のような形式です。

```text
root:x:0:0:root:/root:/bin/bash
```

コロンで区切られた7個のフィールドは次のとおりです。

1. **ログイン名**: `root` など、人が読めるアカウント名。
2. **パスワードフィールド**: shadow パスワードを使うシステムでは通常 `x` で、保護されたパスワードデータが別に保存されることを示します。
3. **UID**: 数値のユーザー識別情報。UID 0 は伝統的にスーパーユーザーとして扱われます。
4. **プライマリ GID**: アカウントのプライマリグループを表す数値 ID。
5. **GECOS／コメント**: 説明用のアカウント情報。内部でコンマ区切りになることがあります。
6. **ホームディレクトリ**: アカウントのホーム設定として使われるパス。ディスク上に存在しない場合もあります。
7. **ログインシェル／プログラム**: 該当するログインセッションで要求される、`/bin/bash` やログインを許可しないプログラムなど。

不正な、または意図的に重複したレコードでは、カーネルが UID 値の一意性を強制するわけではありません。しかし、同じ UID を共有するアカウントは、多くの所有権と権限判断で区別できません。通常、管理者はアカウント UID を一意に保つべきです。

:::single-choice{#passwd-uid-field} `root:x:0:0:root:/root:/bin/bash` で UID を含むフィールドはどれですか？

::option[第2フィールドの `x`]{#passwd-second-password explanation="第2フィールドはパスワードのプレースホルダーであり、数値のユーザー識別情報ではありません。"}
::option[第4フィールドの2番目の `0`]{#passwd-fourth-gid explanation="第4フィールドは UID ではなくプライマリ GID です。"}
::option[第3フィールドの最初の `0`]{#passwd-third-uid .correct explanation="第3フィールドが UID なので、最初の0はこのレコードが UID 0 であることを示します。"}
:::

:::single-choice{#passwd-primary-gid-field} passwd レコードでアカウントのプライマリ GID を保存するフィールドはどれですか？

::option[第5フィールド]{#passwd-gecos-five explanation="第5フィールドは GECOS、つまりコメントフィールドです。"}
::option[第4フィールド]{#passwd-gid-four .correct explanation="コロン区切りの第4フィールドがプライマリグループを数値で識別します。"}
::option[第7フィールド]{#passwd-shell-seven explanation="第7フィールドはログインシェルまたはプログラムを指定します。"}
:::

## パスワードのプレースホルダーを解釈する

一般的な shadow パスワードシステムでは、第2フィールドの `x` によって、パスワードを扱うツールが `/etc/shadow` の保護データを参照します。`*` や `!` などの値は有効なパスワードハッシュではなく、通常、その項目を使う Unix パスワード認証を防ぎます。

ただし、あらゆる方法で認証できないことを証明するものではありません。SSH 鍵、証明書、トークン、サービス固有の仕組みは独立している場合があります。同様に、空のパスワードフィールドは認証スタックに依存するセキュリティ上重要な動作を持つため、手動で作成したり「修正」したりしてはいけません。

:::single-choice{#passwd-x-placeholder} ローカルの `/etc/passwd` レコードで、第2フィールドの `x` は一般に何を意味しますか？

::option[そのアカウントには認証方法が一切ないと保証される。]{#passwd-no-auth-guarantee explanation="このプレースホルダーはすべての認証方法を表さず、それ自体でアカウントが使用不能だという意味でもありません。"}
::option[アカウントのホームディレクトリが削除された。]{#passwd-home-deleted explanation="ホームディレクトリ情報は第6フィールドに保存され、`x` プレースホルダーとは無関係です。"}
::option[保護されたパスワードデータが shadow データベースに保存されている。]{#passwd-shadow-placeholder .correct explanation="公開 passwd レコードにはプレースホルダーを置き、パスワードハッシュと有効期限フィールドは保護された shadow データに保存します。"}
:::

## サービスアカウントを認識する

多くのレコードは人ではなくサービスを表します。サービスごとに識別情報を分けることで、ファイルとプロセスを一つのデーモンに必要な権限へ制限できます。ホームパスが標準的でない、または存在しない場合があり、ログインプログラムには `/usr/sbin/nologin`、`/bin/false` などの制限されたプログラムが使われることがあります。

ディストリビューションのポリシーを確認せず、UID の範囲だけからアカウントの用途を推測してはいけません。割り当て範囲は異なり、中央管理アカウントが別の慣習に従うこともあります。

:::single-choice{#passwd-nologin-shell} 第7フィールドで `/usr/sbin/nologin` のようなログインプログラムを指定する一般的な目的は何ですか？

::option[サービス停止時にアカウントのファイルを削除する。]{#passwd-nologin-delete explanation="ログインプログラムは所有データを自動削除せず、サービス停止時のファイルも管理しません。"}
::option[このフィールドを尊重するログイン経路から、通常の対話的シェルを開始できないようにする。]{#passwd-nologin-purpose .correct explanation="非ログインプログラムは、通常のログインで対話的シェルを与えるべきでないサービスアカウントによく使われます。"}
::option[アカウントへ UID 0 と同じ権限を与える。]{#passwd-nologin-root explanation="対話的ログインを制限しても、アカウントの権限や数値 UID は変わりません。"}
:::

## アカウントレコードを安全に変更する

`useradd`、`usermod`、`userdel` などのアカウント管理ツールを優先してください。関連レコードを調整し、システムの既定値を適用します。正確な動作はディストリビューションで設定可能なため、アカウントを変更する前にオプションを確認します。

ローカル passwd データベースを本当に手動修復する必要がある場合は、通常のエディターではなく `vipw` を使います。並行編集を避けるためのロックが適用されます。`pwck` などでデータベースを検証し、リモートから認証ファイルを変更する前には復旧用セッションを維持してください。

管理された環境でユーザーとグループのレコードを練習するには、次のハンズオンラボを利用できます。

1. **[useradd、usermod、userdel で Linux ユーザーアカウントを管理する](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 新規アカウントの作成と保護から変更、削除まで、ユーザー管理のライフサイクル全体を練習します。
2. **[groupadd、usermod、groupdel で Linux グループを管理する](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 新規グループの作成やユーザー所属の変更など、グループ管理の主要なコマンドラインユーティリティーを実践します。

## まとめ

ローカルの passwd レコードを、完全な識別情報データベースと誤認せずに解釈できるようになりました。

1. `getent passwd` で NSS が解決するアカウントを問い合わせる。
2. コロンで区切られた7個の passwd フィールドを読む。
3. UID とプライマリ GID のフィールドを特定する。
4. ログイン状態を過度に断定せず、パスワードプレースホルダーを解釈する。
5. 通常のエディターではなく、アカウント管理ツールまたは `vipw` を使う。
