# Systemd Goals

## Lesson Content

We won't get into the details of writing systemd unit files. We will, however, go over a brief overview of a unit file and how to manually control units.

Here is a basic service unit file: foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

This is a simple service target. At the beginning of the file, we see a section for `[Unit]`. This allows us to give our unit file a description as well as control the ordering of when to activate the unit. The next portion is the `[Service]` section; under here, we can start, stop, or reload a service. And the `[Install]` section is used for dependencies. This is only the tip of the iceberg for writing systemd files, so I implore you to read up on the subject if you want to know more.

Now, let's get into some commands you can use with systemd units:

**List units**

```bash
systemctl list-units
```

**View status of unit**

```bash
systemctl status networking.service
```

**Start a service**

```bash
sudo systemctl start networking.service
```

**Stop a service**

```bash
sudo systemctl stop networking.service
```

**Restart a service**

```bash
sudo systemctl restart networking.service
```

**Enable a unit**

```bash
sudo systemctl enable networking.service
```

**Disable a unit**

```bash
sudo systemctl disable networking.service
```

Again, you have yet to see how much depth systemd gets into, so read up on it if you want to learn more.

## Exercise

View the unit statuses and start and stop a few services. What do you observe?

## Quiz Question

What is the command to start a service named peanut.service?

## Quiz Answer

`sudo systemctl start peanut.service`
