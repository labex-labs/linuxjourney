---
lesson_id: "docker-ps-command"
course_id: "docker"
lang: "en"
order_index: 4
title: "docker ps"
description: "Learn how to list Docker containers and tell which ones are running or have exited."
meta_title: "docker ps - Docker"
meta_description: "Read docker ps output, find stopped containers with docker ps -a, and interpret container names and exit codes."
meta_keywords: "docker ps, list Docker containers, stopped containers, docker ps -a, container status, exit codes"
---

Is the web server you started in Docker still running? Use `docker ps` to check. A Docker image packages the program and the files it needs. A container is an instance created from that image. The command shows the container list as it looks when you run it.

## Listing Running Containers

By default, `docker ps` lists running containers. The examples show a few columns from a prepared Docker environment, so you can read the output without setting up Docker. In a terminal, type the command after the `$` prompt.

```text
$ docker ps
IMAGE         STATUS         NAMES
nginx:alpine  Up 4 minutes   web
nginx:alpine  Up 30 seconds  demo
```

If Docker prints just the column headers, its running-container list is empty. The same environment can still contain containers that have stopped.

:::single-choice{#docker-ps-running-list} Docker prints only the column headers after you run `docker ps`. What can you tell from that output?

::option[There are no images available to run.]{#docker-ps-running-list-images explanation="The command lists containers. Images can be available even when the running-container list is empty."}
::option[There are no containers in the running list.]{#docker-ps-running-list-empty .correct explanation="The default list shows running containers. Stopped containers can still exist."}
::option[There are no stopped containers to inspect.]{#docker-ps-running-list-stopped explanation="Stopped containers are outside the default selection. The empty list gives no information about them."}
:::

## Reading Names and Status

Start with `NAMES` to find the container you want. Both rows show the same image, `nginx:alpine`, in the `IMAGE` column. Find `web` in the rightmost column, then read `STATUS` on that row. `Up 4 minutes` means that container has been running for about four minutes.

:::single-choice{#docker-ps-name-column} Which row describes a container that has been running for about 30 seconds?

::option[The row named `demo`.]{#docker-ps-name-demo .correct explanation="Find Up 30 seconds under STATUS and follow that row to demo under NAMES."}
::option[The row named `web`.]{#docker-ps-name-web explanation="The web row shows Up 4 minutes. The two containers use the same image and have different start times."}
::option[Both rows with the image `nginx:alpine`.]{#docker-ps-name-image-reference explanation="Each row has its own status. Sharing an image does not give the containers the same start time."}
:::

## Including Exited Containers

If a container you expect is missing, try `docker ps -a`. The `-a` option is short for `--all`. It includes containers that have stopped and still exist. This example also includes a prepared task named `preview`.

```text
$ docker ps -a
IMAGE         STATUS                         NAMES
nginx:alpine  Up 4 minutes                   web
nginx:alpine  Up 30 seconds                  demo
busybox:1.36  Exited (0) 2 minutes ago       report
busybox:1.36  Exited (1) About a minute ago  preview
```

A container runs a main program, such as a web server or a script. `Exited` means that program has stopped. The number in parentheses is its **exit code**, the result it reported when it stopped. Zero usually means success, and a nonzero code usually indicates an error. The `report` task shows `Exited (0)`, a normal result for a task that finished successfully.

![LabEx Terminal showing running and exited containers with report at exit code 0 and preview at exit code 1](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-ps-command/running-and-exited.png)

The LabEx capture lists just the names and states of the four example containers. Elapsed times depend on when you run the command.

:::single-choice{#docker-ps-exit-code-reading} Which row would you investigate for an error, based on its exit code?

::option[`report`, because it has exited.]{#docker-ps-exit-code-report explanation="A short task can exit after it finishes. The exit code of zero usually means it reported success."}
::option[`demo`, because it started most recently among the running containers.]{#docker-ps-exit-code-demo explanation="Up tells you how long the program has been running. This row has no exit code."}
::option[`preview`, because it exited with code 1.]{#docker-ps-exit-code-preview .correct explanation="Preview shows Exited (1). That points to a problem worth checking even though the status alone gives no cause."}
:::

## Choosing the Next Check

An exit code helps you decide where to look. To see whether `preview` printed an error message, use `docker logs` followed by its name. This shows the output Docker collected from that container.

```bash
$ docker logs preview
```

For a running web server, you may also want to know whether a visitor can open its page. To check that, open the page from the computer that needs to reach it. `Up` describes the program inside the container. A successful browser request confirms that the page is reachable from where you tested.

:::single-choice{#docker-ps-check-visitor-access} The page opens on the computer running Docker. A coworker needs to open it from another computer. Which check tells you whether they can?

::option[Open the page from the coworker's computer.]{#docker-ps-next-check-visitor-browser .correct explanation="A request from that computer tests the connection the coworker will use."}
::option[Run `docker ps` again on the Docker computer.]{#docker-ps-next-check-status-again explanation="The list can confirm web is still running. A browser request checks reachability from the coworker's computer."}
::option[Open the page again on the Docker computer.]{#docker-ps-next-check-host-browser explanation="That repeats the check from the original computer. The coworker's connection may behave differently."}
:::

## Summary

You can now use the container list to identify a container, read its state, and choose what to check next.

1. Use `docker ps` to list running containers.
2. Find a container by name and read its status.
3. Use `docker ps -a` to include exited containers.
4. Use logs or a browser request to answer questions the status alone cannot resolve.
