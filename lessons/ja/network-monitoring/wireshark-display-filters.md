---
lesson_id: "wireshark-display-filters"
course_id: "network-monitoring"
lang: "ja"
order_index: 4
title: "Wireshark の表示フィルター"
description: "Wireshark の表示フィルターで、用意されたキャプチャの表示を絞り込む方法を学びます。"
meta_title: "Wireshark の表示フィルター - ネットワーク監視"
meta_description: "Wireshark の表示フィルターで、用意されたキャプチャの表示を絞り込む方法を学びます。"
meta_keywords: "Wireshark, 表示フィルター, ネットワーク監視, サイバーセキュリティ, Linux Journey"
---

パケットキャプチャには複数のプロトコルが含まれることがあります。**表示フィルター**では、保存済みのパケットのうち、Wireshark に表示するものを指定します。変わるのは表示内容で、キャプチャファイルはそのままです。

## プロトコルを選ぶ

GitHub で[サンプルキャプチャ](https://github.com/labex-labs/linuxjourney/blob/master/examples/network-monitoring/sample.pcap)のページを開き、ファイルを `sample.pcap` として保存します。Wireshark で開いて、表示フィルター欄に `dns` と入力します。TShark が入っている Linux 端末では、次のコマンドで保存済みファイルに同じ表示フィルターを適用できます。この例のファイルには、安全な名前解決と、それとは別の練習用通信が含まれます。

```bash
$ tshark -r sample.pcap -Y dns
```

`-r` オプションはファイルを読み込み、`-Y` は表示フィルターを適用します。問い合わせとその応答を探します。

:::single-choice{#wireshark-display-filters-display-effect} フィルターをかけると、元の表示より 2 行減りました。表示されなくなったパケットはどうなりましたか？

::option[キャプチャファイルから削除されました。]{#wireshark-display-filters-display-effect-a explanation="表示フィルターは、画面に出す結果を変えます。"}
::option[ファイルに残っていますが、このフィルターには一致しませんでした。]{#wireshark-display-filters-display-effect-b .correct explanation="フィルターを解除すると、絞り込み前の表示に戻ります。"}
::option[ネットワーク上に再送信されました。]{#wireshark-display-filters-display-effect-c explanation="保存済みキャプチャを読み込んでも、パケットは送信されません。"}
:::

## アドレスで絞り込む

フィルターではパケットのフィールドも指定できます。`ip.addr` は、IPv4 の送信元または宛先アドレスに一致します。二つの等号で、フィールドと例の値を比較します。

```bash
$ tshark -r sample.pcap -Y 'ip.addr == 192.0.2.10'
```

シェルで式を引用符で囲むと、式全体が一つの引数として渡されます。表示された行から、通信の両端を確認できます。

:::single-choice{#wireshark-display-filters-address-scope} 別のアドレスから 192.0.2.10 宛てにパケットが送られました。このフィルターに一致しますか？

::option[はい。通信のどちらの端でも条件に合えば一致します。]{#wireshark-display-filters-address-scope-a .correct explanation="ip.addr は送信元と宛先のどちらにも一致します。"}
::option[いいえ。この条件で確認するのは送信元だけです。]{#wireshark-display-filters-address-scope-b explanation="このフィールドは両方向のアドレスに一致します。"}
::option[パケットに DNS が含まれる場合に限ります。]{#wireshark-display-filters-address-scope-c explanation="この式で確認するのは IPv4 アドレスだけです。"}
:::

![練習用キャプチャで、DNS のみの表示と両プロトコルを含む表示を比較した TShark の出力](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/network-monitoring/wireshark-display-filters/saved-dns-exchange.png)

## 何も表示されないときに判断できること

結果が空の場合、調べたファイルに、そのフィルターに一致する保存済みパケットがなかったことを示します。より広い範囲について判断する前に、フィルター式、時刻、取得地点を確認します。まずフィルターを解除し、キャプチャに通信が入っていることを確かめます。

:::single-choice{#wireshark-display-filters-empty-capture-view} 保存済みのキャプチャに dns を適用しても 1 行も表示されません。何を報告できますか？

::option[ネットワークのどこでも、誰も DNS を使いませんでした。]{#wireshark-display-filters-empty-capture-view-a explanation="一つのファイルで観測できる場所と時間帯には限りがあります。"}
::option[Wireshark が DNS の証拠を消去しました。]{#wireshark-display-filters-empty-capture-view-b explanation="表示フィルターは、保存済みのパケットを削除しません。"}
::option[このキャプチャにこのフィルターを適用したところ、DNS パケットは表示されませんでした。]{#wireshark-display-filters-empty-capture-view-c .correct explanation="実際に調べた証拠の範囲に収まる報告です。"}
:::

ブラウザーのラボで別のキャプチャを調べるには、[Wireshark 入門](https://labex.io/courses/quick-start-with-wireshark)の表示フィルター演習を試してください。

## まとめ

保存済みのパケットキャプチャを絞り込み、結果からどこまで分かるかを説明できるようになりました。

1. 表示フィルターでプロトコルを選びます。
2. ip.addr でパケットのアドレスを絞り込みます。
3. ファイルで観測できる範囲を踏まえて、絞り込んだ結果を読み取ります。
