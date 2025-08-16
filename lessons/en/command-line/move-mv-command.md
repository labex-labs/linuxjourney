# mv (Move)

## Lesson Content

Used for moving files and also renaming them. Quite similar to the `cp` command in terms of flags and functionality.

You can rename files like this:

```bash
mv oldfile newfile
```

Or you can actually move a file to a different directory:

```bash
mv file2 /home/pete/Documents
```

And move more than one file:

```bash
mv file_1 file_2 /somedirectory
```

You can rename directories as well:

```bash
mv directory1 directory2
```

Like `cp`, if you `mv` a file or directory, it will overwrite anything in the same directory. So you can use the `-i` flag to prompt you before overwriting anything.

```bash
mv -i directory1 directory2
```

Let’s say you did want to `mv` a file to overwrite the previous one. You can also make a backup of that file, and it will just rename the old version with a `~`.

```bash
mv -b directory1 directory2
```

## Exercise

Rename a file, then move that file to a different directory.

## Quiz Question

How do you rename a file called `cat` to `dog`?

## Quiz Answer

`mv cat dog`
