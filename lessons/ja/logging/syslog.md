---
index: 2
lang: "ja"
title: "syslog"
meta_title: "syslog - ロギング"
meta_description: "Linux の syslog と rsyslog について学び、システムログを管理し、logger コマンドを使用する方法を学びます。この初心者向けのチュートリアルから始めましょう！"
meta_keywords: "syslog, rsyslog, Linux ログ，logger コマンド，/var/log/syslog, Linux チュートリアル，初心者 Linux, システムログ"
---

## Lesson Content

syslog サービスは、ログを管理し、システムロガーに送信します。Rsyslog は syslog の拡張バージョンであり、ほとんどの Linux ディストリビューションはこの新しいバージョンを使用しているはずです。syslog サービスが収集するすべてのログの出力は、`/var/log/syslog`（認証メッセージを除くすべてのメッセージ）にあります。

システムロガーによってどのファイルが管理されているかを確認するには、`/etc/rsyslog.d`にある設定ファイルを見てください。

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

これらのログファイルのルールは、左列のセレクターと右列のアクションによって示されます。アクションは、ログ情報をどこに送信するか（ファイル、コンソールなど）を示します。すべてのアプリケーションとサービスがログの管理に rsyslog を使用しているわけではないため、具体的に何がログに記録されているかを知りたい場合は、このディレクトリ内を確認する必要があります。

実際にログ記録の動作を見てみましょう。`logger`コマンドを使用して手動でログを送信できます。

```bash
logger -s Hello
```

これで`/var/log/syslog`の中を見ると、このエントリがログに表示されているはずです！

## Exercise

練習は完璧をもたらします！Linux のログ記録とファイル表示の理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux でのログファイルと設定ファイルの表示](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - システムログや設定ファイルを含むテキストファイルを効率的に表示およびナビゲートするための、Linux の基本的なコマンドラインスキルを練習します。
2. **[Linux tail コマンド：ファイルの末尾表示](https://labex.io/ja/labs/linux-linux-tail-command-file-end-display-214303)** - テキストファイルの末尾を表示および監視するための Linux `tail`コマンドを学習します。これはリアルタイムのログ分析に特に役立ちます。
3. **[Linux で grep を使ってテキストを検索する](https://labex.io/ja/labs/comptia-search-text-with-grep-in-linux-590841)** - ファイル内の特定のテキストパターンを検索する方法を学習します。これは、重要な情報を見つけるためにログエントリをふるいにかけるのに非常に貴重なスキルです。

これらの演習は、ログ管理とファイル検査の概念を実際のシナリオに適用し、Linux システム管理の自信を築くのに役立ちます。

## Quiz Question

メッセージを手動でログに記録するために使用できるコマンドは何ですか？

## Quiz Answer

logger
