# User Management Tools

## Lesson Content

Most enterprise environments use management systems to manage users, accounts, and passwords. However, on a single machine computer, there are useful commands to run to manage users.

**Adding Users**

You can use the `adduser` or the `useradd` command. The `adduser` command contains more helpful features, such as making a home directory and more. There are configuration files for adding new users that can be customized depending on what you want to allocate to a default user.

```bash
sudo useradd bob
```

You'll see that the above command creates an entry in `/etc/passwd` for bob, sets up default groups, and adds an entry to the `/etc/shadow` file.

**Removing Users**

To remove a user, you can use the `userdel` command.

```bash
sudo userdel bob
```

This basically does its best to undo the file changes made by `useradd`.

**Changing Passwords**

```bash
passwd bob
```

This will allow you to change the password of yourself or another user (if you are root).

## Exercise

Create a new user, then change their password and log in as the new user.

## Quiz Question

What command is used to change a password?

## Quiz Answer

`passwd`
