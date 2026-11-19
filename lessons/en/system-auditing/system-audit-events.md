---
lesson_id: "system-audit-events"
course_id: "system-auditing"
lang: "en"
order_index: 1
title: "Audit Events"
description: "Learn to choose auditable events that answer a question about a protected file."
meta_title: "Audit Events - System Auditing"
meta_description: "Learn to choose auditable events that answer a question about a protected file."
meta_keywords: "audit events, system auditing, cybersecurity, Linux Journey"
---

A service log might report that a page was loaded. An **audit record** can describe an action your system was configured to observe, such as writing a service configuration. Begin by deciding which action matters and what information you need to review it.

## Choosing an Audit Question

Suppose the web service's configuration controls who can open a preview. You want to review changes to that file. A useful record would name the object, operation, time, account context, and result. Each field helps someone reconstruct one part of the action.

:::single-choice{#system-audit-events-choose-object} What should an audit record identify for this review?

::option[Only the number of web requests that day.]{#system-audit-events-choose-object-b explanation="Request volume describes a different activity."}
::option[The configuration file that was the target.]{#system-audit-events-choose-object-a .correct explanation="The object lets you distinguish this change from writes elsewhere."}
::option[Only the type of operation, such as write.]{#system-audit-events-choose-object-c explanation="The operation explains what was attempted. The target file identifies whether it was relevant."}
:::

## Reading the Result

A record can describe a successful write or an unsuccessful attempt. Keep both the operation and its result in view. A denied write can be useful evidence of an attempt. It gives a different conclusion from a successful write.

:::single-choice{#system-audit-events-operation-result} A record names a write to the configuration and a denied result. What does it show?

::option[The recorded write attempt was denied.]{#system-audit-events-operation-result-b .correct explanation="The operation and result together describe the observed action."}
::option[The file was definitely replaced.]{#system-audit-events-operation-result-a explanation="A denied result does not establish a successful modification."}
::option[The expected page returned HTTP 200.]{#system-audit-events-operation-result-c explanation="No page request is described here."}
:::

## Checking Coverage

The audit system only records the events its mechanisms and policies can observe. Before relying on an empty result, check that the policy covered the right path, operations, and time. Record which source you reviewed.

:::single-choice{#system-audit-events-empty-audit} You find no write record in the selected log. Which check helps before concluding no writes occurred?

::option[Count the number of installed editors.]{#system-audit-events-empty-audit-a explanation="Installed software does not establish audit coverage."}
::option[Search the same time period under a second account name only.]{#system-audit-events-empty-audit-b explanation="An additional search can help when collection is known to work. First check whether the relevant events could have been recorded at all."}
::option[Verify the policy and available time range.]{#system-audit-events-empty-audit-c .correct explanation="Missing coverage can leave no matching record even when activity occurred."}
:::

## Summary

You can now select useful audit evidence for a protected resource.

1. Identify the operation and object you need to review.
2. Read the recorded result alongside the request.
3. Check coverage before using an empty search as evidence.
