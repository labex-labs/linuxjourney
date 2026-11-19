---
lesson_id: "web-authentication"
course_id: "web-security"
lang: "en"
order_index: 4
title: "Authentication"
description: "Learn how a web service verifies identity and why two factors can give different evidence."
meta_title: "Authentication - Web Security"
meta_description: "Learn how a web service verifies identity and why two factors can give different evidence."
meta_keywords: "authentication, web security, cybersecurity, Linux Journey"
---

**Authentication** is the step that verifies the identity claimed by a user. A sign-in form may ask for an account name and a password. The name states the claim. The password provides evidence the service can check.

## Identifying the Claim

Imagine a user enters the account name `alex`. Anyone who knows the name can enter it. The service checks the submitted proof against the information and policy for that account.

:::single-choice{#web-authentication-username-claim} Which input states the account the user is trying to access?

::option[The result of the password check.]{#web-authentication-username-claim-a explanation="That is evidence used to accept or reject the claim."}
::option[The account name.]{#web-authentication-username-claim-b .correct explanation="It tells the service which identity to verify."}
::option[The homepage's response format.]{#web-authentication-username-claim-c explanation="Content type is unrelated to the sign-in identity."}
:::

## Comparing Authentication Factors

A **factor** is a category of proof. A password is something the user knows. A registered security key provides proof based on something the user possesses. Using a password and a separate registered key gives two kinds of evidence.

:::single-choice{#web-authentication-independent-factors} Which example combines knowledge and possession?

::option[A password and a registered security key.]{#web-authentication-independent-factors-a .correct explanation="One checks knowledge and the other checks access to the key."}
::option[A password and a second memorized password.]{#web-authentication-independent-factors-b explanation="Both are examples of something the user knows."}
::option[A username and a page title.]{#web-authentication-independent-factors-c explanation="These labels provide little evidence of identity."}
:::

## Understanding What Success Means

After verifying the proof, the service may let the user start a session. A successful identity check establishes which account the service treats as signed in. It does not by itself describe everything the account can do. The service will use its access rules for requests to particular resources.

:::single-choice{#web-authentication-auth-limit} An account has signed in successfully and asks for an administrator page. What should happen next?

::option[Every signed-in account should receive the page automatically.]{#web-authentication-auth-limit-a explanation="The account still needs the permission required by that page."}
::option[The original page title should determine access.]{#web-authentication-auth-limit-b explanation="Titles do not carry a user's rights."}
::option[The application should check the account's access to that resource.]{#web-authentication-auth-limit-c .correct explanation="Identity verification and resource access answer separate questions."}
:::

## Summary

You can now describe what an authentication decision establishes.

1. Separate the claimed identity from its proof.
2. Recognize two different kinds of authentication factors.
3. Leave resource-level decisions to the service's authorization policy.
