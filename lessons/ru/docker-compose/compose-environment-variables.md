---
lesson_id: "compose-environment-variables"
course_id: "docker-compose"
lang: "ru"
order_index: 5
title: "Переменные окружения"
description: "Научитесь различать значение, подставленное в файл Compose, и значение, переданное в контейнер."
meta_title: "Переменные окружения - Docker Compose"
meta_description: "Научитесь различать значение, подставленное в файл Compose, и значение, переданное в контейнер."
meta_keywords: "переменные окружения, подстановка значений, Docker Compose, DevOps, Linux Journey"
---

Переменная окружения — это значение с именем, которое может прочитать программа. Compose использует переменные двумя способами: подставляет значения при чтении файла и передаёт значения программам внутри контейнера.

## Подставляем значение в файл

Сохраните пример в учебном каталоге под именем `compose.env.yaml`. Выражение `${PAGE_MODE:-demo}` означает, что Compose возьмёт значение `PAGE_MODE`, если переменная задана и не пуста. В остальных случаях он подставит `demo`.

```yaml
services:
  toolbox:
    image: busybox:1.36
    environment:
      PAGE_MODE: "${PAGE_MODE:-demo}"
```

Compose вычисляет выражение до создания контейнера. Это называется **подстановкой**. В других файлах таким же способом можно выбирать, например, порт хоста или тег образа.

:::single-choice{#compose-environment-variables-interpolate-default} Если PAGE_MODE не задана, какое значение появится в выводе конфигурации?

::option[Выражение в исходном виде, как в файле.]{#compose-environment-variables-interpolate-default-a explanation="Compose вычисляет выражение при чтении файла."}
::option[Автоматически созданное имя контейнера.]{#compose-environment-variables-interpolate-default-c explanation="Имя контейнера и значение переменной окружения задаются отдельно."}
::option[Demo, значение после оператора значения по умолчанию.]{#compose-environment-variables-interpolate-default-b .correct explanation="Выражение задаёт demo как запасное значение."}
:::

## Смотрим, какое значение получилось

Если задать переменную перед командой, значение будет действовать только для этого запуска. Попробуйте указать другое значение и посмотреть, что изменится. Команда `config` показывает настройки с подставленными значениями и не создаёт контейнер.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml config
```

Найдите `PAGE_MODE: review` в окружении сервиса. Значение `review` используется для примера. Не помещайте секреты в примеры конфигурации или вывод команд.

:::single-choice{#compose-environment-variables-config-scope} В выводе конфигурации появилось review. Что уже произошло?

::option[Сервис уже запустился с этим значением.]{#compose-environment-variables-config-scope-b explanation="Вывод конфигурации и запуск контейнера — разные операции."}
::option[Compose подставил значение при чтении конфигурации.]{#compose-environment-variables-config-scope-a .correct explanation="Команда config показывает настройки после подстановки, ещё до запуска."}
::option[Теперь все существующие контейнеры используют это значение.]{#compose-environment-variables-config-scope-c explanation="Этот запуск команды не меняет работающие контейнеры."}
:::

## Передаём значение в контейнер

Раздел `environment` передаёт полученное значение в новый контейнер. С помощью `printenv` выведите значение из контейнера, созданного для одного запуска.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml run --rm toolbox printenv PAGE_MODE
```

Должно появиться `review`. Подстановка выбрала значение, а запись в разделе окружения передала его в контейнер. Если переменная нужна только для выбора порта хоста, в окружение программы она автоматически не попадёт.

:::single-choice{#compose-environment-variables-actual-value} Как проверить, какое значение получила программа в контейнере с инструментами?

::option[Вывести PAGE_MODE из контейнера.]{#compose-environment-variables-actual-value-c .correct explanation="Окружение самой программы показывает, какое значение она получила."}
::option[Посмотреть только значение по умолчанию в исходном файле.]{#compose-environment-variables-actual-value-a explanation="Значение в файле может быть переопределено."}
::option[Узнать IP-адрес контейнера с инструментами.]{#compose-environment-variables-actual-value-b explanation="Адрес ничего не говорит о настройках программы."}
:::

## Итоги

Теперь вы различаете два способа использования переменных окружения.

1. Читайте выражения со значением по умолчанию в файле Compose.
2. Проверяйте конфигурацию после подстановки до запуска контейнера.
3. Проверяйте значение в окружении запущенной программы.
