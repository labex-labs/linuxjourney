---
lesson_id: "docker-images"
course_id: "docker"
lang: "en"
order_index: 2
title: "Images"
description: "Learn how to read an image reference and check whether the referenced image is available locally."
meta_title: "Images - Docker"
meta_description: "Read Docker image names and tags, understand registries and pulls, and distinguish an image listing from a container listing."
meta_keywords: "Docker images, image tags, image registry, docker pull, docker image ls"
---

A Docker image packages a program, its files, and default settings. Docker uses that package as the starting point for a container. Here you will read image names and find out which images Docker already has.

## Reading an Image Name and Tag

In `nginx:alpine`, `nginx` is the image name and `alpine` is the **tag**, a label used to select a particular release or variant. Here it selects a variant built on Alpine Linux. The colon separates the name from the tag. `nginx:alpine` and `nginx:latest` are different references to the same image name.

:::single-choice{#docker-images-read-reference} In `busybox:1.36`, which part is the tag?

::option[`busybox`]{#docker-images-reference-name explanation="Busybox is the name before the colon."}
::option[`busybox:1.36`]{#docker-images-reference-whole explanation="The full reference includes the image name and the tag."}
::option[`1.36`]{#docker-images-reference-tag .correct explanation="The text after the colon is the tag used to select the image."}
:::

## Choosing a Tag

When you omit the tag from a reference such as `nginx`, Docker uses `latest`. That is a tag name chosen by convention. A publisher can decide which image a tag points to and can update it later. Using `nginx:alpine` states which variant you want, even though that tag can receive updates too.

:::single-choice{#docker-images-default-tag} A colleague runs `nginx` without a tag and assumes Docker chose the newest release. What did the reference actually select?

::option[The image pointed to by the latest tag.]{#docker-images-default-latest .correct explanation="Omitting the tag selects latest. The publisher decides which image that tag points to."}
::option[The most recently published Nginx image.]{#docker-images-default-newest explanation="Docker uses the tag name latest. It does not sort images by publication time."}
::option[The smallest available Nginx image.]{#docker-images-default-smallest explanation="Image size does not select a default tag. Choose the desired variant by name."}
:::

## Downloading an Image

A **registry** stores and serves images. Docker Hub is the registry Docker uses by default for references such as `nginx:alpine`. To download an image to the Docker environment you are connected to, use `docker pull`. Downloading is sometimes called **pulling** an image.

```bash
$ docker pull nginx:alpine
```

After this command succeeds, the image is available there. Starting a container is a separate action. In transcript examples, the `$` is the terminal prompt.

:::single-choice{#docker-images-pull-result} An image pull finishes successfully. What has Docker done?

::option[Started a container that answers web requests.]{#docker-images-pull-started explanation="A container starts when you run it. Pulling only makes the image available."}
::option[Made the image available for use in that environment.]{#docker-images-pull-available .correct explanation="You can now use the downloaded image as the starting point for a container."}
::option[Uploaded a copy of the image to the registry.]{#docker-images-pull-uploaded explanation="Pull transfers the image from the registry to Docker's local storage."}
:::

## Checking Local Images

Use `docker image ls` to see images already available. This example shows just the name and tag columns. Docker labels the image name column `REPOSITORY`.

```text
$ docker image ls
REPOSITORY   TAG
nginx        alpine
busybox      1.36
```

The first row shows `nginx:alpine`. This table answers which images are present. It has no column for the state of a container created from those images.

![LabEx Terminal showing docker pull and the repository and tag columns in docker image ls](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-images/pull-and-list.png)

The image list in this capture is filtered to the two references used in the lesson.

:::single-choice{#docker-images-local-list} Which reference is shown as available in this output?

::option[`busybox:latest`]{#docker-images-local-busybox-latest explanation="The busybox row shows the 1.36 tag. The sample has no busybox row with a latest tag."}
::option[`busybox:1.36`]{#docker-images-local-busybox .correct explanation="Combine busybox from the REPOSITORY column with 1.36 from the TAG column."}
::option[`nginx:1.36`]{#docker-images-local-nginx-mixed explanation="Keep the name and tag on the same row. The 1.36 tag belongs to the busybox row here."}
:::

## Summary

You can now read an image reference and check whether it appears in the local image list.

1. Identify the name and tag in an image reference.
2. Explain what happens when you leave out the tag.
3. Use `docker pull` to download an image from a registry.
4. Read the name and tag columns in `docker image ls`.
