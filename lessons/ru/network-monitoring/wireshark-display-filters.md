---
lesson_id: "wireshark-display-filters"
course_id: "network-monitoring"
lang: "ru"
order_index: 4
title: "Фильтры отображения Wireshark"
description: "Научитесь выбирать пакеты для просмотра в готовом дампе с помощью фильтра отображения Wireshark."
meta_title: "Фильтры отображения Wireshark — Мониторинг сети"
meta_description: "Научитесь выбирать пакеты для просмотра в готовом дампе с помощью фильтра отображения Wireshark."
meta_keywords: "фильтры отображения Wireshark, мониторинг сети, кибербезопасность, Linux Journey"
---

В дампе пакетов могут быть разные протоколы. **Фильтр отображения** указывает Wireshark, какие сохранённые пакеты показать. Сам файл дампа при этом не меняется.

## Как выбрать протокол

Сохраните [учебный дамп](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/examples/network-monitoring/sample.pcap) под именем `sample.pcap`. Откройте его в Wireshark и введите `dns` в поле фильтра отображения. Если на Linux установлен TShark, следующая команда применит тот же фильтр к сохранённому файлу. Файл содержит безвредный запрос разрешения имени и отдельный учебный трафик.

```bash
$ tshark -r sample.pcap -Y dns
```

Параметр `-r` читает файл, а `-Y` применяет фильтр отображения. Найдите запрос и ответ на него.

:::single-choice{#wireshark-display-filters-display-effect} В отфильтрованном списке на две строки меньше, чем в исходном. Что стало с остальными пакетами?

::option[Они удалены из файла дампа.]{#wireshark-display-filters-display-effect-a explanation="Фильтр отображения меняет, какие результаты видны."}
::option[Они остались в файле и не подошли под фильтр.]{#wireshark-display-filters-display-effect-b .correct explanation="Очистите фильтр, чтобы снова увидеть весь список."}
::option[Их повторно отправили по сети.]{#wireshark-display-filters-display-effect-c explanation="При чтении сохранённого дампа пакеты не передаются."}
:::

## Как отобрать пакеты по адресу

Фильтр может обращаться к полю пакета. `ip.addr` применим к IPv4-адресу источника или назначения. Два знака равенства сравнивают поле со значением из примера.

```bash
$ tshark -r sample.pcap -Y 'ip.addr == 192.0.2.10'
```

Кавычки позволяют оболочке передать всё выражение одним аргументом. В показанных строках можно узнать стороны обмена.

:::single-choice{#wireshark-display-filters-address-scope} Пакет отправлен на 192.0.2.10 с другого адреса. Подойдёт ли он под фильтр?

::option[Да, потому что условие проверяет любую из сторон.]{#wireshark-display-filters-address-scope-a .correct explanation="Поле ip.addr может совпасть с адресом источника или назначения."}
::option[Нет, потому что условие проверяет только источник.]{#wireshark-display-filters-address-scope-b explanation="Это поле может совпасть в любом направлении."}
::option[Только если пакет содержит DNS.]{#wireshark-display-filters-address-scope-c explanation="Выражение проверяет только IPv4-адрес."}
:::

![Сохранённый вывод TShark сравнивает отображение только DNS с выводом обоих протоколов в учебном дампе](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/network-monitoring/wireshark-display-filters/saved-dns-exchange.png)

## Как объяснить пустой результат

Пустой результат означает, что фильтр не нашёл подходящих сохранённых пакетов в этом файле. Прежде чем делать более широкий вывод, проверьте выражение, время и точку захвата. Сначала очистите фильтр, чтобы убедиться, что в дампе вообще есть трафик.

:::single-choice{#wireshark-display-filters-empty-capture-view} Вы применили dns к сохранённому дампу и не видите ни одной строки. Что можно сообщить?

::option[Никто во всей сети не использовал DNS.]{#wireshark-display-filters-empty-capture-view-a explanation="Файл охватывает ограниченную точку захвата и период."}
::option[Wireshark удалил данные DNS.]{#wireshark-display-filters-empty-capture-view-b explanation="Фильтр отображения не удаляет сохранённые пакеты."}
::option[Фильтр не показал пакетов DNS в этом дампе.]{#wireshark-display-filters-empty-capture-view-c .correct explanation="Такой вывод ограничен данными, которые вы проверили."}
:::

Чтобы изучить другой дамп в браузерной лаборатории, выполните упражнение на фильтры отображения в курсе [Wireshark для начинающих](https://labex.io/courses/quick-start-with-wireshark).

## Итоги

Теперь вы можете фильтровать сохранённый дамп пакетов и объяснять границы полученного результата.

1. Выбрать протокол с помощью фильтра отображения.
2. Отобрать пакеты по адресу через ip.addr.
3. Учитывать пределы видимости файла при чтении отфильтрованного списка.
