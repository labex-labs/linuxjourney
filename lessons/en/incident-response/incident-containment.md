---
lesson_id: "incident-containment"
course_id: "incident-response"
lang: "en"
order_index: 4
title: "Containment"
description: "Learn to compare approved containment options by purpose, impact, and evidence needs."
meta_title: "Containment - Incident Response"
meta_description: "Learn to compare approved containment options by purpose, impact, and evidence needs."
meta_keywords: "containment, incident response, cybersecurity, Linux Journey"
---

**Containment** is a short-term action intended to limit ongoing harm while the team investigates. The suitable action depends on what is affected and what access people still need.

## Defining the Boundary

Imagine an internal preview panel is reachable through a public route, while the homepage should stay open. One option is to restrict the preview route. A wider option is to take the whole site offline. Compare the behavior each choice would change.

:::single-choice{#incident-containment-narrow-action} Which option best fits a goal of removing public preview access while keeping the homepage available?

::option[Disable every public route regardless of purpose.]{#incident-containment-narrow-action-b explanation="That would also remove the homepage."}
::option[Restrict the affected preview route and verify both paths.]{#incident-containment-narrow-action-a .correct explanation="This targets the reported exposure and checks that required service remains."}
::option[Change the label of the preview service.]{#incident-containment-narrow-action-c explanation="A label does not stop requests from reaching it."}
:::

## Planning for Evidence and Access

Consult the response plan and the people authorized to make the change. Record who approved it, its intended duration, and which evidence should be preserved first when circumstances permit. Consider whether the action would interrupt service logs or the responders' access.

:::single-choice{#incident-containment-action-impact} A proposed isolation change might also block investigators from retrieving records. What should the team review?

::option[What to preserve and how approved responders will retain access.]{#incident-containment-action-impact-b .correct explanation="This accounts for both the containment goal and the investigation."}
::option[Only whether the configuration file has a short name.]{#incident-containment-action-impact-a explanation="Naming does not preserve records or access."}
::option[Whether to publish credentials so everyone can reconnect.]{#incident-containment-action-impact-c explanation="Credentials should remain protected and access should stay controlled."}
:::

## Verifying a Containment Change

Check whether the unintended path closed. Test an expected path separately to understand side effects. Record when you made the change and when the team should reassess it. Containment can succeed while the underlying cause remains open.

:::single-choice{#incident-containment-containment-success} The public preview route is closed and the homepage still works. Which statement is supported?

::option[The root cause has definitely been repaired.]{#incident-containment-containment-success-a explanation="The checks confirm the access boundary and do not establish repair."}
::option[Every potential path to the preview has been tested.]{#incident-containment-containment-success-b explanation="These checks cover the specific paths used."}
::option[The tested public preview path is blocked and the required homepage remains available.]{#incident-containment-containment-success-c .correct explanation="This reports the outcome within the verified scope."}
:::

## Summary

You can now evaluate a short-term containment action.

1. Name the path or access the action should restrict.
2. Check authorization, evidence, and expected effects.
3. Verify the intended restriction and essential service separately.
