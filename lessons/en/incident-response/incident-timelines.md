---
lesson_id: "incident-timelines"
course_id: "incident-response"
lang: "en"
order_index: 3
title: "Incident Timelines"
description: "Learn to place evidence on one timeline while marking uncertain event times."
meta_title: "Incident Timelines - Incident Response"
meta_description: "Learn to place evidence on one timeline while marking uncertain event times."
meta_keywords: "incident timelines, incident response, cybersecurity, Linux Journey"
---

An incident timeline orders observations from different sources. Use a common time zone and keep the original timestamp visible in your records. A sequence gives you a way to ask what may be related.

## Converting One Timestamp

Here a web report uses UTC and a deployment record uses an offset of two hours ahead of UTC.

```text
Deployment record:  2026-11-19 11:17:00 +02:00
Web report:         2026-11-19 09:22:00 UTC
```

On a Linux system with GNU date, `-d` reads a supplied timestamp and `-u` requests UTC output. The argument beginning with `+` sets the display format.

```bash
$ date -u -d '2026-11-19 11:17:00+02:00' '+%Y-%m-%d %H:%M:%S UTC'
```

The result is `2026-11-19 09:17:00 UTC`. In this example it precedes the web report by five minutes.

:::single-choice{#incident-timelines-earlier-event} Which entry occurred earlier in the normalized timeline?

::option[The deployment record.]{#incident-timelines-earlier-event-a .correct explanation="Converting its offset gives 09:17 UTC, earlier than the report at 09:22."}
::option[The web report.]{#incident-timelines-earlier-event-b explanation="Its smaller visible hour reflects its time zone before comparison."}
::option[They occurred at exactly the same time.]{#incident-timelines-earlier-event-c explanation="The two normalized times differ by five minutes."}
:::

![Recorded GNU date conversion of 11:17 at offset +02:00 to 09:17 UTC](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-timelines/normalize-utc.png)

## Distinguishing Observations from Estimates

A report can state that the first failure occurred around 09:19. Keep that as an estimate. A user's report time is separate from the actual first failed request. Mark each row with its source and time precision.

:::single-choice{#incident-timelines-estimated-time} A teammate says around 09:19. How should that appear?

::option[As exactly 09:19:00 confirmed by a log.]{#incident-timelines-estimated-time-a explanation="The source provides an estimate."}
::option[As an event with no source.]{#incident-timelines-estimated-time-c explanation="The source is needed to decide how much confidence to place in the time."}
::option[As an approximate time attributed to that report.]{#incident-timelines-estimated-time-b .correct explanation="This preserves both what the source said and its precision."}
:::

## Ordering Without Assigning Cause

A deployment can precede a service problem without being its cause. Check whether the affected route changed and whether other signals support the connection. Keep open questions visible beside the timeline.

:::single-choice{#incident-timelines-timeline-cause} What does the ordered sequence establish by itself?

::option[The deployment caused the public failure.]{#incident-timelines-timeline-cause-a explanation="Order suggests a possibility but does not establish cause."}
::option[The recorded deployment precedes the web report.]{#incident-timelines-timeline-cause-c .correct explanation="This is the time relationship demonstrated by the records."}
::option[No other events can be relevant.]{#incident-timelines-timeline-cause-b explanation="The timeline contains selected observations."}
:::

## Summary

You can now build a timeline that keeps evidence and uncertainty visible.

1. Convert recorded time zones consistently.
2. Attribute each time and mark estimates.
3. Use the sequence to choose follow-up checks.
