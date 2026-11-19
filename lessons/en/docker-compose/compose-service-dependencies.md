---
lesson_id: "compose-service-dependencies"
course_id: "docker-compose"
lang: "en"
order_index: 6
title: "Service Dependencies"
description: "Learn to distinguish dependency startup order from a service that is ready to answer requests."
meta_title: "Service Dependencies - Docker Compose"
meta_description: "Learn to distinguish dependency startup order from a service that is ready to answer requests."
meta_keywords: "service dependencies, docker compose, devops, Linux Journey"
---

A helper that needs a web server can start in the right order and still make its first request too early. A **health check** is a small test run by Docker to observe whether a service can do something useful, such as answer an HTTP request.

## Choosing a Readiness Check

In this separate example the check runs inside the web container. It requests the local web page. A successful request gives Docker evidence that the server is answering from that location.

```yaml
services:
  web:
    image: nginx:alpine
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "/dev/null", "http://127.0.0.1/"]
      interval: 3s
      timeout: 2s
      retries: 5
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
    depends_on:
      web:
        condition: service_healthy
```

Save this as `compose.health.yaml` in the same practice folder. The check runs at intervals and has a time limit per attempt. It checks a local response inside the web container.

:::single-choice{#compose-service-dependencies-check-location} Where does wget run for this health check?

::option[In the web container.]{#compose-service-dependencies-check-location-c .correct explanation="The loopback URL is evaluated from inside that container."}
::option[In the host's browser.]{#compose-service-dependencies-check-location-a explanation="This is a command run by Docker according to the web service definition."}
::option[In the toolbox container.]{#compose-service-dependencies-check-location-b explanation="The check is defined under web."}
:::

## Waiting for a Healthy Dependency

The `service_healthy` condition makes Compose wait for a successful health check before starting the dependent toolbox. Simple startup ordering can start a dependent as soon as the dependency is running. That can be earlier than its first successful request.

```bash
$ docker compose -p journey-health -f compose.health.yaml up -d
$ docker compose -p journey-health -f compose.health.yaml ps
```

Look for a healthy state on the web row and a running toolbox.

:::single-choice{#compose-service-dependencies-ready-condition} The web process started but its local request still fails. Which condition should delay starting the toolbox?

::option[Startup order alone.]{#compose-service-dependencies-ready-condition-b explanation="Starting web first can still leave a gap before it answers."}
::option[Selecting detached mode.]{#compose-service-dependencies-ready-condition-c explanation="Detach changes how the terminal waits. It does not define readiness."}
::option[Service healthy.]{#compose-service-dependencies-ready-condition-a .correct explanation="The dependency condition waits for the health result."}
:::

![Compose status showing a healthy web dependency and the running toolbox](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-dependencies/healthy-dependency.png)

## Handling a Later Failure

A Compose startup condition makes an initial ordering decision. A previously healthy service can still stop answering after startup. A client should handle a failed request and reconnect when the dependency becomes available. Use the service state and a direct request to check the present behavior.

:::single-choice{#compose-service-dependencies-later-failure} A request fails an hour after both services started. Which evidence helps now?

::option[The original startup order alone.]{#compose-service-dependencies-later-failure-a explanation="It describes what happened at startup."}
::option[A current health result and a request from the dependent service.]{#compose-service-dependencies-later-failure-b .correct explanation="These observations help distinguish the present service state and the client's path."}
::option[The number of images in the Docker cache.]{#compose-service-dependencies-later-failure-c explanation="Image availability says little about a running service's response."}
:::

## Checking Two Points of View

A successful local health check shows what the web container can reach from inside itself. The toolbox still needs the project network and a usable service address. Check the health result and the request from the toolbox separately.

:::single-choice{#compose-service-dependencies-final-application} Health is green but one request from the toolbox fails. Which comparison helps locate the problem?

::option[Read only the original startup time.]{#compose-service-dependencies-final-application-b explanation="Startup timing does not show what each path can reach now."}
::option[Declare both requests successful because the web health is green.]{#compose-service-dependencies-final-application-c explanation="The health check gives evidence from one location."}
::option[Compare the same request from inside web with a request to web from the toolbox.]{#compose-service-dependencies-final-application-a .correct explanation="These checks compare readiness inside the service with the path its dependent actually uses."}
:::

## Summary

You can now use a check to reason about whether a dependency is ready.

1. Identify what a health check actually observes.
2. Choose a healthy dependency condition when startup order is insufficient.
3. Verify current behavior if a service fails later.
