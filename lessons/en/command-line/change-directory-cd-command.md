# cd (Change Directory)

## Lesson Content

Now that you know where you are, let’s see if we can move around the filesystem a bit. Remember, we’ll need to navigate our way using paths. There are two different ways to specify a path: with absolute and relative paths.

- Absolute path: This is the path from the root directory. The root is the head honcho. The root directory is commonly shown as a slash (`/`). Every time your path starts with `/`, it means you are starting from the root directory. For example, `/home/pete/Desktop`.

- Relative path: This is the path from where you are currently in the filesystem. If I was in location `/home/pete/Documents` and wanted to get to a directory inside `Documents` called `taxes`, I don’t have to specify the whole path from root like `/home/pete/Documents/taxes`; I can just go to `taxes/` instead.

Now that you know how paths work, we just need something to help us change to the directory we want to. Luckily, we have `cd` or “change directory” to do that.

```bash
cd /home/pete/Pictures
```

So now I've changed my directory location to `/home/pete/Pictures`.

Now from this directory, I have a folder inside called `Hawaii`. I can navigate to that folder with:

```bash
cd Hawaii
```

Notice how I just used the name of the folder? It’s because I was already in `/home/pete/Pictures`.

It can get pretty tiring navigating with absolute and relative paths all the time. Luckily, there are some shortcuts to help you out.

- `.` (current directory): This is the directory you are currently in.
- `..` (previous directory): Takes you to the directory above your current one.
- `~` (home directory): This directory defaults to your “home directory,” such as `/home/pete`.
- `-` (previous directory): This will take you to the previous directory you were just at.

```bash
cd .
cd ..
cd ~
cd -
```

Give them a try!

## Exercise

1. Run the `cd` command without any flags. Where does it take you?

## Quiz Question

If you are in `/home/pete/Pictures` and wanted to go to `/home/pete`, what’s a good shortcut to use?

## Quiz Answer

cd ..
