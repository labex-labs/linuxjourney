---
lesson_id: "build-release-deploy"
course_id: "deployment"
lang: "en"
order_index: 1
title: "Build, Release, and Deploy"
description: "Learn to trace a source revision through its build, release, and deployment records."
meta_title: "Build, Release, and Deploy - Deployment"
meta_description: "Learn to trace a source revision through its build, release, and deployment records."
meta_keywords: "build, release, and deploy, deployment, devops, Linux Journey"
---

A teammate says version 2 is ready. That could mean its files were built, a version was approved, or visitors can already reach it. Follow the records to see which stage has happened.

## Identifying the Build

A build turns a particular source revision into an output. The example packages a small website as a container image and stores it in an image registry. Record the source commit beside the resulting image reference.

```text
Build 81
Source commit: 3ab4501
Image: registry.example/journey/site:2
Result: succeeded
```

This record shows what was produced. The site may still be running an earlier version.

:::single-choice{#build-release-deploy-build-record} Which record connects the packaged image to the source revision?

::option[A browser bookmark.]{#build-release-deploy-build-record-b explanation="A bookmark names an address without recording how its files were built."}
::option[Build 81.]{#build-release-deploy-build-record-a .correct explanation="It names both the source commit and the resulting image."}
::option[The newest local branch name.]{#build-release-deploy-build-record-c explanation="A branch name can move and does not identify this build."}
:::

## Reading the Release

A **release** identifies an approved version for distribution. For example, a release record might approve the exact image from build 81 for staging. That makes it possible to refer to the same artifact after approval without building a new copy.

:::single-choice{#build-release-deploy-release-record} Release 2 is approved for staging. What does that establish?

::option[The recorded artifact is approved for that use.]{#build-release-deploy-release-record-b .correct explanation="The release records which artifact was authorized for staging."}
::option[Every environment already serves version 2.]{#build-release-deploy-release-record-a explanation="Approval gives permission to proceed and does not record a running version."}
::option[Version 2 has a higher request rate.]{#build-release-deploy-release-record-c explanation="A release record does not measure traffic."}
:::

## Finding the Deployed Version

A **deployment** places a particular version in an environment and starts or updates the workload there. An environment is a place such as staging or production with its own settings and resources. A successful request to a version endpoint can help check which version answers there.

```text
Staging version response: 2
Production version response: 1
```

In this example the new version responds in staging, while production still responds with version 1.

:::single-choice{#build-release-deploy-running-version} A reviewer wants evidence that version 2 serves production. Which observation would directly help?

::option[A second staging response with version 2.]{#build-release-deploy-running-version-a explanation="That still checks staging."}
::option[The release's approval message.]{#build-release-deploy-running-version-b explanation="Approval does not test the running service."}
::option[A version response from the production address.]{#build-release-deploy-running-version-c .correct explanation="It checks the environment the reviewer asked about."}
:::

## Summary

You can now distinguish the records created along a release path.

1. Connect a build output to its source.
2. Identify the artifact approved in a release.
3. Confirm the version answering in the intended environment.
