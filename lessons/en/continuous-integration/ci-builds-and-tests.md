---
lesson_id: "ci-builds-and-tests"
course_id: "continuous-integration"
lang: "en"
order_index: 4
title: "Builds and Tests"
description: "Learn to distinguish preparation, building, and testing by running a small page check locally."
meta_title: "Builds and Tests - Continuous Integration"
meta_description: "Learn to distinguish preparation, building, and testing by running a small page check locally."
meta_keywords: "builds and tests, continuous integration, devops, Linux Journey"
---

A check that fails is easier to interpret when each stage has one job. **Preparation** makes inputs and tools available. A **build** creates output. A **test** checks an expectation against the source or output.

## Preparing the Input

In an empty practice folder, write an example page. The redirection replaces `index.html` if the file exists, so use a fresh practice directory.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
```

In a CI job checkout would provide the page. Some projects also install dependencies, which are the libraries or tools required to run their build or tests.

:::single-choice{#ci-builds-and-tests-prepare-input} The page is missing before the command that copies it. Which stage should you investigate first?

::option[Artifact download in a later job.]{#ci-builds-and-tests-prepare-input-a explanation="The missing input is needed before building this output."}
::option[Preparation.]{#ci-builds-and-tests-prepare-input-b .correct explanation="The input file should have been made available in this job."}
::option[Production response time.]{#ci-builds-and-tests-prepare-input-c explanation="The scenario concerns files on the runner."}
:::

## Building the Output

Copy the page to a directory used for the finished site.

```bash
$ mkdir -p dist
$ cp index.html dist/index.html
```

The `-p` option lets `mkdir` succeed when the directory already exists. Copying makes a separate file in the output directory. Subsequent tests can inspect this output.

:::single-choice{#ci-builds-and-tests-build-product} Which file is ready to package after the copy succeeds?

::option[Dist/index.html.]{#ci-builds-and-tests-build-product-a .correct explanation="The build placed a copy in the output directory."}
::option[A deployed page on the public site.]{#ci-builds-and-tests-build-product-b explanation="Copying the file locally creates no running service."}
::option[A workflow status record.]{#ci-builds-and-tests-build-product-c explanation="The build here produces a page, while the runner tracks check status separately."}
:::

## Testing the Page

Run this check immediately after building. The `-F` option looks for literal text and `-q` keeps the result quiet. The shell stores the last command's exit code in `$?`. Zero means the text was found. One means there was no matching line.

```bash
$ grep -Fq '<h1>Welcome</h1>' dist/index.html
$ echo "$?"
```

Expect `0`. The test checked for the exact text in the built file. It had no expectation about colors, browser rendering, or response time.

:::single-choice{#ci-builds-and-tests-test-scope} This test passes. Which conclusion follows?

::option[The page is accessible from the internet.]{#ci-builds-and-tests-test-scope-a explanation="The check read a local output file."}
::option[The page renders in every supported browser.]{#ci-builds-and-tests-test-scope-b explanation="No browser was used for this test."}
::option[The built file contains the expected heading string.]{#ci-builds-and-tests-test-scope-c .correct explanation="That is the condition the grep command checked."}
:::

![Successful local heading check with shell exit code zero on LabEx](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-builds-and-tests/heading-check.png)

## Summary

You can now tell what each stage of a small CI check proves.

1. Prepare the input before running the build.
2. Identify the file produced by the build.
3. Interpret the exit code and the exact scope of the test.
