---
lesson_id: "compose-environment-variables"
course_id: "docker-compose"
lang: "en"
order_index: 5
title: "Environment Variables"
description: "Learn to distinguish a value substituted into a Compose file from a value passed into a container."
meta_title: "Environment Variables - Docker Compose"
meta_description: "Learn to distinguish a value substituted into a Compose file from a value passed into a container."
meta_keywords: "environment variables, docker compose, devops, Linux Journey"
---

An environment variable is a named value a program can read. Compose can use variables in two places. It can substitute a value while reading the file, and it can pass values to a program inside a container.

## Substituting a Value in the File

Save this as `compose.env.yaml` in your practice folder. In this file, `${PAGE_MODE:-demo}` means to use `PAGE_MODE` when its value is set and nonempty and otherwise to use `demo`.

```yaml
services:
  toolbox:
    image: busybox:1.36
    environment:
      PAGE_MODE: "${PAGE_MODE:-demo}"
```

Compose resolves the expression before creating the container. This is called **interpolation**. In other files you may see the same technique used to select a host port or image tag.

:::single-choice{#compose-environment-variables-interpolate-default} If PAGE_MODE is unset, which value appears in the rendered configuration?

::option[The literal expression from the file.]{#compose-environment-variables-interpolate-default-a explanation="Compose resolves the expression when it reads the file."}
::option[An automatically generated container name.]{#compose-environment-variables-interpolate-default-c explanation="Naming the container and choosing an environment value are separate settings."}
::option[Demo, the value after the default operator.]{#compose-environment-variables-interpolate-default-b .correct explanation="The expression specifies demo as the fallback."}
:::

## Viewing the Resolved Value

A variable assignment before a command sets the variable for that invocation. Use it to see what a different value would do. The `config` command prints resolved settings and creates no container.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml config
```

Look for `PAGE_MODE: review` under the service's environment. The value `review` is a demonstration setting. Keep secrets out of sample configuration and printed output.

:::single-choice{#compose-environment-variables-config-scope} The rendered file shows review. What has happened so far?

::option[A service has already started with that value.]{#compose-environment-variables-config-scope-b explanation="Rendering the file is a separate operation from starting a container."}
::option[Compose substituted the value while reading the configuration.]{#compose-environment-variables-config-scope-a .correct explanation="The config command shows resolved settings before anything is launched."}
::option[Every existing container now uses the value.]{#compose-environment-variables-config-scope-c explanation="This invocation does not change running containers."}
:::

## Passing a Value into the Container

The `environment` section passes the resolved setting into a new container. Use `printenv` to ask the program inside the one-off container to print that value.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml run --rm toolbox printenv PAGE_MODE
```

Expect `review`. Interpolation selected the value. The environment entry delivered it to the container. A variable used only to choose a host port would not automatically become part of the program's environment.

:::single-choice{#compose-environment-variables-actual-value} Which action checks the value the program inside the toolbox receives?

::option[Print PAGE_MODE from the container.]{#compose-environment-variables-actual-value-c .correct explanation="The program's own environment is the evidence for what it received."}
::option[Read the default value in the original file only.]{#compose-environment-variables-actual-value-a explanation="Another value may override the file's default."}
::option[Find the toolbox IP address.]{#compose-environment-variables-actual-value-b explanation="The address does not reveal program settings."}
:::

## Summary

You can now tell the two uses of environment variables apart.

1. Read a default expression in a Compose file.
2. Inspect the resolved configuration before launching a container.
3. Check a value in the environment of the launched program.
