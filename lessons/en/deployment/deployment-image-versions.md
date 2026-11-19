---
lesson_id: "deployment-image-versions"
course_id: "deployment"
lang: "en"
order_index: 2
title: "Image Versions"
description: "Learn to distinguish an image tag from a digest and compare the exact images two environments use."
meta_title: "Image Versions - Deployment"
meta_description: "Learn to distinguish an image tag from a digest and compare the exact images two environments use."
meta_keywords: "image versions, deployment, devops, Linux Journey"
---

A tag such as `site:2` makes an image reference easy to read. A publisher can move a tag when it pushes a replacement. To identify exact image content, record its **digest**, a value calculated from the referenced content.

## Reading a Tag

Imagine a registry shows these records on two different days. These abbreviated digest values are illustrative and cannot be used to pull an image.

```text
Monday    site:2    sha256:a1b2…
Tuesday   site:2    sha256:c3d4…
```

The same tag now points to different content. A machine that pulled on Monday may still use the older image.

:::single-choice{#deployment-image-versions-moving-tag} Both environments report the tag site:2. What would show which image each actually pulled?

::option[The shared tag alone.]{#deployment-image-versions-moving-tag-b explanation="Both different images in the example use the same tag."}
::option[The number of containers on either machine.]{#deployment-image-versions-moving-tag-c explanation="The count does not identify their images."}
::option[Their recorded digests.]{#deployment-image-versions-moving-tag-a .correct explanation="The tag can move while the digest identifies the content selected at pull time."}
:::

## Reading a Digest Reference

An image reference can use an `@` followed by the full digest. This asks the registry for that exact object. Use the full digest from the registry or build record. Shortened display values are useful in examples and insufficient to retrieve the image.

:::single-choice{#deployment-image-versions-fixed-reference} Which form selects a particular registry object?

::option[The image name without a tag.]{#deployment-image-versions-fixed-reference-a explanation="Docker applies a default tag that can move."}
::option[The image name followed by its full digest.]{#deployment-image-versions-fixed-reference-c .correct explanation="The digest refers to exact content."}
::option[A comment naming the day of the build.]{#deployment-image-versions-fixed-reference-b explanation="The registry cannot retrieve an object by a comment."}
:::

## Comparing Like for Like

An image name can point to a list of builds for different machine types, or to one image for a specific platform. When comparing what two hosts actually run, record their platform and compare the relevant platform-specific image references. Keep the original full reference in the release record.

:::single-choice{#deployment-image-versions-compare-platform} A release supports both arm64 and amd64. Which comparison is useful when checking two amd64 hosts?

::option[A comparison of the amd64 image references they selected.]{#deployment-image-versions-compare-platform-b .correct explanation="You are comparing the content intended for the same platform."}
::option[A comparison of different architecture image objects.]{#deployment-image-versions-compare-platform-a explanation="Those objects are expected to correspond to different platforms."}
::option[A comparison of their hostnames.]{#deployment-image-versions-compare-platform-c explanation="The names identify hosts and do not identify deployed content."}
:::

## Summary

You can now trace an exact image beyond its friendly tag.

1. Explain why the same tag can point to different content.
2. Recognize a full digest reference.
3. Compare the correct platform-specific image.
