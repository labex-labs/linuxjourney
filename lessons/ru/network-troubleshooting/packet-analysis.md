---
lang: "ru"
title: "Анализ пакетов"
description: "Изучите основы анализа пакетов с помощью tcpdump. Разберитесь в сетевом трафике, захватывайте данные и интерпретируйте вывод с помощью этого руководства по Linux для начинающих."
keywords: "tcpdump, анализ пакетов, сетевой анализ, сети Linux, руководство для начинающих, Wireshark, команды Linux, сетевой трафик"
---

## Lesson Content

Тема анализа пакетов могла бы занять целый отдельный курс, и существует множество книг, написанных только по анализу пакетов. Однако сегодня мы изучим только основы. Существуют два чрезвычайно популярных анализатора пакетов: Wireshark и tcpdump. Эти инструменты сканируют ваши сетевые интерфейсы, захватывают активность пакетов, разбирают пакеты и выводят информацию для нашего просмотра. Они позволяют нам углубиться в тонкости сетевого анализа и разобраться в низкоуровневых вещах. Мы будем использовать tcpdump, так как у него более простой интерфейс; однако, если вы решите освоить анализ пакетов для своего набора инструментов, я бы порекомендовал изучить Wireshark.

### Install tcpdump

```bash
sudo apt install tcpdump
```

### Capture packet data on an interface

```plaintext
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on wlan0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
11:28:24.960464 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 3, length 64
11:28:24.979299 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 3, length 64
11:28:25.961869 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 4, length 64
11:28:25.976176 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 4, length 64
11:28:26.963667 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 5, length 64
11:28:26.976137 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 5, length 64
11:28:30.674953 ARP, Request who-has 172.254.1.0 tell ThePickleParty.lan, length 28
11:28:31.190665 IP ThePickleParty.lan.51056 > 192.168.86.255.rfe: UDP, length 306
```

Вы заметите много всего, когда запустите захват пакетов. Что ж, это ожидаемо; в фоновом режиме происходит много сетевой активности. В моем примере выше я взял только фрагмент своего захвата, а именно время, когда я решил пропинговать <www.google.com>.

### Understanding the output

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- Первое поле — это метка времени сетевой активности.
- IP: содержит информацию о протоколе.
- Далее вы увидите исходный и целевой адрес: `icebox.lan > nuq04s29-in-f4.1e100.net`.
- `seq`: это начальный и конечный порядковый номер TCP-пакета.
- `length`: длина в байтах.

Как видно из вывода tcpdump, мы отправляем пакет ICMP echo request на <www.google.com> и получаем в ответ пакет ICMP echo reply! Также обратите внимание, что разные пакеты будут выводить разную информацию; обратитесь к manpage, чтобы узнать, что это такое.

### Writing tcpdump output to a file

```bash
sudo tcpdump -w /some/file
```

Несколько последних мыслей: мы лишь поверхностно затронули тему анализа пакетов. Есть так много всего, что можно изучить, и мы даже не коснулись более глубокого анализа с выводом в Hex и ASCII. В Интернете есть множество ресурсов, которые помогут вам узнать больше об анализаторах пакетов, и я призываю вас найти их!

## Exercise

Download and install the Wireshark tool and play around with the interface.

## Quiz Question

Какой флаг используется для захвата определенного интерфейса с помощью tcpdump?

## Quiz Answer

-i
