---
lesson_id: "docker-run-command"
course_id: "docker"
lang: "en"
order_index: 3
title: "docker run"
description: "Learn how Docker creates and starts containers from images with docker run."
meta_title: "docker run - Docker"
meta_description: "Read a docker run command, choose a container name, and distinguish a short foreground task from a detached server."
meta_keywords: "docker run, run a Docker container, container names, foreground, detached mode"
---

You have an image for a web server. To start the server, use `docker run` to create and start a container from that image. Start with a command that finishes quickly so you can see when control returns to the terminal.

## Running a Short Task

BusyBox is a small image with basic Linux commands. In the example below, `echo` prints a message. Put the image reference before the command you want to run inside the container. Docker normally downloads the image if it is missing locally. The `$` marks the terminal prompt. If Docker needs to pull the image first, it may print download messages before the line shown here.

```text
$ docker run busybox:1.36 echo Hello
Hello
```

You see the output in your terminal. After `echo` finishes, the container stops and your prompt returns.

:::single-choice{#docker-run-command-short-task} What runs inside the container in this example?

::option[`busybox:1.36` as a shell command.]{#docker-run-command-short-image explanation="Busybox is the image supplying the tools. The command comes after the image reference."}
::option[`echo Hello` using the image's tools.]{#docker-run-command-short-echo .correct explanation="The words after the image reference select echo and tell it what to print."}
::option[`docker run` as a second Docker command.]{#docker-run-command-short-docker explanation="You run docker run in your terminal. It starts the command inside the container."}
:::

## Naming the Container

Use `--name` before the image reference to give a container a name you can recognize later. This command names a short task `report`.

```bash
$ docker run --name report busybox:1.36 echo Ready
```

An existing container keeps its name after it stops. In the same Docker environment, use a name that is available when creating another container.

:::single-choice{#docker-run-command-name-choice} Report has finished, but the container still exists. You want a second container using the same image. What can you change?

::option[Use a new container name and keep the image reference.]{#docker-run-command-name-new .correct explanation="A free name lets Docker create a separate container from the same image."}
::option[Change the image tag and keep the container name.]{#docker-run-command-name-change-tag explanation="The original container still holds the name, even if you select a different image."}
::option[Change the message and keep the container name.]{#docker-run-command-name-change-message explanation="The message is input for echo. It does not free the name report."}
:::

## Starting a Server in the Background

Images can specify a default command. The `nginx:alpine` image starts a web server when you omit a command after the image name. Add `-d` to **detach**, which lets the server run while your prompt returns.

```bash
$ docker run -d --name web nginx:alpine
```

Docker prints a container ID, a long identifier for the container it started. You will check whether the server is still running in the next lesson.

![LabEx Terminal showing Hello and Ready from short Docker tasks and a container ID from a detached server](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-run-command/foreground-and-detached.png)

The short tasks print their messages in the terminal. The detached server returns a container ID.

:::single-choice{#docker-run-command-detach-meaning} Docker prints an ID and the prompt returns. What does detach let you do?

::option[Use the terminal only after the server finishes.]{#docker-run-command-detach-wait explanation="Detached mode gives you the prompt while the server can continue running."}
::option[Skip starting the server and keep the image ready.]{#docker-run-command-detach-skip explanation="Docker still starts the container in detached mode."}
::option[Use the terminal while the server runs.]{#docker-run-command-detach-continue .correct explanation="Detached mode returns control to your terminal after starting the container."}
:::

## Recognizing a New Container

Each successful `docker run` creates a new container. If you use the server image again with a free name, Docker creates a second container. The first one keeps its own name and state.

:::single-choice{#docker-run-command-second-instance} Web is running. What does `docker run -d --name demo nginx:alpine` do if demo is available?

::option[Renames the running web container to demo.]{#docker-run-command-second-rename explanation="Docker run creates a container. The original web container keeps its name."}
::option[Adds demo as another tag for the image.]{#docker-run-command-second-tag explanation="The option names a container. The image reference remains nginx:alpine."}
::option[Starts a separate container named demo.]{#docker-run-command-second-new .correct explanation="Docker creates a new container using that image and assigns the name demo."}
:::

For practice starting a container and observing its output, try [Your First Docker Lab](https://labex.io/labs/docker-your-first-docker-lab-92719).

## Summary

You can now read a docker run command and predict what Docker will create.

1. Identify the image and the optional command that runs in the container.
2. Use `--name` to identify a container later.
3. Describe what happens when a short task finishes.
4. Use `-d` to return to the prompt while a server runs.
