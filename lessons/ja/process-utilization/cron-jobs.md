---
index: 8
lang: "ja"
title: "Cron ジョブ"
meta_title: "Cron ジョブ - プロセス利用率"
meta_description: "cron ジョブで Linux タスクをスケジュールする方法を学びます。crontab の構文を理解し、日常業務のためにスクリプトを自動化します。この初心者向けのガイドから始めましょう！"
meta_keywords: "cron jobs, crontab, タスクのスケジュール，Linux の自動化，Linux コマンド，初心者向け Linux, Linux チュートリアル，crontab -e"
---

## Lesson Content

これまでリソースの利用について話してきましたが、ここでは Linux でタスクをスケジュールするために使用される優れたツールである cron について触れるのが良いでしょう。cron は、指定した時間にプログラムを実行するサービスです。毎日実行したいスクリプトがあり、それが何かを実行する必要がある場合に、これは非常に便利です。

例えば、`/home/pete/scripts/change_wallpaper` にスクリプトがあるとします。私はこのスクリプトを毎朝壁紙の画像を変更するために使用していますが、毎朝手動でこのスクリプトを実行しなければなりません。代わりに、cron ジョブを作成して、cron を介してスクリプトを実行することができます。この cron ジョブを実行したい時間を指定し、スクリプトを実行できます。

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

フィールドは左から右へ以下の通りです。

- Minute - (0-59)
- Hour - (0-23)
- Day of the month - (1-31)
- Month - (1-12)
- Day of the week - (0-7). 0 と 7 は日曜日を表します

フィールドのアスタリスクは、すべての値に一致することを意味します。したがって、上記の例では、毎月毎日午前 8 時 30 分に実行したいということです。

cron ジョブを作成するには、`crontab` ファイルを編集するだけです。

```bash
crontab -e
```

## Exercise

指定した時間に実行したい cron ジョブを作成してください。

## Quiz Question

cron ジョブを編集するコマンドは何ですか？

## Quiz Answer

crontab -e
