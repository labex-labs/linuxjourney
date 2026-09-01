---
lesson_id: "package-management-systems"
course_id: "packages"
lang: "ru"
order_index: 6
title: "yum и apt"
description: "Изучите работающие с репозиториями процессы APT и DNF для проверки, установки, удаления и обновления пакетов."
meta_title: "yum и apt — пакеты"
meta_description: "Изучите различия yum и apt и научитесь устанавливать, удалять и обновлять пакеты в системах Linux на основе RPM и Debian."
meta_keywords: "yum и apt, yum apt, управление пакетами Linux, apt, yum, Debian, Red Hat, установка пакетов, обновление пакетов, команды Linux"
---

Диспетчеры пакетов, работающие с репозиториями, получают метаданные, разрешают зависимости, проверяют аутентифицированное содержимое и координируют транзакции. Системы семейства Debian обычно используют APT. Современные выпуски Fedora и Red Hat Enterprise Linux используют DNF; в текущих RHEL команда `yum` сохраняется как совместимый псевдоним DNF, тогда как старые системы применяли исходную реализацию YUM.

Всегда следуйте документации установленного дистрибутива и выпуска, а не предполагайте, что один набор команд подходит везде.

## Обновление и проверка метаданных

APT разделяет обновление метаданных и обновление пакетов:

```bash
Debian family: $ sudo apt update
```

Перед установкой выполните поиск и проверку:

```bash
Debian family: $ apt search package-name
Debian family: $ apt show package-name
RPM family:    $ dnf search package-name
RPM family:    $ dnf info package-name
```

Конфигурация репозиториев определяет, что могут обнаружить эти команды. Внимательно проверяйте имена источников, архитектуры, версии и ошибки подписей.

:::single-choice{#package-management-systems-apt-show} Какая команда отображает сведения APT о `package-name`?

::option[`apt remove package-name`]{#package-management-systems-apt-remove-command explanation="Подкоманда `remove` предлагает удалить пакет."}
::option[`dnf search package-name`]{#package-management-systems-dnf-search-command explanation="Команда ищет в репозиториях семейства RPM и не является командой подробностей APT."}
::option[`apt show package-name`]{#package-management-systems-apt-show-command .correct explanation="Подкоманда `show` отображает метаданные именованного двоичного пакета."}
:::

## Установка пакетов

Установите пакет по имени из репозитория:

```bash
Debian family: $ sudo apt install package-name
RPM family:    $ sudo dnf install package-name
```

Диспетчер предлагает зависимости и любые конфликты либо замены. Не подтверждайте автоматически, пока не проверите происхождение, версию и архитектуру пакета, объём загрузки, изменение диска, удаления и новые зависимости.

:::single-choice{#package-management-systems-dnf-install} Какая современная команда устанавливает `package-name` из настроенных репозиториев семейства RPM?

::option[`rpm -qa package-name`]{#package-management-systems-rpm-query-command explanation="Это запрос установленной базы RPM, а не запрос установки из репозитория."}
::option[`dnf install package-name`]{#package-management-systems-dnf-install-command .correct explanation="DNF — современный диспетчер репозиториев в Fedora и новых выпусках RHEL."}
::option[`apt update package-name`]{#package-management-systems-apt-update-package explanation="APT update обновляет индексы и не устанавливает именованный пакет семейства RPM."}
:::

## Удаление пакетов

Запросите удаление:

```bash
Debian family: $ sudo apt remove package-name
RPM family:    $ sudo dnf remove package-name
```

Удаление может повлиять на зависимые пакеты или оставить больше не используемые зависимости и конфигурацию. Проверяйте предлагаемую транзакцию, отличайте семантику remove от purge в системах семейства Debian и сохраняйте данные приложения согласно его собственному процессу резервного копирования и хранения. Удаление пакета не обещает удалить данные, созданные пользователями.

:::single-choice{#package-management-systems-remove-review} Почему следует проверить транзакцию удаления до подтверждения?

::option[Удаление всегда форматирует файловую систему, содержащую пакет.]{#package-management-systems-removal-format explanation="Диспетчеры пакетов удаляют управляемые файлы и состояние, но обычно не форматируют файловую систему."}
::option[Диспетчеры пакетов не могут показать предлагаемый набор изменений.]{#package-management-systems-no-proposal explanation="Интерактивные диспетчеры обычно показывают план транзакции именно для проверки."}
::option[Другие пакеты могут зависеть от выбранного пакета и тоже оказаться затронуты.]{#package-management-systems-dependent-removal .correct explanation="Ограничения зависимостей могут расширить запрос за пределы первоначально введённого имени пакета."}
:::

## Применение обновлений

В системе APT обновите метаданные, а затем отдельным успешным этапом проверьте обновления:

```bash
$ sudo apt update
$ apt list --upgradable
$ sudo apt upgrade
```

В системе DNF проверьте и примените доступные обновления согласно локальной документации:

```bash
$ dnf check-update
$ sudo dnf upgrade
```

Команда обновления может изменить основные библиотеки, службы, ядра и зависимости. Используйте резервные копии, политику обслуживания, примечания к выпуску и подходящее системе планирование перезапуска или перезагрузки. Проверяйте семантику кодов завершения: например, некоторые операции проверки используют ненулевой код, чтобы сообщить о наличии обновлений, а не об ошибке выполнения.

:::single-choice{#package-management-systems-apt-update-upgrade} Как связаны `apt update` и `apt upgrade`?

::option[`update` удаляет пакеты, а `upgrade` восстанавливает их файлы конфигурации.]{#package-management-systems-apt-remove-restore explanation="Между командами нет такого отношения удаления и восстановления."}
::option[`update` обновляет метаданные, а `upgrade` применяет одобренный план обновления пакетов.]{#package-management-systems-apt-two-steps .correct explanation="APT разделяет обновление каталога и установку новых версий пакетов."}
::option[Это два одинаковых имени одной операции.]{#package-management-systems-apt-identical explanation="Они выполняют разные этапы, каждый из которых следует проверять отдельно."}
:::

## Выбор `dnf` или `yum`

В современной документации Fedora и RHEL используйте `dnf`. Команда `yum` в новой системе RHEL может вызывать совместимое поведение DNF, однако скриптам не следует определять реализацию только по имени исполняемого файла. На устаревших хостах проверяйте установленную версию и поддерживаемый синтаксис до переноса инструкций.

:::single-choice{#package-management-systems-yum-current-rhel} Что обычно представляет собой `yum` в современной системе RHEL?

::option[Команду совместимости, работающую поверх DNF.]{#package-management-systems-yum-dnf-alias .correct explanation="Новые выпуски RHEL используют DNF, сохраняя имя команды yum для совместимости."}
::option[Низкоуровневый инструмент Debian для архивов `.deb`.]{#package-management-systems-yum-dpkg explanation="Системы Debian используют для собственных пакетов APT и dpkg, а не YUM."}
::option[Средство сжатия только для метаданных репозитория.]{#package-management-systems-yum-compressor explanation="YUM и DNF — интерфейсы управления пакетами, а не отдельные форматы сжатия."}
:::

Потренируйтесь работать с APT в лаборатории [Установка и удаление пакетов](https://labex.io/ru/labs/linux-installing-and-removing-packages-385380), а с понятиями семейства DNF/YUM — в лаборатории [Запрос и обновление пакетов с помощью YUM](https://labex.io/ru/labs/rhel-query-and-update-packages-with-yum-in-linux-590869).

## Итоги

Теперь вы можете выбирать и проверять распространённые операции с пакетами репозиториев.

1. Используйте APT в системах семейства Debian, а DNF — в современных системах семейства RPM.
2. До установки проверяйте метаданные и предлагаемые изменения зависимостей.
3. Рассматривайте удаление как транзакцию с учётом зависимостей, а не удаление одного файла.
4. Разделяйте обновление метаданных и применение обновлений там, где это делает инструмент.
5. Проверяйте, является ли `yum` старым YUM или командой совместимости DNF.
