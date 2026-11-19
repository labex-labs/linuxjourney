---
lesson_id: "linux-security-updates"
course_id: "linux-hardening"
lang: "en"
order_index: 7
title: "Security Updates"
description: "Learn to review available package updates and verify a service after approved maintenance."
meta_title: "Security Updates - Linux Hardening"
meta_description: "Learn to review available package updates and verify a service after approved maintenance."
meta_keywords: "security updates, linux hardening, cybersecurity, Linux Journey"
---

A security update can correct a defect in installed software. Begin by checking which software version is installed and what fix is available for your operating system. Plan the change around the service people use.

## Inspecting Available Updates

On an Ubuntu practice host, this read-only command lists packages that APT knows can be upgraded. It uses package information already present on the host.

```bash
$ apt list --upgradable
```

A listed package has a newer candidate in the available package data. Use your distribution's security notice to check whether that update contains the fix you need. An empty list can also mean the available information is out of date.

:::single-choice{#linux-security-updates-candidate-is-listed} A package appears in this list. What does that tell you?

::option[The update has already been applied.]{#linux-security-updates-candidate-is-listed-a explanation="The list describes an available upgrade candidate."}
::option[APT knows about a newer candidate for the installed package.]{#linux-security-updates-candidate-is-listed-b .correct explanation="This is what the local package information currently reports."}
::option[Every newer candidate is a security update.]{#linux-security-updates-candidate-is-listed-c explanation="Check the distribution's advisory for the reason for that update."}
:::

## Planning the Change

An approved change should name the service, target version, and maintenance window. Some updates require a service restart or a reboot to take effect. Plan a verification request and recovery option before changing the host.

:::single-choice{#linux-security-updates-reboot-check} A package update fixes code used by a long-running service. What should you check after installation?

::option[Whether the service needs to restart to use the updated code.]{#linux-security-updates-reboot-check-a .correct explanation="A running process may still have the old code loaded."}
::option[Whether the update was available in the package list before installation.]{#linux-security-updates-reboot-check-b explanation="Availability helps plan maintenance. It does not establish the version loaded by a process."}
::option[Whether the package list now shows no remaining upgrades.]{#linux-security-updates-reboot-check-c explanation="An up-to-date package list can coexist with a process that has not reloaded the updated code."}
:::

## Verifying the Result

Confirm the installed version matches the approved target. Check the service from the expected user path and record the result. If the fix concerns a running component, also confirm the updated version is actually in use.

:::single-choice{#linux-security-updates-security-verification} Which pair best supports completion after a service update?

::option[The list command runs twice.]{#linux-security-updates-security-verification-a explanation="A repeated list does not show the service works."}
::option[A maintenance ticket has a new title.]{#linux-security-updates-security-verification-b explanation="The title gives no runtime evidence."}
::option[The approved version is in use and a representative request succeeds.]{#linux-security-updates-security-verification-c .correct explanation="This verifies the software state and the service people rely on."}
:::

## Reading Two Version Signals

An installed package and the program serving requests can temporarily use different versions. For example, the package inventory can show the fixed version while a process that started before the update still runs. Use evidence about the running process to close the review.

:::single-choice{#linux-security-updates-final-application} What is still open when the installed version is fixed and the old process is still present?

::option[Whether every other process on the machine needs replacement.]{#linux-security-updates-final-application-c explanation="The question concerns the updated service and its approved maintenance requirements."}
::option[Whether the updated program is the one serving requests.]{#linux-security-updates-final-application-a .correct explanation="The package inventory verifies installed files, while the process check verifies the live service."}
::option[Whether an update package was available at all.]{#linux-security-updates-final-application-b explanation="The installed package already reports the fixed version."}
:::

## Summary

You can now review an update from candidate through verification.

1. Distinguish available updates from installed changes.
2. Account for restarts and recovery in the plan.
3. Verify the running version and expected service behavior.
