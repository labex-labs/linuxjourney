---
lesson_id: "security-session-records"
course_id: "security-logs"
lang: "en"
order_index: 4
title: "Session Records"
description: "Learn how to pair opened and closed session records and check which sessions a log excerpt can describe."
meta_title: "Session Records - Security Logs"
meta_description: "Read Linux session records, pair opening and closing events, and decide how to check a missing closure."
meta_keywords: "Linux session records, session opened, session closed, login session ID, log retention"
---

A sign-in check confirms that someone passed the check for an account. A **session** is the period of activity that follows a sign-in and ends when the user signs out or disconnects. Session records tell you when that period started and when it ended, if both events were logged.

## Reading an Opening Record

A session system can assign a **session ID** to identify a session on a machine. These simulated lines show two openings for the same account on `web-01`. All times in this lesson are in the same time zone.

```text
t=09:14:05Z source=session host=web-01 account=alex session=42 state=opened
t=09:17:00Z source=session host=web-01 account=alex session=43 state=opened
```

The first line reports that session 42 began. The second reports a separate session, 43, on the same host.

:::single-choice{#security-session-records-two-openings} Which statement do the two openings support?

::option[The first session ended when the second began.]{#security-session-records-open-ended explanation="The second opening starts another session. It gives no closing time for the first."}
::option[Two different accounts signed in to the host.]{#security-session-records-open-accounts explanation="Both lines name the same account. The session field distinguishes the two periods of activity."}
::option[The same account opened two separate sessions.]{#security-session-records-open-two .correct explanation="Both lines name alex and each has its own session ID on web-01."}
:::

## Pairing an Opening and a Closing

Read the host and session ID together before pairing two records. Compare the closing line below with the opening records.

```text
t=09:20:05Z source=session host=web-01 account=alex session=42 state=closed
```

On `web-01`, the opening and closing records for session 42 are six minutes apart. The pair gives a recorded start and end. It provides no list of actions taken between them.

![LabEx Terminal displaying simulated openings for sessions 42 and 43 and the closing record for session 42](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-session-records/session-records.png)

The simulated opening and closing records appear together in this terminal view.

:::single-choice{#security-session-records-pair-ids} Suppose the closing line showed `session=43` instead, with the host and time unchanged. When would that session have started?

::option[At 09:14:05.]{#security-session-records-pair-forty-two explanation="That opening names the same account but belongs to session 42."}
::option[At 09:17:00.]{#security-session-records-pair-forty-three .correct explanation="Match web-01 and session 43 to the second opening. It started at 09:17:00."}
::option[At 09:20:05.]{#security-session-records-pair-end-time explanation="That is the recorded closing time. Use the matching opening for the start."}
:::

## Checking a Missing Closing Record

Return to the original closing record for session 42. The excerpt ends at 09:21 and still has no matching close for session 43. The session could still have been active when the excerpt ended. A closing record may also be outside the available time window or missing from this source. A log's **retention period** is how long the record is kept and available for review.

:::single-choice{#security-session-records-missing-close} What can you say about session 43 from the excerpt alone?

::option[It was still active at the end of the excerpt.]{#security-session-records-missing-active explanation="That is possible, but the missing close does not establish the current state."}
::option[The excerpt contains no recorded closing time for it.]{#security-session-records-missing-unknown .correct explanation="This describes the available records. A later or different source may provide the closing time."}
::option[It closed together with session 42.]{#security-session-records-missing-together explanation="The recorded close belongs to 42. There is no matching close for 43 here."}
:::

## Choosing a Source for the Question

For a historical closing time, look for a matching close in a later excerpt from the same host. If the question is whether the session is active now, check a current session list from that host. A saved log and a current list answer questions about different times.

:::single-choice{#security-session-records-current-status} You need to know whether session 43 is active now. Which source is most useful?

::option[A current session list from web-01.]{#security-session-records-current-list .correct explanation="A current list shows the sessions the host reports as active now."}
::option[An older copy of the opening record.]{#security-session-records-current-opening explanation="It shows the session started. It cannot tell whether it is still active."}
::option[A closing record for session 42 on web-01.]{#security-session-records-current-other explanation="A close for a different session cannot answer the question about session 43."}
:::

## Summary

You can now use session records to describe a recorded start and end.

1. Identify an opening and its host and session ID.
2. Match a closing record to the correct opening.
3. State what a missing closing record leaves unknown.
4. Choose between historical records and a current session list.
