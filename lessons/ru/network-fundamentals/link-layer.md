---
index: 8
lang: "ru"
title: "Канальный уровень"
meta_title: "Канальный уровень - Основы сети"
meta_description: "Узнайте о канальном уровне в TCP/IP, как ARP разрешает MAC-адреса и как происходит прохождение пакетов. Изучите основы сети с помощью этого руководства по сетям Linux."
meta_keywords: "Канальный уровень, ARP, TCP/IP, MAC-адрес, основы сети, сети Linux, для начинающих, руководство"
---

## Lesson Content

В основе модели TCP/IP лежит канальный уровень (Link Layer). Этот уровень аппаратно-зависим.

На канальном уровне наш пакет инкапсулируется еще раз в нечто, называемое фреймом (frame). Заголовок фрейма содержит MAC-адреса источника и назначения наших хостов, контрольные суммы и разделители пакетов, чтобы получатель мог определить, когда пакет заканчивается.

К счастью, мы находимся в одной сети, поэтому нашему пакету не придется путешествовать слишком далеко. Сначала канальный уровень прикрепляет мой MAC-адрес источника к заголовку фрейма, но ему также нужно знать MAC-адрес Патти. Как он это узнает, и как мне его найти, если его нет в Интернете? Мы используем ARP!

### ARP (Address Resolution Protocol)

ARP находит MAC-адрес, связанный с IP-адресом. ARP используется в пределах одной сети. Если бы Патти не была в той же сети, мы бы использовали систему маршрутизации для определения следующего маршрутизатора, который получит пакет, и как только мы оказались бы в одной сети, мы могли бы использовать ARP.

Как только мы оказываемся в одной сети, системы сначала используют таблицу поиска ARP, которая хранит информацию о том, какие IP-адреса связаны с какими MAC-адресами. Если значения там нет, то используется ARP. Затем система отправит широковещательное сообщение в сеть, используя протокол ARP, чтобы выяснить, какой хост имеет IP 10.10.1.4. Широковещательное сообщение — это специальное сообщение, которое отправляется всем хостам в сети (метко названное для отправки широковещательной рассылки). Любая машина с запрошенным IP-адресом ответит ARP-пакетом, содержащим IP-адрес и MAC-адрес.

Теперь, когда у нас есть все необходимые данные — IP-адрес и MAC-адреса — наш канальный уровень пересылает этот фрейм через нашу сетевую карту, к следующему устройству, и находит сеть Патти. Этот шаг немного сложнее, чем я только что объяснил, но мы обсудим более подробную информацию в курсе по маршрутизации.

И вот оно: простое (или не очень простое) прохождение пакета по уровням TCP/IP. Имейте в виду, что пакеты не перемещаются односторонне. Мы еще даже не добрались до сети Патти! При перемещении по сетям требуется пройти через модель TCP/IP как минимум дважды, прежде чем какие-либо данные будут отправлены или получены. В действительности, этот пакет будет выглядеть примерно так:

### Packet Traversal

1. Pete sends Patty an email: this data gets sent to the transport layer.
2. The transport layer encapsulates the data into a TCP or UDP header to form a segment. The segment attaches the destination and source TCP or UDP port, then the segment is sent to the network layer.
3. The network layer encapsulates the TCP segment inside an IP packet; it attaches the source and destination IP address. Then it routes the packet to the link layer.
4. The packet then reaches Pete's physical hardware and gets encapsulated in a frame. The source and destination MAC addresses get added to the frame.
5. Patty receives this data frame through her physical layer and checks each frame for data integrity, then de-encapsulates the frame contents and sends the IP packet to the network layer.
6. The network layer reads the packet to find the source and destination IP that was previously attached. It checks if its IP is the same as the destination IP, which it is! It de-encapsulates the packet and sends the segment to the transport layer.
7. The transport layer de-encapsulates the segments, checks the TCP or UDP port numbers, and makes a connection to the application layer based on those port numbers.
8. The application layer receives the data from the transport layer on the port that was specified and presents it to Patty in the form of the final email message.

## Exercise

No exercises for this lesson.

## Quiz Question

Что используется для поиска MAC-адреса в той же сети?

## Quiz Answer

ARP
