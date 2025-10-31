---
index: 2
lang: "en"
title: "rsync"
meta_title: "rsync - Network Sharing"
meta_description: "Discover how to use the powerful rsync command in Linux for efficient file synchronization, remote data transfer, and reliable backups. This guide covers key rsync commands and options."
meta_keywords: "rsync, linux rsync, file synchronization, data backup, remote sync, rsync command, linux file transfer, rsync tutorial"
---

## Lesson Content

### What is rsync?

Another essential tool for copying data between different hosts is `rsync`, which stands for remote synchronization. While similar to `scp`, `rsync` has a key difference that makes it incredibly efficient. It uses a delta-transfer algorithm that intelligently checks the destination for existing data and only transfers the parts of files that have changed.

For instance, if a large file transfer is interrupted, `rsync` can resume the copy, transferring only the remaining parts of the file instead of starting over from scratch. This makes it a robust choice for unstable network connections.

### Key Features of rsync

The efficiency of `rsync` comes from its smart optimizations. It verifies file integrity using checksums to ensure the copied data is not corrupted during transfer. These features provide significant flexibility, making `rsync` an ideal tool for:

- Directory synchronization (both remote and local)
- Creating incremental data backups
- Handling large data transfers efficiently

### Common rsync Options

You can modify the behavior of the `rsync` command with several options. Some of the most commonly used ones include:

- `-v`: Verbose output, showing which files are being transferred.
- `-r`: Recursive, which is necessary for copying entire directories.
- `-h`: Human-readable output, displaying numbers in a more understandable format (e.g., KB, MB).
- `-z`: Compresses file data during the transfer, which is great for slow connections.
- `-a`: Archive mode, a convenient shortcut that combines several options (`-rlptgoD`) to preserve permissions, ownership, and timestamps.

### rsync Usage Examples

#### Sync Files on the Same Host

You can use `rsync` to synchronize two directories on your local machine. This is useful for creating local backups.

```bash
rsync -avh /my/local/directory/one/ /my/local/directory/two/
```

#### Sync Files from a Remote Host to a Local Host

To pull files from a remote server to your local machine, specify the remote source first.

```bash
rsync -avh username@remotehost.com:/remote/directory/ /local/directory/
```

#### Sync Files from a Local Host to a Remote Host

To push files from your local machine to a remote server, specify the local source first.

```bash
rsync -avh /local/directory/ username@remotehost.com:/remote/directory/
```

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What command, known for its delta-transfer algorithm, is particularly useful for creating efficient data backups? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

rsync
