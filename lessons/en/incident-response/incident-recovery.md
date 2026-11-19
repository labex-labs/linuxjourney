---
lesson_id: "incident-recovery"
course_id: "incident-response"
lang: "en"
order_index: 5
title: "Recovery"
description: "Learn to verify an approved service state before declaring recovery complete."
meta_title: "Recovery - Incident Response"
meta_description: "Learn to verify an approved service state before declaring recovery complete."
meta_keywords: "recovery, incident response, cybersecurity, Linux Journey"
---

**Recovery** restores the expected service and checks that it remains usable. A newly started process is an early signal. The team also needs evidence that configuration, dependencies, and user-facing behavior match the intended state.

## Identifying the Restored State

Record the approved candidate version and configuration. If a service was isolated, check which access should remain restricted. Reopening a path can change the containment boundary.

:::single-choice{#incident-recovery-restore-target} Which result tells you whether you restored the intended version?

::option[A fresh timestamp on any unrelated VM.]{#incident-recovery-restore-target-b explanation="That does not identify the restored service."}
::option[A list of available packages alone.]{#incident-recovery-restore-target-c explanation="Available packages do not establish what is currently serving requests."}
::option[A response or deployment record identifying the approved version at the target.]{#incident-recovery-restore-target-a .correct explanation="It ties the running service to the version the team chose."}
:::

## Rechecking the Reported Problem

In the simulated incident, visitors saw `503` on the public homepage. After restoration, request that same path from an appropriate test location. Check for the expected success result and watch recent request errors. A successful internal preview does not test the public path.

:::single-choice{#incident-recovery-verify-original-path} Which test best shows that the original user-visible symptom is gone?

::option[Check only that the service binary exists.]{#incident-recovery-verify-original-path-a explanation="The file may exist without handling public requests."}
::option[Check the public homepage from the relevant client path.]{#incident-recovery-verify-original-path-b .correct explanation="This repeats the observation that initially failed."}
::option[Check only the internal preview.]{#incident-recovery-verify-original-path-c explanation="This path was different from the affected route."}
:::

## Continuing to Observe

Agree on a short observation period and success criteria. Review relevant signals such as errors, latency, or access denials. Record any limits, remaining actions, and the next review time. Keep the recovery evidence with the incident record.

:::single-choice{#incident-recovery-observation-period} An initial check passes but the failure was intermittent. What should happen before closing the recovery check?

::option[Continue checking the agreed signals during the observation window.]{#incident-recovery-observation-period-c .correct explanation="This gives evidence that the restored behavior is holding."}
::option[Close it immediately because one response arrived.]{#incident-recovery-observation-period-a explanation="A single observation may miss an intermittent problem."}
::option[Discard all comparison data.]{#incident-recovery-observation-period-b explanation="The earlier results establish what improved."}
:::

## Summary

You can now check the service state and user-visible behavior after recovery.

1. Identify the approved version and configuration.
2. Retest the user-facing symptom.
3. Observe the agreed signals before closing the recovery check.
