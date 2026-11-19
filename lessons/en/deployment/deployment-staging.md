---
lesson_id: "deployment-staging"
course_id: "deployment"
lang: "en"
order_index: 3
title: "Staging"
description: "Learn what staging can verify and why the same artifact can behave differently across environments."
meta_title: "Staging - Deployment"
meta_description: "Learn what staging can verify and why the same artifact can behave differently across environments."
meta_keywords: "staging, deployment, devops, Linux Journey"
---

A release is almost ready. Run the artifact in **staging**, a practice environment designed to resemble the service users will rely on. This helps you check the release against realistic settings before exposing it to production traffic.

## Promoting the Same Artifact

Use the image that was tested and approved. If you build it again from changing dependencies, you may get a different artifact. Record the full image reference in each deployment.

```text
Environment  Artifact      Page configuration
staging      site@digest-A Internal preview
production   site@digest-A Public website
```

The example uses a symbolic digest. The artifact is the same and the settings differ.

:::single-choice{#deployment-staging-same-artifact} What shows that the same packaged code can be promoted to production?

::option[The artifact reference matches in both deployment records.]{#deployment-staging-same-artifact-b .correct explanation="The exact reference connects both environments to one build."}
::option[Both environments use the same label for a port.]{#deployment-staging-same-artifact-a explanation="Matching one setting does not establish artifact identity."}
::option[Both environments were deployed on the same day.]{#deployment-staging-same-artifact-c explanation="Time alone does not identify what was deployed."}
:::

## Choosing Representative Checks

Staging should let you exercise important behavior, such as loading the page and reading from a test dependency. Use authorized test accounts and test data. A successful staging check increases confidence about the scenario tested. Differences in traffic, data, or configuration can still matter after promotion.

:::single-choice{#deployment-staging-staging-scope} The staging page loads using a test database. What should you still verify after a real deployment?

::option[That the artifact no longer needs a version.]{#deployment-staging-staging-scope-b explanation="Version records remain useful during verification and recovery."}
::option[That every production request will succeed.]{#deployment-staging-staging-scope-c explanation="A small test sample cannot establish every future result."}
::option[That the production path works with its approved settings.]{#deployment-staging-staging-scope-a .correct explanation="The staging request did not exercise the production environment."}
:::

## Checking the Target Before Changing It

Read the target name and address before you apply a deployment. Afterward, use the same address to confirm the new version and important behavior. Keep staging and production details visible in your notes so a result has clear context.

:::single-choice{#deployment-staging-correct-target} You plan to deploy to staging. The command shows the production address. What should you do first?

::option[Continue and relabel the result as staging.]{#deployment-staging-correct-target-a explanation="The address determines which service receives the change."}
::option[Stop and confirm the intended target.]{#deployment-staging-correct-target-c .correct explanation="This avoids applying the change in the wrong environment."}
::option[Test from a different browser after deploying.]{#deployment-staging-correct-target-b explanation="The target should be corrected before the change starts."}
:::

For a hands-on CI/CD example, see [Continuous Deployment to Staging](https://labex.io/tutorials/cd-deployment-to-staging-636593).

## Summary

You can now use staging to check an approved artifact before promotion.

1. Keep the identity of the artifact across environments.
2. Choose checks that represent important user behavior.
3. Confirm the environment before changing it.
