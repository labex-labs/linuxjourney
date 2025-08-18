---
lang: "en"
title: "/etc/shadow"
meta_description: "Learn about the /etc/shadow file in Linux, its fields, and how it secures user passwords. Understand Linux authentication for beginners."
meta_keywords: "/etc/shadow, Linux security, user authentication, password management, Linux tutorial, beginner guide"
---

## Lesson Content

The `/etc/shadow` file is used to store information about user authentication. It requires superuser read permissions.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

You'll notice that it looks very similar to the contents of `/etc/passwd`; however, in the password field, you'll see an encrypted password. The fields are separated by colons as follows:

1. Username
2. Encrypted password
3. Date of last password changed - expressed as the number of days since Jan 1, 1970. If there is a 0, that means the user should change their password the next time they log in.
4. Minimum password age - Days that a user will have to wait before being able to change their password again.
5. Maximum password age - Maximum number of days before a user has to change their password.
6. Password warning period - Number of days before a password is going to expire.
7. Password inactivity period - Number of days after a password has expired to allow login with their password.
8. Account expiration date - Date that a user will not be able to log in.
9. Reserved field for future use.

In most distributions today, user authentication doesn't rely on just the `/etc/shadow` file; there are other mechanisms in place, such as PAM (Pluggable Authentication Modules), that replace authentication.

## Exercise

Take a look at the `/etc/shadow` file.

## Quiz Question

No questions, move along!

## Quiz Answer
