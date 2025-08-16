---
lang: "ru"
title: "Имена устройств"
description: "Изучите имена устройств Linux, такие как SCSI (sd), псевдо- и PATA (hd) устройства. Разберитесь с /dev/sda, /dev/null и многим другим в этом руководстве для начинающих."
keywords: "Имена устройств Linux, /dev, устройства SCSI, псевдоустройства, устройства PATA, учебник по Linux, Linux для начинающих, файлы устройств"
---

## Lesson Content

Вот наиболее распространенные имена устройств, с которыми вы столкнетесь:

### SCSI Devices

Если на вашей машине есть какое-либо массовое хранилище, скорее всего, оно использует протокол SCSI (произносится «скази»). SCSI расшифровывается как Small Computer System Interface; это протокол, используемый для обеспечения связи между дисками, принтерами, сканерами и другими периферийными устройствами и вашей системой. Возможно, вы слышали о устройствах SCSI, которые на самом деле не используются в современных системах; однако наши системы Linux сопоставляют диски SCSI с жесткими дисками в `/dev`. Они представлены префиксом `sd` (SCSI disk):

Распространенные файлы устройств SCSI:

- `/dev/sda` - First hard disk
- `/dev/sdb` - Second hard disk
- `/dev/sda3` - Third partition on the first hard disk

### Pseudo Devices

Как мы обсуждали ранее, псевдоустройства на самом деле физически не подключены к вашей системе. Большинство распространенных псевдоустройств являются символьными устройствами:

- `/dev/zero` - accepts and discards all input, produces a continuous stream of NULL (zero value) bytes
- `/dev/null` - accepts and discards all input, produces no output
- `/dev/random` - produces random numbers

### PATA Devices

Иногда в старых системах вы можете увидеть жесткие диски, обозначаемые префиксом `hd`:

- `/dev/hda` - First hard disk
- `/dev/hdd2` - Second partition on 4th hard disk

## Exercise

Write to the pseudo devices and see what happens. Be careful not to write your disks to those devices!

## Quiz Question

Каково будет обычное имя устройства для первого раздела на втором диске SCSI?

## Quiz Answer

sdb1
