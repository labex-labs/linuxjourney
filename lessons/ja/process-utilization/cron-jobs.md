---
index: 8
lang: "ja"
title: "Cron ジョブ"
meta_title: "Cron ジョブ - プロセス利用"
meta_description: "cron ジョブで Linux タスクをスケジュールする方法を学びます。crontab の構文を理解し、日常業務のためにスクリプトを自動化します。この初心者向けのガイドから始めましょう！"
meta_keywords: "cron jobs, crontab, スケジュールタスク，Linux 自動化，Linux コマンド，初心者 Linux, Linux チュートリアル，crontab -e"
---

## Lesson Content

リソースの利用について話してきましたが、Linux には cron を使ってタスクをスケジュールするための便利なツールがあるので、ここで触れておくのが良いでしょう。指定した時間にプログラムを実行してくれるサービスがあります。これは、毎日実行したいスクリプトがあり、何かを実行する必要がある場合に非常に役立ちます。

例えば、`/home/pete/scripts/change_wallpaper`にスクリプトがあるとします。私はこのスクリプトを毎朝壁紙の画像を変更するために使っていますが、毎朝手動でこのスクリプトを実行しなければなりません。代わりに、cron を使ってスクリプトを実行する cron ジョブを作成することができます。この cron ジョブを実行し、スクリプトを実行したい時間を指定できます。

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

フィールドは左から右へ以下の通りです。

- 分 - (0-59)
- 時 - (0-23)
- 日 - (1-31)
- 月 - (1-12)
- 曜日 - (0-7)。0 と 7 は日曜日を表します

フィールドのアスタリスクは、すべての値に一致することを意味します。したがって、上記の例では、毎月毎日午前 8 時 30 分に実行したいということです。

cron ジョブを作成するには、`crontab`ファイルを編集するだけです。

```bash
crontab -e
```

## Exercise

練習は完璧をもたらします！Linux でのタスクスケジューリングの理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux で at と cron を使ってタスクをスケジュールする](https://labex.io/ja/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - `at`、`atq`、`atrm`、`crontab`を使ってジョブの作成、管理、削除を練習し、システム管理タスクの自動化における実践的な経験を積みます。

この演習は、実際のシナリオで概念を適用し、タスクスケジューリングに自信を持つのに役立ちます。

## Quiz Question

cron ジョブを編集するコマンドは何ですか？

## Quiz Answer

crontab -e
