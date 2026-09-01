---
lesson_id: "etc-group-file"
course_id: "user-management"
lang: "ja"
order_index: 5
title: "/etc/group"
description: "ローカルのグループレコードが名前を GID に対応付け、補助メンバーを列挙する仕組みを学びます。"
meta_title: "/etc/group - ユーザー管理"
meta_description: "Linux の/etc/group ファイルを調査し、グループ管理を理解します。cat /etc/groupでグループデータを表示する方法を学び、GIDやユーザーリストを含む構造を理解します。このガイドでは、etc group linux ファイルの基本を網羅します。"
meta_keywords: "/etc/group, /etc/group linux, /etc/group ファイル linux, cat /etc/group, etc group linux, グループ管理，GID, Linux 権限，Linux グループ"
---

`/etc/group` はローカルのグループレコードを保存します。グループ名を数値 GID に対応付け、明示的なメンバーを列挙することで、複数アカウントが共有するアクセス制御を支えます。

## ローカルグループと解決済みグループ

このファイルは、グループ情報源の一つにすぎません。NSS はローカルファイル、ディレクトリサービスなど、設定されたデータベースからグループを解決できます。ローカルレコードは次のように表示します。

```bash
$ cat /etc/group
```

解決済みグループデータベースは `getent` で問い合わせます。

```bash
$ getent group
$ getent group developers
```

グループ一覧は内部のアカウント名や役割名を開示する場合があるため、共有前に出力を確認してください。

:::single-choice{#group-query-resolved-database} NSS が解決するグループデータベースを問い合わせるコマンドはどれですか？

::option[`getent group`]{#group-getent-all .correct explanation="`getent` は設定済みの NSS 情報源からグループレコードを参照します。"}
::option[`cat /etc/group`]{#group-cat-local explanation="これはローカルのグループファイルだけを読み、別の情報源が提供するグループを省く場合があります。"}
::option[`groups /etc/group`]{#group-groups-file explanation="`groups` はユーザー名を受け取り所属を報告するもので、ローカルデータベースのパス名を NSS 問い合わせとして扱いません。"}
:::

## 4個のフィールドを読む

ローカルレコードには、コロンで区切られた4個のフィールドがあります。

```text
developers:x:1500:alice,bob
```

1. **グループ名**: `developers`。
2. **パスワードフィールド**: 一般に `x`、`*` などのプレースホルダー。保護されたグループパスワードデータは `/etc/gshadow` に保存できます。
3. **GID**: 数値のグループ識別情報。この例では `1500`。
4. **メンバー一覧**: コンマ区切りの明示的なメンバー名。この例では `alice` と `bob`。

グループパスワードは、一部の構成で `newgrp` などが使う従来の機能です。sudo の認可を与える通常の仕組みではなく、フィールドの手動編集で導入すべきでもありません。

:::single-choice{#group-gid-field} `developers:x:1500:alice,bob` で GID を含むフィールドはどれですか？

::option[第2フィールドの `x`]{#group-second-password explanation="第2フィールドはグループパスワードのプレースホルダーであり、数値の識別情報ではありません。"}
::option[第4フィールドの `alice,bob`]{#group-fourth-members explanation="第4フィールドは GID ではなく、明示的なメンバー名を列挙します。"}
::option[第3フィールドの `1500`]{#group-third-gid .correct explanation="コロンで区切られた第3フィールドが数値のグループ ID です。"}
:::

:::single-choice{#group-explicit-member-field} ローカルグループレコードで、明示的なメンバー名はどのように表されますか？

::option[第4フィールドのコンマ区切り一覧。]{#group-members-field-four .correct explanation="最後のフィールドに、明示的な補助メンバー名をコンマで区切って記録します。"}
::option[第2フィールドの空白区切り一覧。]{#group-members-field-two explanation="第2フィールドはパスワード関連データまたはプレースホルダー用で、メンバー一覧ではありません。"}
::option[グループ名に埋め込まれた数値 UID。]{#group-members-in-name explanation="グループ名とメンバー名は別々のフィールドで、通常のメンバー項目はログイン名であり、埋め込まれた UID 数字ではありません。"}
:::

## プライマリグループ所属を考慮する

`/etc/group` のメンバー一覧には通常、passwd レコードでその GID をプライマリグループとして指定しているユーザーを重ねて記録しません。そのため、第4フィールドに名前がなくても、そのユーザーがグループメンバーである場合があります。

たとえば、Alice の passwd レコードでプライマリ GID が1500なら、ローカルグループレコードのメンバーフィールドが空でも、Alice は `developers` に所属します。

```text
developers:x:1500:
```

したがって、第4フィールドだけを解析すると、所属関係を完全には把握できません。

:::single-choice{#group-primary-membership-visibility} Alice の passwd レコードでは GID 1500 がプライマリ GID ですが、グループ1500の第4フィールドに名前がありません。Alice はそのグループのメンバーですか？

::option[いいえ。すべての所属は `/etc/group` の第4フィールドに現れなければならない。]{#group-field-four-only explanation="これはプライマリ GID による所属を無視し、グループメンバーを少なく数えてしまいます。"}
::option[はい。プライマリ所属は passwd レコードの GID フィールドから得られる。]{#group-primary-from-passwd .correct explanation="グループファイルの明示的な一覧は主に補助所属用で、プライマリ所属はアカウント側に記録されます。"}
::option[グループパスワードフィールドに Alice のユーザー名がある場合だけ。]{#group-password-member explanation="パスワードフィールドはプライマリ所属の宣言とは無関係です。"}
:::

## ユーザーのグループを確認する

解決済みアカウントのビューには `id USER` または `groups USER` を使います。

```bash
$ id alice
$ groups alice
```

現在のプロセスについては、引数なしの `id` が資格情報に実際に含まれるグループを報告します。新しく設定した補助グループ所属は通常、すでに実行中のログインセッションには現れません。新しい認証済みセッションを開始するか、必要に応じて意図的に設定した `newgrp` などの仕組みを使います。

:::single-choice{#group-current-process-credentials} 現在のプロセスの UID、プライマリ GID、補助グループを報告するコマンドはどれですか？

::option[`id`]{#group-current-id .correct explanation="ユーザー引数なしの `id` は、現在のプロセスの識別資格情報を報告します。"}
::option[`cat /etc/group`]{#group-current-cat explanation="ローカルファイルはレコードを一覧表示しますが、現在のプロセスでどの解決済みグループが有効かは示しません。"}
::option[`getent passwd`]{#group-current-passwd explanation="これはアカウントレコードを問い合わせますが、現在のプロセスの補助グループ一覧を特に報告するものではありません。"}
:::

## ローカルグループを安全に変更する

汎用エディターでレコードを編集せず、`groupadd`、`groupmod`、`groupdel`、`gpasswd`、`usermod` などのツールを使います。特に次の違いに注意してください。

- `usermod -aG GROUP USER`: 補助グループ所属を追加します。
- `usermod -G ...`: `-a` を省略すると、補助グループ一覧を置き換えます。

ローカルデータベースの手動修復が避けられない場合は、`vigr` でロックし、`grpck` で検証します。リモートの識別情報を変更する前に、復旧経路を確保してください。

管理された環境でローカルグループ管理を練習するには、次のハンズオンラボを利用できます。

1. **[useradd、usermod、userdel で Linux ユーザーアカウントを管理する](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 新規アカウントの作成と保護から変更、削除まで、ユーザー管理のライフサイクル全体を練習します。
2. **[groupadd、usermod、groupdel で Linux グループを管理する](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - `groupadd`、`usermod`、`groupdel` など、グループ管理の主要なコマンドラインユーティリティーを実践します。
3. **[新しいユーザーとグループを追加する](https://labex.io/labs/linux-add-new-user-and-group-17987)** - 新規ユーザーアカウントとカスタムグループを作成し、所属を管理することで、サーバー環境へ新しいメンバーを追加する状況を模擬します。

## まとめ

ローカルグループレコードを解釈し、完全な所属関係をより正確に解決できるようになりました。

1. `getent group` で設定済みのグループ情報源を問い合わせる。
2. コロンで区切られた4個のグループフィールドを読む。
3. 数値 GID と明示的なメンバー一覧を特定する。
4. passwd レコードから得られるプライマリ所属を含める。
5. 変更した所属に依存する前に、有効な資格情報を確認する。
