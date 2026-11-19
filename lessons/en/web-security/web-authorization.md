---
lesson_id: "web-authorization"
course_id: "web-security"
lang: "en"
order_index: 6
title: "Authorization"
description: "Learn to compare an authenticated user's request with an application's access policy."
meta_title: "Authorization - Web Security"
meta_description: "Learn to compare an authenticated user's request with an application's access policy."
meta_keywords: "authorization, web security, cybersecurity, Linux Journey"
---

A user can sign in and still lack permission for a particular action. **Authorization** is the decision about whether a specified account can take an action on a resource.

## Reading a Policy

A **role** is a named group of permissions. This practice policy governs a preview service.

```text
Role       View published page   Edit draft
Reader    Yes                   No
Editor    Yes                   Yes
```

Read the row for the user's role and the column for the requested operation. An editor can view the published page and edit a draft. A reader can view the published page.

:::single-choice{#web-authorization-read-policy} A signed-in reader asks to edit a draft. What does the table say?

::option[The action is not allowed for Reader.]{#web-authorization-read-policy-b .correct explanation="The Reader row has No under Edit draft."}
::option[The action is allowed for any signed-in account.]{#web-authorization-read-policy-a explanation="The requested action has a role-specific setting."}
::option[The user must switch to HTTPS to gain edit rights.]{#web-authorization-read-policy-c explanation="Transport protection does not assign application permissions."}
:::

## Checking the Right Resource

Many systems grant different rights for different resources. An editor could be allowed to change drafts in their own project while viewing only another project's pages. The check should identify both the operation and the target resource.

:::single-choice{#web-authorization-target-resource} Maya can edit Project A. What evidence decides whether she can edit Project B?

::option[The title of Project A.]{#web-authorization-target-resource-b explanation="The title does not describe another project's access."}
::option[The fact that her sign-in succeeded.]{#web-authorization-target-resource-c explanation="Authentication identifies Maya's account and leaves the resource decision open."}
::option[The permission policy for Maya and Project B.]{#web-authorization-target-resource-a .correct explanation="The earlier grant covered a specific resource."}
:::

## Checking at the Service

A user interface may hide editing controls from readers. The server should still enforce its policy whenever it receives a request. Test expected allowed and denied cases through normal approved actions for the practice service.

:::single-choice{#web-authorization-decision-location} An application hides the Edit button for readers. Where should its access decision also be enforced?

::option[Only in the browser when it decides which button to show.]{#web-authorization-decision-location-a explanation="The browser can guide the interface. The service makes the access decision for the request it receives."}
::option[In the service that receives the requested operation.]{#web-authorization-decision-location-c .correct explanation="The service can evaluate the account, action, and target resource each time."}
::option[Only on the page that lists the roles.]{#web-authorization-decision-location-b explanation="Showing the role name does not enforce a restricted operation."}
:::

## Summary

You can now reason about an application access decision.

1. Match the account's role to the requested action.
2. Include the specific resource in the check.
3. Verify that the service enforces its policy on requests.
