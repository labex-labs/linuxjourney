---
lesson_id: "compose-files"
course_id: "docker-compose"
lang: "en"
order_index: 1
title: "Compose Files"
description: "Learn to read a Compose file by finding its services, images, commands, and ports."
meta_title: "Compose Files - Docker Compose"
meta_description: "Learn to read a Compose file by finding its services, images, commands, and ports."
meta_keywords: "compose files, docker compose, devops, Linux Journey"
---

Running a web server and its helper with separate commands is manageable once. A **Compose file** keeps the settings together so you can start the same services again. This course assumes a Docker environment with the Compose plug-in, which provides the `docker compose` command.

## Defining Two Services

In a new practice folder named `journey-compose`, save the following as `compose.yaml`. A **service** describes how Compose should run a container. This file defines a web server and a small toolbox that stays alive for later checks.

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
```

Use spaces for indentation. The indented keys under `web` belong to that service. The dash under `ports` begins a list item. The brackets on `command` also form a list, here with the program name and its argument.

:::single-choice{#compose-files-service-images} Which service uses the BusyBox image?

::option[The web service.]{#compose-files-service-images-a explanation="Web has its own image line naming nginx."}
::option[The toolbox service.]{#compose-files-service-images-c .correct explanation="Its image field names busybox:1.36."}
::option[Both services.]{#compose-files-service-images-b explanation="Each service has a separate image setting."}
:::

## Reading the Web Service

The web service publishes host port 8080 to container port 80. On the machine running Docker, a request to `http://127.0.0.1:8080` can reach Nginx after the service starts. The toolbox has no published port. Its `sleep` command keeps it running for 3,600 seconds during practice.

:::single-choice{#compose-files-mapping-owner} Which part of the file decides how a browser on the Docker host reaches Nginx?

::option[The ports setting under web.]{#compose-files-mapping-owner-a .correct explanation="That entry maps the host address and port to the web container."}
::option[The image tag under toolbox.]{#compose-files-mapping-owner-b explanation="This selects the toolbox image."}
::option[The sleep argument under toolbox.]{#compose-files-mapping-owner-c explanation="The argument controls how long that program runs."}
:::

## Checking the Parsed Configuration

Run this command from the folder with the file. Type the command after the `$` prompt. Compose reads `compose.yaml` and prints the configuration it understands. Look for the `web` and `toolbox` entries. It may expand short settings into longer forms when displaying them.

```bash
$ docker compose config
```

:::single-choice{#compose-files-config-scope} The command prints two services successfully. What have you verified?

::option[Both containers have started.]{#compose-files-config-scope-a explanation="The configuration command only reads and renders settings."}
::option[The browser received a successful response.]{#compose-files-config-scope-c explanation="A request can be tested after the server is started."}
::option[Compose can read the two service definitions.]{#compose-files-config-scope-b .correct explanation="You can inspect the parsed configuration before starting it."}
:::

## Summary

You can now identify the parts of a simple Compose file.

1. Read the names and image references under services.
2. Relate a service's settings to the container it describes.
3. Inspect the parsed file with docker compose config.
