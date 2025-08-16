# /proc filesystem

## Lesson Content

Remember, everything in Linux is a file, even processes. Process information is stored in a special filesystem known as the `/proc` filesystem.

```bash
ls /proc
```

You should see multiple values here; there are subdirectories for every PID. If you looked at a PID in the `ps` output, you would be able to find it in the `/proc` directory.

Go ahead and enter one of the processes and look at that file:

```bash
cat /proc/12345/status
```

You should see process state information as well as more detailed information. The `/proc` directory is how the kernel views the system, so there is a lot more information here than what you would see in `ps`.

## Exercise

No exercises for this lesson.

## Quiz Question

What filesystem stores process information?

## Quiz Answer

/proc
