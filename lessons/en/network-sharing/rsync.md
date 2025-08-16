# rsync

## Lesson Content

Another tool used to copy data from different hosts is rsync (short for remote synchronization). Rsync is very similar to scp, but it has a major difference. Rsync uses a special algorithm that checks in advance if there is already data that you are copying to and will only copy over the differences. For example, let's say that you were copying over a file and your network got interrupted; therefore, your copy stopped midway. Instead of re-copying everything from the beginning, rsync will only copy over the parts that didn't get copied.

It also verifies the integrity of a file you are copying over with checksums. These small optimizations allow greater file transfer flexibility and make rsync ideal for directory synchronization remotely and locally, data backups, large data transfers, and more.

Some commonly-used rsync options:

- v - verbose output
- r - recursive into directories
- h - human-readable output
- z - compressed for easier transfer, great for slow connections

### Copy/sync files on the same host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copy/sync files to local host from a remote host

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copy/sync files to a remote host from a local host

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

Use rsync to sync a directory to another directory. Be sure not to overwrite an important directory!

## Quiz Question

What command would be useful for data backups?

## Quiz Answer

rsync
