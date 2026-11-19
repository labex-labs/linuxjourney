---
lesson_id: "host-attack-surface"
course_id: "linux-hardening"
lang: "en"
order_index: 1
title: "Attack Surface"
description: "Learn to identify what a Linux host needs to expose and which access paths deserve review."
meta_title: "Attack Surface - Linux Hardening"
meta_description: "Learn to identify what a Linux host needs to expose and which access paths deserve review."
meta_keywords: "attack surface, linux hardening, cybersecurity, Linux Journey"
---

A Linux host may have a public web page, maintenance access, and background services. Begin by writing down what each service does and who should reach it. You can then look for access that has no clear purpose.

## Listing Intended Access

A simple inventory connects a resource to the people or programs that need it. Here is a practice host.

```text
Resource           Intended access
Public homepage    Visitors
Maintenance SSH    Operations team
Preview panel      Local staff on this host only
```

An **access path** is a way a user or program reaches a resource. The set of reachable interfaces through which someone could affect a system is part of its **attack surface**.

:::single-choice{#host-attack-surface-intended-audience} Which resource in this inventory needs a public network path?

::option[Maintenance SSH.]{#host-attack-surface-intended-audience-b explanation="Its intended users are the operations team."}
::option[The public homepage.]{#host-attack-surface-intended-audience-a .correct explanation="Its intended users include visitors outside the host."}
::option[The preview panel.]{#host-attack-surface-intended-audience-c explanation="The stated use is local to the host."}
:::

## Comparing Intended and Observed Access

Suppose the preview panel is reachable over the network and the inventory still says local only. Check with the owner and verify the actual route before changing it. A service can need to run while having no need to accept remote requests.

:::single-choice{#host-attack-surface-mismatch} Which observation deserves review under the stated policy?

::option[A visitor can reach the preview panel.]{#host-attack-surface-mismatch-b .correct explanation="That gives the panel an access path outside its intended audience."}
::option[A visitor can load the homepage.]{#host-attack-surface-mismatch-a explanation="That is the homepage's intended use."}
::option[Local staff can open the preview on the host.]{#host-attack-surface-mismatch-c explanation="Local access matches the stated need."}
:::

## Prioritizing What to Check

Start with access that is both unnecessary and consequential. In a practice example, a preview panel that can change the site is a higher priority than an unused service with no important data. Record the intended audience, the observed exposure, and the test that would confirm the proposed restriction works without disrupting legitimate users.

:::single-choice{#host-attack-surface-priority-check} After changing preview access, which two observations would confirm that the restriction met the goal?

::option[The panel still accepts a local request.]{#host-attack-surface-priority-check-a explanation="This confirms essential access and leaves the unintended remote path untested."}
::option[The machine rebooted and uses the same hostname.]{#host-attack-surface-priority-check-b explanation="Host state does not show whether the policy was met."}
::option[Local staff can still reach it and the unintended remote path is closed.]{#host-attack-surface-priority-check-c .correct explanation="Together these checks validate the required access and the restriction."}
:::

## Summary

You can now identify which access paths deserve hardening review.

1. Describe a resource and its intended audience.
2. Compare intended and observed access.
3. Verify both protection and legitimate use after a change.
