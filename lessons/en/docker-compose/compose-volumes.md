---
lesson_id: "compose-volumes"
course_id: "docker-compose"
lang: "en"
order_index: 4
title: "Volumes"
description: "Learn why a named volume keeps files across container replacements."
meta_title: "Volumes - Docker Compose"
meta_description: "Learn why a named volume keeps files across container replacements."
meta_keywords: "volumes, docker compose, devops, Linux Journey"
---

A container can write a file in its own writable layer. If you remove that container, Docker removes that layer. A **named volume** is storage that Docker manages separately. You can attach it to a replacement container.

## Defining a Practice Volume

Save this separate example as `compose.volume.yaml` in the practice directory. It maps storage named `notes` to the path `/data` inside the toolbox. The bottom `volumes` section declares the named storage.

```yaml
services:
  toolbox:
    image: busybox:1.36
    volumes:
      - notes:/data
volumes:
  notes:
```

The service definition controls where the mount appears inside a container. The top-level declaration tells Compose to manage that volume with the project.

:::single-choice{#compose-volumes-attached-path} Which path inside the toolbox uses the named volume?

::option[/notes.]{#compose-volumes-attached-path-b explanation="Notes is the volume's name rather than the path mounted inside the container."}
::option[/data.]{#compose-volumes-attached-path-a .correct explanation="The right side of notes:/data is the container path."}
::option[Every path inside the container.]{#compose-volumes-attached-path-c explanation="The volume covers the configured directory."}
:::

## Writing and Reading with Separate Containers

The `-f` option selects the alternate file and `-p` gives it a separate project name. The `run --rm` command creates a one-off container and removes it after it finishes. Run these in the isolated practice folder. The first command overwrites the test file at `/data/note.txt`.

```bash
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox sh -c 'echo ready > /data/note.txt'
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox cat /data/note.txt
```

The second container should print `ready`. It mounts the same volume as the first one.

:::single-choice{#compose-volumes-persistence} Why can the second container read the file after the first one was removed?

::option[Both containers mounted the named volume.]{#compose-volumes-persistence-b .correct explanation="The file was written to the separate storage attached at /data."}
::option[Both containers kept the first one's writable layer.]{#compose-volumes-persistence-a explanation="The first container's layer was removed with it."}
::option[BusyBox automatically added the file to its image.]{#compose-volumes-persistence-c explanation="Running a container leaves the original image unchanged."}
:::

![Two separate toolbox containers writing and reading the same named-volume file](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-volumes/persisted-note.png)

## Keeping Data Intentional

A filename such as `/tmp/note.txt` outside the mounted directory stays with that container unless some other storage covers it. Inspect the paths before assuming a file is protected. Deleting the volume itself can erase its data. A backup is a separate copy that you can restore if the volume is lost.

:::single-choice{#compose-volumes-inside-mount} Which file would the next toolbox container see through this volume?

::option[/tmp/note.txt from the first toolbox's writable layer.]{#compose-volumes-inside-mount-a explanation="This path is outside the configured mount."}
::option[A file stored in a differently named volume.]{#compose-volumes-inside-mount-b explanation="The new container must mount that other volume to see it."}
::option[/data/note.txt written by the first toolbox.]{#compose-volumes-inside-mount-c .correct explanation="The mount at /data gives each container access to the same stored file."}
:::

## Summary

You can now explain why a file can outlive the container that wrote it.

1. Read the volume name and the mount path.
2. Verify persistence by reading the file from a separate container.
3. Keep volume deletion and container replacement distinct.
