---
lesson_id: "ci-build-artifacts"
course_id: "continuous-integration"
lang: "en"
order_index: 6
title: "Build Artifacts"
description: "Learn to connect a file produced by CI to its run and source revision."
meta_title: "Build Artifacts - Continuous Integration"
meta_description: "Learn to connect a file produced by CI to its run and source revision."
meta_keywords: "build artifacts, continuous integration, devops, Linux Journey"
---

A **build artifact** is a file or collection of files saved from a run for later use. Examples include a test report or a site archive. Keeping the run and revision with the artifact helps a reviewer tell which source produced it.

## Packaging an Output Directory

Use the practice folder where `dist` contains the built page. This example makes a compressed archive, a single file holding the directory's contents. It replaces any existing archive of the same name in the current folder.

```bash
$ tar -czf site.tar.gz -C dist .
$ tar -tzf site.tar.gz
```

In the first command, `-c` creates the archive, `-z` compresses it, and `-f` names the output file. `-C dist .` tells tar to start in `dist`. The second command uses `-t` to list what was packed. Find `./index.html` before making the archive available.

:::single-choice{#ci-build-artifacts-inspect-archive} Which command checks that the page was included?

::option[Listing the archive with tar -tzf site.tar.gz.]{#ci-build-artifacts-inspect-archive-b .correct explanation="The listing shows whether index.html is inside."}
::option[Creating the archive once more.]{#ci-build-artifacts-inspect-archive-a explanation="Repeating the build does not show the entries to review."}
::option[Reading the name alone.]{#ci-build-artifacts-inspect-archive-c explanation="The archive name gives no evidence about its contents."}
:::

![Tar archive listing showing index.html inside site.tar.gz](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-build-artifacts/archive-contents.png)

## Linking an Artifact to a Run

A workflow can upload the finished archive. The run page shows which revision it built. Two artifacts named `site.tar.gz` can be different if they came from different revisions. Use the run and revision together when choosing which file to download.

:::single-choice{#ci-build-artifacts-choose-run} Runs 41 and 42 contain site.tar.gz. Which identifies the package for the revision you reviewed?

::option[The first download named site.tar.gz.]{#ci-build-artifacts-choose-run-b explanation="The name does not tell you which source produced it."}
::option[The latest successful run regardless of its revision.]{#ci-build-artifacts-choose-run-c explanation="A later run can be successful for different source files. Match the revision you intend to use."}
::option[The run whose recorded revision matches the review.]{#ci-build-artifacts-choose-run-a .correct explanation="The filename can be reused by several runs."}
:::

## Distinguishing an Archive and a Container Image

A site archive contains files that you can unpack. A container image includes the packaged filesystem and settings Docker uses to start a container. A workflow can publish an image to an image registry. Record the image reference with the source revision if the image is the item you intend to run.

:::single-choice{#ci-build-artifacts-deployable-type} The next stage expects to start a container from a registry. Which output should it reference?

::option[A test report downloaded from the run.]{#ci-build-artifacts-deployable-type-a explanation="A report describes results and provides no container filesystem."}
::option[The published container image reference.]{#ci-build-artifacts-deployable-type-c .correct explanation="Docker can use that reference to retrieve the prepared image."}
::option[The site archive's filename.]{#ci-build-artifacts-deployable-type-b explanation="It contains page files and does not identify a registry image."}
:::

## Summary

You can now identify a build artifact and trace where it came from.

1. Package and inspect the built files.
2. Check the producing run and source revision.
3. Choose a file artifact or a container image according to what the next step needs.
