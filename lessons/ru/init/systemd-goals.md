---
lesson_id: "systemd-goals"
course_id: "init"
lang: "ru"
order_index: 6
title: "Цели systemd"
description: "Узнайте, как просматривать, переопределять, проверять, запускать, включать и диагностировать service units systemd."
meta_title: "Цели systemd - Init"
meta_description: "Изучите цели systemd и управление службами Linux командами systemctl: основы unit-файлов, запуск, остановку, включение и просмотр состояния."
meta_keywords: "systemd, systemctl, службы Linux, unit-файлы, цели systemd, управление службами, units systemd, команды Linux"
---

`systemctl` отправляет запросы менеджеру systemd. Этот урок посвящён системным service units. До изменения состояния подтвердите точное имя unit, область менеджера, зависимости и эксплуатационное влияние.

## Чтение service unit

Минимальный иллюстративный unit может выглядеть так:

```ini
[Unit]
Description=Example worker
Wants=network-online.target
After=network-online.target

[Service]
Type=exec
ExecStart=/usr/local/bin/example-worker
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `[Unit]` содержит описание и связи зависимостей.
- `[Service]` определяет жизненный цикл процесса и поведение службы.
- `[Install]` сообщает командам включения, какие псевдонимы или ссылки зависимостей создавать; это не автоматически активная зависимость времени выполнения.

`ExecStart=` по умолчанию не передаётся оболочке. Конвейеры, перенаправления, переменные и кавычки работают не как в интерактивной командной строке, если явно не вызвана оболочка.

:::single-choice{#systemd-goals-install-section} Каково основное назначение директив `[Install]`, например `WantedBy=`?

::option[Гарантировать, что процесс службы уже работает.]{#systemd-goals-install-running explanation="Для текущей активации нужен start или другая запускающая зависимость."}
::option[Описывать ссылки или связи, создаваемые при включении unit.]{#systemd-goals-enable-links .correct explanation="Установочные метаданные интерпретируются операциями enable и отделены от текущего состояния процесса."}
::option[Выполнять каждую команду через интерактивную оболочку пользователя.]{#systemd-goals-install-shell explanation="Разбор команд unit по умолчанию не использует интерактивную оболочку."}
:::

## Просмотр эффективной конфигурации

Выведите загруженные units:

```bash
$ systemctl list-units --type=service
```

Выведите установленные unit-файлы и состояния включения:

```bash
$ systemctl list-unit-files --type=service
```

Это разные представления: unit-файл может быть включён, но неактивен; активен, но отключён; static, generated, transient, masked либо отсутствовать в одном списке. Посмотрите объединённое содержимое поставщика и drop-in:

```bash
$ systemctl cat UNIT.service
$ systemctl show UNIT.service
```

:::single-choice{#systemd-goals-list-units-versus-files} Что показывает `list-unit-files`, чего прежде всего не показывает `list-units`?

::option[Только процессы с самым высоким потреблением CPU.]{#systemd-goals-cpu-processes explanation="Ранжирование ресурсов процессов не входит в эти команды инвентаризации units."}
::option[Состояния включения установленных unit-файлов.]{#systemd-goals-unit-file-state .correct explanation="Команда сообщает enabled, disabled, static, masked и связанные установочные состояния."}
::option[Каждую строку, когда-либо записанную в журнал.]{#systemd-goals-all-journal explanation="Для запросов журнала используется `journalctl`."}
:::

## Создание локального переопределения

Используйте drop-in вместо редактирования пакетного unit:

```bash
$ sudo systemctl edit UNIT.service
```

В современных реализациях после сохранения этот процесс обычно просит менеджер перечитать конфигурацию. Если файлы менялись иным способом, выполните:

```bash
$ sudo systemctl daemon-reload
```

`daemon-reload` перечитывает определения units и перестраивает зависимости. Он не перезагружает конфигурацию приложений и не перезапускает службы. При необходимости проверьте синтаксис и зависимости через `systemd-analyze verify`, затем просмотрите итоговый объединённый unit.

:::single-choice{#systemd-goals-daemon-reload} Что делает `systemctl daemon-reload`?

::option[Заставляет каждый демон перечитать конфигурацию приложения.]{#systemd-goals-reload-all-apps explanation="Перезагрузка приложения специфична для службы и отделена от конфигурации менеджера."}
::option[Перезагружает ядро в новый выпуск.]{#systemd-goals-reload-kernel explanation="Для активации ядра нужна загрузка, а не перечитывание units."}
::option[Перечитывает определения units systemd и сведения о зависимостях.]{#systemd-goals-reload-manager .correct explanation="Он обновляет представление конфигурации менеджера, не перезапуская службы автоматически."}
:::

## Текущее состояние службы

После проверки конфигурации и сохранения аварийного доступа:

```bash
$ sudo systemctl start peanut.service
$ sudo systemctl stop peanut.service
$ sudo systemctl restart peanut.service
$ sudo systemctl reload peanut.service
```

`reload` успешен только при определённом или поддерживаемом действии перезагрузки. `restart` прерывает процесс и может не восстановить службу. Для удалённого доступа, сети, хранилища и аутентификации сохраняйте отдельный консольный путь и проверяйте конфигурацию заранее.

Проверьте состояние и журналы:

```bash
$ systemctl status peanut.service
$ systemctl is-active peanut.service
$ journalctl -u peanut.service -b
```

Состояние «Active» отражает менеджер, но не доказывает здоровье каждой конечной точки приложения.

:::single-choice{#systemd-goals-start-peanut} Какая команда запускает `peanut.service` сейчас, сама по себе не меняя будущее включение?

::option[`sudo systemctl enable peanut.service`]{#systemd-goals-enable-only explanation="Enable меняет установочные ссылки, но не запускает службу без `--now`."}
::option[`sudo systemctl start peanut.service`]{#systemd-goals-start-command .correct explanation="Start запрашивает текущую активацию и отделён от включения."}
::option[`sudo systemctl daemon-reload peanut.service`]{#systemd-goals-daemon-reload-unit explanation="Daemon-reload не принимает unit для активации и не запускает эту службу."}
:::

## Включение, отключение и маскирование

Управляйте будущими ссылками зависимостей:

```bash
$ sudo systemctl enable peanut.service
$ sudo systemctl disable peanut.service
```

Enable не запускает unit без `--now`, а disable не останавливает работающую unit без `--now`. У static unit может не быть установочных метаданных, но она всё равно активируется как зависимость другой unit.

Mask связывает unit с `/dev/null` и блокирует обычную активацию, включая зависимую, до unmask. Это сильнее disable и способно сломать зависимые компоненты; сначала изучите обратные зависимости.

:::single-choice{#systemd-goals-disable-runtime} Что происходит с уже работающей службой после `systemctl disable UNIT` без `--now`?

::option[Она немедленно завершается через `SIGKILL`.]{#systemd-goals-disable-kills explanation="Disable сам по себе не запрашивает текущую остановку."}
::option[Её исполняемый файл удаляется из файловой системы.]{#systemd-goals-disable-deletes explanation="Операции включения управляют ссылками, а не файлами пакета программы."}
::option[Обычно она продолжает работать, а будущие ссылки включения удаляются.]{#systemd-goals-disable-keeps-running .correct explanation="Текущее и установочное состояния являются отдельными измерениями."}
:::

## Проверка результата службы

После изменения проверяйте состояние процесса, недавние журналы, слушающие конечные точки, зависимые units, здоровье приложения и поведение после контролируемой перезагрузки, если менялось включение. По ситуации используйте `systemctl is-failed`, `systemctl list-dependencies` и родные проверки приложения.

## Итоги

Теперь вы можете управлять службой systemd, не путая конфигурацию, текущее состояние и включение.

1. Читать `[Unit]`, `[Service]` и `[Install]` по разным ролям.
2. Сравнивать состояние загруженных units и установленных unit-файлов.
3. Использовать drop-in и перечитывать менеджер после внешних изменений файлов.
4. Запускать, останавливать, перезагружать и перезапускать только после оценки влияния.
5. Считать enable, disable и mask отдельными средствами постоянства.
