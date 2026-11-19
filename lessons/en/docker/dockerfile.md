---
lesson_id: "dockerfile"
course_id: "docker"
lang: "en"
order_index: 7
title: "Dockerfile"
description: "Learn how a Dockerfile turns a page and a base image into a reusable web server image."
meta_title: "Dockerfile - Docker"
meta_description: "Read FROM, COPY, and CMD in a small Dockerfile and distinguish building an image from running a container."
meta_keywords: "Dockerfile, Docker build, FROM, COPY, CMD, build context"
---

You have used an existing web server image to start a container. To serve your own page, you can make an image that already contains it. A **Dockerfile** is a text file with instructions for building that image.

## Starting with a Base Image

A **base image** supplies the files and programs you start from. The following Dockerfile begins with the Nginx image, adds a page, and records the command the container should use by default. Keep the Dockerfile and a file named `index.html` in the same example directory. For the page, a single line such as `<h1>Hello from Docker</h1>` is enough.

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
CMD ["nginx", "-g", "daemon off;"]
```

`FROM nginx:alpine` starts from the named image, which already provides the Nginx program. Docker uses it while building the new image.

:::single-choice{#dockerfile-base-image-purpose} Which line supplies Nginx before your page is added?

::option[`COPY index.html /usr/share/nginx/html/index.html`]{#dockerfile-base-image-copy explanation="COPY adds the page. It relies on the server supplied by the base image."}
::option[`FROM nginx:alpine`]{#dockerfile-base-image-from .correct explanation="FROM selects the starting image, which already contains the server."}
::option[The line beginning with `CMD`.]{#dockerfile-base-image-cmd explanation="CMD sets the default startup command. The server program comes from the base image."}
:::

## Adding a File

`COPY` reads `index.html` from the files you give to the build. It writes the page to the path shown on the right, where this version of the Nginx image serves its default page. If you edit the local page later, rebuild the image to include the change.

:::single-choice{#dockerfile-copy-after-edit} You changed the heading in your local index.html after the build. How do you include that change in a new image?

::option[Start another container from the existing image.]{#dockerfile-copy-edit-run explanation="That container starts with the page already packaged in the existing image."}
::option[Change just the name of the existing container.]{#dockerfile-copy-edit-rename explanation="A container name does not change the files packaged in an image."}
::option[Build the image again with the updated page.]{#dockerfile-copy-edit-rebuild .correct explanation="The build runs COPY against the current local file and includes it in the image."}
:::

## Setting the Startup Command

`CMD` sets the default command for a new container. This example tells Nginx to keep running in the foreground inside the container. Docker can still run the container detached from your terminal when you use `docker run -d`.

:::single-choice{#dockerfile-cmd-start-time} When does the default CMD in the example take effect?

::option[When a container starts with its default command.]{#dockerfile-cmd-when-start .correct explanation="Docker uses the image's default command at container startup."}
::option[While Docker copies the page into the image.]{#dockerfile-cmd-when-copy explanation="COPY adds the page during the build. It does not run the server."}
::option[When Docker finishes writing the image.]{#dockerfile-cmd-when-build explanation="The build records the startup command for later use."}
:::

## Building and Running

Run the build from the directory that contains both files. The `-t` option assigns the image reference `journey-web:1`. The final dot tells Docker to use the current directory as the source of the build files.

```bash
$ docker build -t journey-web:1 .
$ docker run -d --name custom-web -p 127.0.0.1:8082:80 journey-web:1
```

The second command starts a container. If port 8082 is available, a browser on the Docker host can open `http://127.0.0.1:8082` to see the custom page.

:::single-choice{#dockerfile-build-versus-run} The build succeeded and you have yet to run the second command. What is ready?

::option[The image exists and can be used to create a container.]{#dockerfile-build-ready-image .correct explanation="The build produced the image. The next command will start a container from it."}
::option[The named container is already serving the custom page.]{#dockerfile-build-ready-container explanation="The server starts when you run the image in a container."}
::option[Docker has published the browser port for the image.]{#dockerfile-build-ready-port explanation="The port mapping is an option on docker run. Building does not set up that connection."}
:::

![LabEx Terminal showing the image build, container start, and HTML response from the custom page](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/dockerfile/build-and-run.png)

The final request retrieves the page packaged during the build. Build progress and image IDs may look different in your environment.

## Summary

You can now read a small Dockerfile and follow the path from a local page to a running server.

1. Identify a base image in `FROM`.
2. Describe where `COPY` reads and writes a file.
3. Recognize `CMD` as the container's default startup command.
4. Build an image and then start a container from it.
