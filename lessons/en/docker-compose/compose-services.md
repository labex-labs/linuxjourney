---
lesson_id: "compose-services"
course_id: "docker-compose"
lang: "en"
order_index: 2
title: "Compose Services"
description: "Learn to start Compose services and check their container states."
meta_title: "Compose Services - Docker Compose"
meta_description: "Learn to start Compose services and check their container states."
meta_keywords: "compose services, docker compose, devops, Linux Journey"
---

Use the `compose.yaml` with `web` and `toolbox` from the previous lesson. Both services belong to one Compose **project**, the group of resources managed together using this configuration. Run the commands from the practice folder.

## Starting the Project

If port 8080 is already in use, choose a free host port in `compose.yaml`. For example, the `published-web` container from the Docker course uses port 8080 while it is running. You can keep it running and set the Compose mapping to `127.0.0.1:8081:80` if port 8081 is available. Keep port 80 on the container side and use your chosen host port in later browser requests.

Use `docker compose up -d` to start the services in the background. Compose creates required project resources and uses the service settings to create or update containers.

```bash
$ docker compose up -d
```

:::single-choice{#compose-services-project-start} You run up -d from this practice folder. Which settings determine what starts?

::option[Every image available on the Docker host.]{#compose-services-project-start-a explanation="The host can store images unrelated to this project."}
::option[All containers that happen to have stopped.]{#compose-services-project-start-c explanation="Compose works with the project it was asked to start."}
::option[The services in the selected Compose file.]{#compose-services-project-start-b .correct explanation="Compose uses the definitions of web and toolbox in this example."}
:::

## Reading the Service List

Use `docker compose ps` to inspect this project. Its service column shows the names from the YAML file. Docker also assigns each container a name, which can contain the project name.

```bash
$ docker compose ps
```

Look for `web`, `toolbox`, and their statuses. A running container is evidence that the program is running at the time of the check. Use a browser request to verify the web response separately.

:::single-choice{#compose-services-compose-list} Compose reports web as running. What further check directly confirms it returns the expected page?

::option[Count the services listed by config.]{#compose-services-compose-list-b explanation="The file count is independent of the web response."}
::option[Request the published web address.]{#compose-services-compose-list-a .correct explanation="The request tests whether the actual page is served."}
::option[Check the name of another container.]{#compose-services-compose-list-c explanation="A container name identifies the instance and does not test the service."}
:::

![Compose status showing the running web and toolbox services and host port 8080](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-services/project-status.png)

The screenshot uses the original host port, 8080. If you chose a different port, look for that number on the host side of the mapping.

## Checking a Stopped Service

The toolbox is temporary. If it finishes sleeping or you stop it, add `-a` to include stopped containers in the Compose list. The example command below stops the helper in this practice project while leaving the web service running. Start the helper again when you want to continue the course.

```bash
$ docker compose stop toolbox
$ docker compose ps -a
$ docker compose start toolbox
```

:::single-choice{#compose-services-stopped-service} Where should you look for the toolbox after stopping it?

::option[In this project's docker compose ps -a output.]{#compose-services-stopped-service-c .correct explanation="The all option includes stopped project containers."}
::option[In the image list only.]{#compose-services-stopped-service-a explanation="Stopping its running program leaves the container available for inspection."}
::option[In a container list for a different project.]{#compose-services-stopped-service-b explanation="The toolbox belongs to this project."}
:::

For more container and Compose practice, see [Docker Command Labs](https://labex.io/courses/docker-command-labs).

## Summary

You can now use a Compose file to start and inspect a group of services.

1. Start the services in the selected project.
2. Find the service name and current status.
3. Include stopped services when investigating the project.
