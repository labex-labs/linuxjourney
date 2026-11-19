---
lesson_id: "docker-containers"
course_id: "docker"
lang: "en"
order_index: 1
title: "Containers"
description: "Learn what a Docker container runs and how it relates to the machine running Docker."
meta_title: "Containers - Docker"
meta_description: "Understand containers through a small web server and learn what changes when its main program starts or stops."
meta_keywords: "Docker containers, container basics, Docker host, container process, web server"
---

A browser opens a page from a web server running in Docker. Where is the server running, and what happens to the page when that server stops? Start with the program that answers the browser.

## A Program Inside a Container

A **web server** is a program that answers requests for pages. Imagine that your browser and a small web server named `web` are on the same machine. Docker runs the server in a **container**, which gives the program its own view of files and other resources. The course uses prepared examples, so you can follow along without installing Docker.

:::single-choice{#docker-containers-page-request} When the browser asks for a page, what sends back the page content?

::option[The web server running in the container.]{#docker-containers-page-server .correct explanation="The server program receives the request and sends the page back."}
::option[The files that describe how to start the container.]{#docker-containers-page-files explanation="Those files help define the setup. A running program answers the request."}
::option[Docker's list of containers on the machine.]{#docker-containers-page-list explanation="The container list describes what Docker is running. It does not serve the web page."}
:::

## The Container and Its Host

The machine running the containers is called the **host**. With Docker running Linux containers on Linux, the programs run as processes on that Linux host. A **process** is a running program. Each container can see a restricted set of resources, even though several containers share the same host. On Docker Desktop, Linux containers run inside a Linux virtual machine managed by Docker.

:::single-choice{#docker-containers-shared-host} Two Linux containers run on the same Linux host. What does that tell you?

::option[Their programs must use the same view of the files.]{#docker-containers-host-shared-files explanation="Each container can have its own view of files on the same host."}
::option[Their programs can run as separate processes on that host.]{#docker-containers-host-separate-processes .correct explanation="A shared host can run separate containerized programs."}
::option[Each container must start a separate Linux machine.]{#docker-containers-host-separate-machines explanation="Linux containers can run as processes on one host without starting a machine for each one."}
:::

## Starting from an Image

Docker creates a container from an **image**, a package that supplies the program and the files it needs. You can use the same web server image to create `web` and `demo`. When started, each container runs a separate process for the same server program. You can stop either container independently.

:::single-choice{#docker-containers-two-from-image} You stop demo while web is still running. What happens to web?

::option[It pauses until demo starts again.]{#docker-containers-two-paused explanation="Each container runs its own program. Stopping demo does not pause web in this setup."}
::option[It needs to be created again from the image.]{#docker-containers-two-recreate explanation="The existing web container was created separately and can stay running."}
::option[It keeps running in its own container.]{#docker-containers-two-independent .correct explanation="The two containers share an image as a starting point and run independently."}
:::

## Checking a Service Before and After It Stops

Suppose the browser is already set up to send requests to `web`. Before you stop it, the browser receives the page. After you stop it, a fresh request no longer gets the page from that server. The image is still available for another container. A server needs a running program and a way for the browser to reach it. A later lesson shows how to connect the browser to a container.

:::single-choice{#docker-containers-stopped-server} The image is still available, but web has stopped. What is needed for web itself to answer again?

::option[Its server program must be running again.]{#docker-containers-stopped-program .correct explanation="The image supplies the files. A running server program handles new requests."}
::option[The image needs a new name before it can serve pages.]{#docker-containers-stopped-rename explanation="Renaming a package does not make a stopped server run."}
::option[The browser needs another copy of the server image.]{#docker-containers-stopped-browser-image explanation="The browser sends requests. The server program runs in the container."}
:::

![LabEx Terminal showing an HTTP 200 response before the container stops and a failed connection afterward](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-containers/server-response.png)

In this LabEx example, a container named `page-demo` serves the page. The first `curl` request gets HTTP 200. After the container stops, a fresh request fails. Curl prints `000` because it received no HTTP response.

## Summary

You can now explain how a container runs a program on a host.

1. Identify the program that responds to a browser request.
2. Explain how containers can share a host.
3. Describe how one image can supply multiple containers.
4. Use a fresh request to observe whether a previously reachable server is still answering.
