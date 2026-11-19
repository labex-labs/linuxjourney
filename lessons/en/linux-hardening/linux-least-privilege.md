---
lesson_id: "linux-least-privilege"
course_id: "linux-hardening"
lang: "en"
order_index: 3
title: "Least Privilege"
description: "Learn to choose file and administrative permissions for a specific service task."
meta_title: "Least Privilege - Linux Hardening"
meta_description: "Learn to choose file and administrative permissions for a specific service task."
meta_keywords: "least privilege, linux hardening, cybersecurity, Linux Journey"
---

**Least privilege** means giving an account the access required for its job. Start with verbs. The account may need to read one file, write another, and perform no administrative work.

## Matching Rights to Work

A web worker needs to read `index.html`. The deployment account updates it. These two jobs can use different permissions. The worker can read the page and the deployer can write it.

:::single-choice{#linux-least-privilege-read-only-page} Which page permission does the worker need for this example?

::option[Read access.]{#linux-least-privilege-read-only-page-a .correct explanation="Serving the file requires reading its contents."}
::option[Write access.]{#linux-least-privilege-read-only-page-b explanation="The deployment account changes the page."}
::option[Permission to administer unrelated services.]{#linux-least-privilege-read-only-page-c explanation="That work is outside the web worker's task."}
:::

## Checking the Whole Path

File permissions are only one part of the check. Linux also needs permission to enter the directories leading to the file. On a directory, the execute permission allows the program to traverse it when it knows the name it needs. A readable file behind a directory the worker cannot traverse is still inaccessible to that worker.

:::single-choice{#linux-least-privilege-path-boundary} The worker can read index.html according to the file mode, but it cannot enter the parent directory. What should you review?

::option[Whether the page has a larger file size.]{#linux-least-privilege-path-boundary-a explanation="Size does not grant directory access."}
::option[Whether to let everyone write the page.]{#linux-least-privilege-path-boundary-c explanation="Write permission does not fix the missing path access."}
::option[The directory's traversal permission for the worker.]{#linux-least-privilege-path-boundary-b .correct explanation="The worker needs access through the path as well as to the file."}
:::

## Limiting Special Actions

Administrative tools such as `sudo` can allow an approved user to perform specific maintenance. Define the action, who is approved to perform it, and how you can verify the new access. Check that the approved maintenance still works and that an unrelated administrative action remains unavailable under the same policy.

:::single-choice{#linux-least-privilege-policy-test} A maintenance role should review service status. Which test plan best checks the intended permissions?

::option[Check that every administrative command now succeeds.]{#linux-least-privilege-policy-test-a explanation="The extra rights would exceed the documented task."}
::option[Check that the role can inspect status and that unrelated privileged changes remain restricted.]{#linux-least-privilege-policy-test-c .correct explanation="This tests both necessary access and the intended boundary."}
::option[Check only that the username exists.]{#linux-least-privilege-policy-test-b explanation="An existing account does not demonstrate its permissions."}
:::

## Summary

You can now reason about the minimum access a task needs.

1. Separate read, write, and administrative actions.
2. Check access through the directories in a path.
3. Verify both allowed and restricted actions for a role.
