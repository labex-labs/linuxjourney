---
lesson_id: "docker-logs-command"
course_id: "docker"
lang: "en"
order_index: 6
title: "docker logs"
description: "Learn how to read output collected from a container and use it to choose a troubleshooting step."
meta_title: "docker logs - Docker"
meta_description: "Read logs from running and exited containers, focus on recent output, and distinguish an application error from a container status."
meta_keywords: "docker logs, container logs, Docker troubleshooting, startup errors, tail logs"
---

A container named `preview` has exited. The container list gives you its state and exit code. To find out what the program reported, look at the output Docker collected from that container.

## Choosing a Container

Pass the container name to `docker logs`. The command can read retained output from a stopped container that still exists. In this example, a short task tried to read a file at `/site/title.txt` before it stopped.

```text
$ docker logs preview
cat: can't open '/site/title.txt': No such file or directory
```

Here, `cat` is the program that tried to read the file. The message names the path that program could not find inside the container.

:::single-choice{#docker-logs-command-read-exited} Both preview and report used the same image. Which command reads the output from preview?

::option[`docker logs report`]{#docker-logs-command-exited-report explanation="The name selects one container. Report identifies a different run."}
::option[`docker logs busybox:1.36`]{#docker-logs-command-exited-image explanation="That is the image reference. Logs belong to a container created from the image."}
::option[`docker logs preview`]{#docker-logs-command-exited-preview .correct explanation="This uses the name of the container whose output you want."}
:::

## Reading the Message in Context

Logs contain messages the program wrote. A startup message can tell you that the program began listening for requests. An error can tell you which action the program could not complete. The example points to a missing path inside `preview`. A useful next check is whether the container was supposed to have a file at that exact path. The message gives you a place to look.

:::single-choice{#docker-logs-command-error-boundary} What does the missing-file message establish?

::option[The file is missing from every directory on the host.]{#docker-logs-command-error-host-path explanation="The program looked up a path inside the container. The message does not describe all host files."}
::option[The program could not find the named file inside preview.]{#docker-logs-command-error-container-path .correct explanation="The message reports the file lookup from the program running in preview."}
::option[The host browser used an unpublished port.]{#docker-logs-command-error-network explanation="The message concerns a file lookup. It gives no information about the browser's port."}
:::

## Looking at Recent Output

For a container with many lines of output, use `--tail` followed by a number. Docker returns up to that many lines from the end of the collected output. You can start with a small number and read more if the first error is above those lines.

```bash
$ docker logs --tail 5 web
```

![LabEx Terminal showing the missing-file error from preview and the last five log lines from web](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-logs-command/preview-and-tail.png)

The two commands read different containers. In the LabEx run, `preview` reports the missing file and `web` reports that Nginx started.

:::single-choice{#docker-logs-command-tail-choice} You want to see just the most recent two lines available from web. Which command fits?

::option[`docker logs --tail 2 web`]{#docker-logs-command-tail-two .correct explanation="Tail 2 asks for up to two lines from the end of this container's output."}
::option[`docker logs --tail 5 web`]{#docker-logs-command-tail-five explanation="This asks for up to five lines, so it can show more than two."}
::option[`docker logs web`]{#docker-logs-command-tail-unlimited explanation="Without a tail limit, Docker can return all available lines."}
:::

## Handling an Empty Result

Docker can only show output it collected. A command can run quietly, or the program may write its messages to a file that Docker does not collect. If `docker logs` succeeds and prints nothing, use `docker ps -a` to check the container's state. An empty log result alone leaves that state unknown.

:::single-choice{#docker-logs-command-empty-result} The saved task named cleanup has no log lines. You want to know whether it is still running or has already exited. What would answer that?

::option[Ask Docker for more lines from cleanup.]{#docker-logs-command-empty-more-lines explanation="Changing the line limit does not reveal whether a quiet program has stopped."}
::option[Find the image that cleanup was started from.]{#docker-logs-command-empty-image explanation="The image identifies its starting files and settings. The container list shows its state."}
::option[Read the state of cleanup in the full container list.]{#docker-logs-command-empty-container-state .correct explanation="The full list includes existing containers that have exited, as well as running ones."}
:::

## Summary

You can now use a container's output to decide what to check next.

1. Read collected output from a named container, including one that has exited.
2. Use the program's message to locate the reported problem.
3. Limit the output with `--tail`.
4. Use a separate check when the logs leave a question open.
