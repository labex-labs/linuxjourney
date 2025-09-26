---
index: 2
lang: "ja"
title: "syslog"
meta_title: "syslog - ロギング"
meta_description: "Linux の syslog と rsyslog について学び、システムログの管理方法、および logger コマンドの使用方法を習得します。この初心者向けのチュートリアルを始めましょう！"
meta_keywords: "syslog, rsyslog, Linux ログ，logger コマンド，/var/log/syslog, Linux チュートリアル，初心者 Linux, システムロギング"
---

## Lesson Content

syslog サービスは、システムロガーにログを管理し送信します。Rsyslog は syslog の高度なバージョンであり、ほとんどの Linux ディストリビューションでこの新しいバージョンが使用されているはずです。syslog サービスが収集するすべてのログの出力は、`/var/log/syslog`（認証メッセージを除くすべてのメッセージ）で見つけることができます。

システムロガーによって維持されているファイルを確認するには、`/etc/rsyslog.d`内の設定ファイルを見てください。

```plaintext
pete@icebox:~$ less /etc/rsyslog.d/50-default.conf
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log
```

ログファイルに対するこれらのルールは、左側のセレクターと右側のアクションによって示されます。アクションは、ログ情報をどこに送信するか（ファイル、コンソールなど）を教えてくれます。すべてのアプリケーションやサービスがログの管理に rsyslog を使用しているわけではないため、具体的に何がログに記録されているかを知りたい場合は、このディレクトリの中を確認する必要があります。

実際にロギングがどのように機能するかを見てみましょう。`logger`コマンドを使用して手動でログを送信できます。

```bash
logger -s Hello
```

次に`/var/log/syslog`の中を見ると、ログにこのエントリが表示されるはずです。

## Exercise

練習あるのみです！Linux ロギングとファイル表示に関する理解を深めるための実践的なラボをいくつかご紹介します。

1. **[Linux でのログファイルと設定ファイルの表示](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - システムログや設定ファイルを含むテキストファイルを効率的に表示および移動するための、不可欠な Linux コマンドラインスキルを練習します。
2. **[Linux tail コマンド：ファイル末尾の表示](https://labex.io/ja/labs/linux-linux-tail-command-file-end-display-214303)** - テキストファイルの末尾を表示および監視するための Linux `tail`コマンドを学習します。これはリアルタイムのログ分析に特に役立ちます。
3. **[Linux で grep を使用してテキストを検索](https://labex.io/ja/labs/comptia-search-text-with-grep-in-linux-590841)** - ファイル内の特定のテキストパターンを検索する方法を学習します。これは、ログエントリをふるいにかけて重要な情報を見つけるための非常に貴重なスキルです。

これらのラボは、ログ管理とファイル検査の概念を実際のシナリオに適用し、Linux システム管理への自信を築くのに役立ちます。

## Quiz Question

メッセージを手動でログに記録するために使用できるコマンドは何ですか？

## Quiz Answer

logger
