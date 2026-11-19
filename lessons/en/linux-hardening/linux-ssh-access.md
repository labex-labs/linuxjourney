---
lesson_id: "linux-ssh-access"
course_id: "linux-hardening"
lang: "en"
order_index: 6
title: "SSH Access"
description: "Learn to distinguish SSH server identity, user authentication, and login access policy."
meta_title: "SSH Access - Linux Hardening"
meta_description: "Learn to distinguish SSH server identity, user authentication, and login access policy."
meta_keywords: "ssh access, linux hardening, cybersecurity, Linux Journey"
---

When you use SSH for maintenance, both ends of the connection have a question to answer. Your client needs to know which server it reached. The server needs to know whether the account is allowed to sign in.

## Checking the Server Identity

An SSH server presents a **host key**. The client can compare it with the known identity for that host. If a key unexpectedly changes, verify the new key through an approved independent source, such as the team's host inventory or a maintainer using a trusted channel.

:::single-choice{#linux-ssh-access-unexpected-key} Your client says the server's host key changed. What is the first useful check?

::option[Confirm the expected new host key through a trusted source.]{#linux-ssh-access-unexpected-key-b .correct explanation="That verifies the identity before you rely on the connection."}
::option[Try several usernames until one works.]{#linux-ssh-access-unexpected-key-a explanation="A username does not verify the server's identity."}
::option[Delete every saved host key and proceed.]{#linux-ssh-access-unexpected-key-c explanation="This would discard known identity information before explaining the change."}
:::

## Checking the User's Access

A user key can provide proof that a client is authorized to act as an account. The host key answers the separate question of server identity. A server's policy can limit which accounts and authentication methods it accepts. This practice summary says `ops` signs in using key-based authentication.

:::single-choice{#linux-ssh-access-distinguish-keys} Which identity is checked when the server evaluates ops's user key?

::option[The name of the public web page.]{#linux-ssh-access-distinguish-keys-b explanation="The web content is separate from SSH authentication."}
::option[The server proving its own identity.]{#linux-ssh-access-distinguish-keys-c explanation="The client uses the host key for that check."}
::option[The client attempting to sign in as ops.]{#linux-ssh-access-distinguish-keys-a .correct explanation="User authentication concerns the account the client is trying to use."}
:::

## Preserving a Maintenance Path

Before approved changes to an SSH policy, agree on the expected accounts and access method. Use a separate test connection and keep the established recovery path available until the intended login succeeds. An existing open session might survive a change while a new login fails.

:::single-choice{#linux-ssh-access-test-new-login} An existing session remains open after a policy change. What confirms a maintainer can still get in?

::option[A ping response alone.]{#linux-ssh-access-test-new-login-a explanation="A network response does not show SSH authentication succeeded."}
::option[A new approved SSH session using the intended account and method.]{#linux-ssh-access-test-new-login-c .correct explanation="This directly checks the policy a future login will face."}
::option[The old session remaining idle.]{#linux-ssh-access-test-new-login-b explanation="It was authenticated under earlier conditions."}
:::

## Summary

You can now check the main identities and choices in SSH maintenance access.

1. Verify the server identity using its host key.
2. Distinguish that check from user authentication.
3. Verify a new approved connection after a change.
