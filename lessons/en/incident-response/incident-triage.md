---
lesson_id: "incident-triage"
course_id: "incident-response"
lang: "en"
order_index: 1
title: "Incident Triage"
description: "Learn to turn an initial incident report into a scoped first investigation."
meta_title: "Incident Triage - Incident Response"
meta_description: "Learn to turn an initial incident report into a scoped first investigation."
meta_keywords: "incident triage, incident response, cybersecurity, Linux Journey"
---

An initial report may say a page failed or that an alert fired. **Triage** means deciding what needs attention first. Write down the affected service, time, and observed behavior before choosing a response.

## Reading the Report

A teammate writes this simulated report.

```text
09:22 UTC: Visitors received 503 from the public homepage.
The staff preview still loaded during the same check.
First failure observed at approximately 09:19 UTC.
```

The report gives two routes and two different observations. Confirm the public homepage result and record the time and address you checked.

:::single-choice{#incident-triage-affected-service} Which symptom should the first check focus on?

::option[The staff preview returning 503.]{#incident-triage-affected-service-b explanation="The report says that preview still loaded."}
::option[The public homepage returning 503.]{#incident-triage-affected-service-a .correct explanation="That is the affected path named in the report."}
::option[A missing page on an unrelated host.]{#incident-triage-affected-service-c explanation="That path is outside this report."}
:::

## Estimating the Impact

Check how many users or requests are affected and whether the service remains usable. Determine whether the event is still happening. State uncertain estimates as estimates until you have better evidence. Use the response plan to decide whom to notify.

:::single-choice{#incident-triage-triage-scope} Which observation helps decide whether the issue is still urgent?

::option[A current check of the failing path and recent request outcomes.]{#incident-triage-triage-scope-b .correct explanation="This shows whether the symptom persists and how widely it appears."}
::option[The age of the repository's first commit.]{#incident-triage-triage-scope-a explanation="That does not show the current effect."}
::option[The original report's severity label by itself.]{#incident-triage-triage-scope-c explanation="The original label is context. Current impact helps decide whether the issue remains urgent."}
:::

## Choosing a Useful First Action

If the current request also fails, keep the result and look at recent service changes and logs during the affected time. A parallel healthy path helps narrow the issue. Avoid treating the first plausible explanation as confirmed cause.

:::single-choice{#incident-triage-first-next-step} The public path still fails and staff preview still works. What should you look at next?

::option[All unrelated projects in the company.]{#incident-triage-first-next-step-a explanation="The report points to a narrower service and time."}
::option[A random old error from another date.]{#incident-triage-first-next-step-b explanation="Start with evidence near the observed failure."}
::option[Public route records during the reported window.]{#incident-triage-first-next-step-c .correct explanation="These can help distinguish a routing issue from a service failure."}
:::

## Summary

You can now create a focused first response to an incident report.

1. Name the affected path, time, and symptom.
2. Check current user impact.
3. Choose the next evidence source for the affected path.
