---
lesson_id: "compose-service-discovery"
course_id: "docker-compose"
lang: "en"
order_index: 3
title: "Service Discovery"
description: "Learn how Compose services reach each other by name and how host access uses a published port."
meta_title: "Service Discovery - Docker Compose"
meta_description: "Learn how Compose services reach each other by name and how host access uses a published port."
meta_keywords: "service discovery, docker compose, devops, Linux Journey"
---

A browser on the Docker host reaches the web service at its published address. A second container in the project has a different route. Compose normally connects services in the same project to a shared network, where they can look each other up by service name.

## Requesting the Page from the Toolbox

Return to the practice folder that contains `compose.yaml`. If the toolbox has exited since the previous lesson, start it again with `docker compose start toolbox`. With both services running, use `docker compose exec` to run a command in the existing toolbox service. The BusyBox `wget` command requests a page. The `-q` option suppresses progress messages and `-O -` writes the page to the terminal.

```bash
$ docker compose exec -T toolbox wget -q -O - http://web:80/
```

The `-T` option disables allocation of an interactive terminal. The URL names the web service and its container port. Success returns the Nginx page HTML.

:::single-choice{#compose-service-discovery-sibling-url} Which address should another service on the same Compose network use for the web container?

::option[`http://web:80/`]{#compose-service-discovery-sibling-url-c .correct explanation="The shared network resolves web to the intended service and port 80 reaches its listener."}
::option[`http://127.0.0.1:8080/`]{#compose-service-discovery-sibling-url-a explanation="A loopback address inside that service points to its own network environment."}
::option[`http://web:8080/`]{#compose-service-discovery-sibling-url-b explanation="In this example the web program listens on port 80 inside the network."}
:::

![HTML returned inside the toolbox after requesting the web service by name](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-discovery/internal-request.png)

## Choosing an Address from the Host

On the Docker host, open `http://127.0.0.1:8080/` if you kept the original mapping. If you changed the host port in the previous lesson, use that port in the browser address. The toolbox still uses `http://web:80/` because it connects inside the Compose network, where the service name `web` is available.

:::single-choice{#compose-service-discovery-host-url} Suppose you change the host side of the mapping to 8081. Which example address also needs to change?

::option[The toolbox URL using web on port 80.]{#compose-service-discovery-host-url-b explanation="This connection still goes directly to the container listener."}
::option[Both example addresses.]{#compose-service-discovery-host-url-c explanation="Only the host-side port was changed."}
::option[The address used by the browser on the host.]{#compose-service-discovery-host-url-a .correct explanation="The browser connects through the new published host port."}
:::

## Keeping a Stable Service Name

When a container is replaced, its network address can change. Its Compose service name stays the same. A client can resolve the name again and reconnect. An already open connection to a replaced container may end.

:::single-choice{#compose-service-discovery-replacement} The web container was recreated and now has a different address. What can the toolbox use for its next request?

::option[The old address copied from the container.]{#compose-service-discovery-replacement-a explanation="A new instance can receive a different network address."}
::option[The same web service name and container port.]{#compose-service-discovery-replacement-b .correct explanation="The name can resolve to the current container on the project network."}
::option[The name of the toolbox itself.]{#compose-service-discovery-replacement-c explanation="That other service name identifies the command runner."}
:::

## Summary

You can now select a service address based on where a request starts.

1. Use a service name and container port within the project network.
2. Use a published address for the browser on the host.
3. Resolve the service name again after a container is replaced.
