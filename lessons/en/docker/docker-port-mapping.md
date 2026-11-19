---
lesson_id: "docker-port-mapping"
course_id: "docker"
lang: "en"
order_index: 5
title: "Port Mapping"
description: "Learn how to publish a container port and find the address a local browser should use."
meta_title: "Port Mapping - Docker"
meta_description: "Read Docker port mappings, distinguish host and container ports, and diagnose a request sent to the wrong port."
meta_keywords: "Docker port mapping, published ports, docker run -p, host port, container port"
---

A web server can be running inside a container while your browser still needs a way to reach it. A **port** is a number that helps a machine direct incoming network requests to the right service. Docker can publish a host port to pass those requests to a port inside the container.

## Reading a Port Mapping

The Nginx server in this example accepts web requests on port 80 inside the container. The `web` container from the earlier example was created without a published port. Here, give a new container its own name and use `-p` to set the mapping when you create it.

```bash
$ docker run -d --name published-web -p 127.0.0.1:8080:80 nginx:alpine
```

Read `8080:80` as from **host port** 8080, where the browser connects, to **container port** 80, where the server receives the request. The address `127.0.0.1` binds the mapping to the host's loopback address, the address a machine uses to reach itself.

Use a private practice environment. In Docker Engine versions earlier than 28.0.0, other machines on the same local network segment may be able to reach ports published to localhost. [Docker port publishing](https://docs.docker.com/engine/network/port-publishing/)

:::single-choice{#docker-port-mapping-request-target} In `127.0.0.1:9090:80`, which port should a browser on the Docker host contact?

::option[Port 9090 on the host.]{#docker-port-mapping-target-outer .correct explanation="The middle part selects the host port where the browser connects."}
::option[Port 80 on the host.]{#docker-port-mapping-target-inner explanation="Port 80 is the destination inside the container."}
::option[Port 9090 inside the container.]{#docker-port-mapping-target-wrong-side explanation="The server receives the request on its container port, which is 80 here."}
:::

## Testing from the Host

Open `http://127.0.0.1:8080` in a browser on the machine where Docker published the port. If Docker runs on a remote machine, typing `127.0.0.1` on your laptop points back at your laptop. For a browser-based lab, use the access method supplied by the lab environment.

:::single-choice{#docker-port-mapping-local-browser} Docker published port 8080 on a separate lab machine. Where does `127.0.0.1` point when typed into your laptop's browser?

::option[To the separate lab machine.]{#docker-port-mapping-local-lab explanation="That address refers to the lab machine only when used from the lab machine itself."}
::option[To the web container inside Docker.]{#docker-port-mapping-local-container explanation="The browser uses its own machine's address. A port mapping is what can forward a request to a container."}
::option[To your laptop.]{#docker-port-mapping-local-laptop .correct explanation="The loopback address refers to the machine where the browser is running."}
:::

## Checking What Docker Published

The `PORTS` column of `docker ps` can show the mapping. Here, the arrow points from the host address and port to the container port. The `/tcp` suffix names the network protocol used by this mapping.

```text
$ docker ps
STATUS         PORTS                   NAMES
Up 2 minutes   127.0.0.1:8080->80/tcp   published-web
```

A row can show `80/tcp` by itself. With no host address and arrow, that entry does not show a published host port.

![LabEx Terminal showing host port 8080 forwarding to container port 80 and a successful HTTP 200 response](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-port-mapping/loopback-mapping.png)

This capture filters the list to `published-web`. The `curl` request runs on the Docker host and confirms that the published address returns a successful response.

:::single-choice{#docker-port-mapping-read-listing} A row shows `80/tcp` with no arrow. What can you tell from that entry?

::option[Docker published port 80 on the host.]{#docker-port-mapping-listing-host explanation="A published mapping identifies a host port and points to the container port."}
::option[The entry shows a container port without a published host port.]{#docker-port-mapping-listing-container .correct explanation="The entry names port 80 inside the container. It has no host address or forwarding arrow."}
::option[Docker published port 8080 on the host.]{#docker-port-mapping-listing-default explanation="The entry contains no host port. Docker does not infer 8080 from it."}
:::

## Choosing the Address to Test

If the page fails to open, compare the address you entered with the left side of the mapping. An `Up` status and an arrow tell you what Docker is running and forwarding. A browser request checks whether the server actually returns the page.

:::single-choice{#docker-port-mapping-correct-misdirected} On the Docker host, you try port 8080 and get no page. The row shows `127.0.0.1:8081->80/tcp`. What should you try next?

::option[Open `http://127.0.0.1:80`.]{#docker-port-mapping-misdirected-80 explanation="Port 80 is on the container side of the mapping."}
::option[Open `http://127.0.0.1:8081`.]{#docker-port-mapping-misdirected-8081 .correct explanation="Use the published host port on the left side of the arrow."}
::option[Retry `http://127.0.0.1:8080`.]{#docker-port-mapping-misdirected-8080 explanation="The listed host port is 8081. Retrying 8080 does not test that mapping."}
:::

## Summary

You can now read a port mapping and use it to choose the correct browser address.

1. Distinguish the host port from the container port.
2. Explain where `127.0.0.1` points.
3. Recognize a published mapping in the container list.
4. Use the published host port to test the service.
