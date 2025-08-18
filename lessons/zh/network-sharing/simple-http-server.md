---
lang: "zh"
title: "简单的 HTTP 服务器"
meta_title: "简单的 HTTP 服务器 - 网络共享"
meta_description: "学习使用 Python 的 http.server 模块创建一个简单的 HTTP 服务器。通过这个适合初学者的 Linux 教程，快速在你的网络上共享文件。"
meta_keywords: "http.server, SimpleHTTPServer, Python web server, 文件共享，Linux 教程，初学者指南"
---

## Lesson Content

Python 有一个非常有用的工具，可以通过 HTTP 提供文件服务。如果你只是想创建一个快速的网络共享，让网络上的其他机器可以访问，这会非常棒。要做到这一点，只需进入你想要共享的目录并运行：

```bash
python -m http.server
```

或者，如果你仍然在使用 Python 2：

```bash
python -m SimpleHTTPServer
```

这会设置一个基本的 Web 服务器，你可以通过 localhost 地址访问它。所以，获取你运行此命令的机器的 IP 地址，然后在另一台机器上，在浏览器中通过 `http://IP_ADDRESS:8000` 访问它。在你自己的机器上，你可以通过在 Web 浏览器中输入 `http://localhost:8000` 来查看可用的文件。

## Exercise

尝试设置一个 `http.server`！

## Quiz Question

你可以使用什么工具来使用 Python 创建一个简单的 HTTP 服务器？

## Quiz Answer

http.server
