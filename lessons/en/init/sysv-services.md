# System V Service

## Lesson Content

There are many command-line tools you can use to manage Sys V services.

**List services**

```bash
service --status-all
```

**Start a service**

```bash
sudo service networking start
```

**Stop a service**

```bash
sudo service networking stop
```

**Restart a service**

```bash
sudo service networking restart
```

These commands aren't specific to Sys V init systems; you can use them to manage Upstart services as well. Since Linux is trying to move away from the more traditional Sys V init scripts, there are still things in place to help that transition.

## Exercise

Manage a couple of services and change their states. What do you observe?

## Quiz Question

What is the command to stop a service named `peanut` with Sys V?

## Quiz Answer

`sudo service peanut stop`
