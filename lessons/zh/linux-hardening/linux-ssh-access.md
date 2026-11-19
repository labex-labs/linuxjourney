---
lesson_id: "linux-ssh-access"
course_id: "linux-hardening"
lang: "zh"
order_index: 6
title: "SSH 访问"
description: "区分 SSH 服务器身份、用户身份验证和登录访问策略。"
meta_title: "SSH 访问 - Linux 安全加固"
meta_description: "核对 SSH 主机密钥，理解用户身份验证，并在调整策略后验证新的维护连接。"
meta_keywords: "SSH 访问, 主机密钥, 身份验证, 登录策略, Linux 安全加固, Linux Journey"
---

使用 SSH 进行维护时，连接两端各有一个问题需要确认。客户端要确定自己连到了哪台服务器。服务器则要判断这个账户是否可以登录。

## 核对服务器身份

SSH 服务器会出示**主机密钥**。客户端可以把它与已知的主机身份比较。如果密钥突然发生变化，应通过获准的独立渠道验证新密钥，例如团队的主机清单，或通过可信渠道联系维护人员。

:::single-choice{#linux-ssh-access-unexpected-key} 客户端提示服务器的主机密钥发生了变化。应该先做哪项检查？

::option[通过可信渠道确认预期的新主机密钥。]{#linux-ssh-access-unexpected-key-b .correct explanation="先核实身份，再信任这条连接。"}
::option[尝试多个用户名，直到有一个能用。]{#linux-ssh-access-unexpected-key-a explanation="用户名无法验证服务器的身份。"}
::option[删除所有保存的主机密钥，然后继续连接。]{#linux-ssh-access-unexpected-key-c explanation="这样会在弄清变化原因之前丢掉已知的身份信息。"}
:::

## 检查用户是否有权登录

用户密钥可以证明客户端有权以某个账户的身份操作。主机密钥回答的是另一个问题，即服务器是谁。服务器策略可以限定允许登录的账户和身份验证方式。练习摘要显示，`ops` 使用基于密钥的方式登录。

:::single-choice{#linux-ssh-access-distinguish-keys} 服务器检查 ops 的用户密钥时，验证的是哪个身份？

::option[公开网页的名称。]{#linux-ssh-access-distinguish-keys-b explanation="网页内容与 SSH 身份验证是两回事。"}
::option[服务器出示自身身份。]{#linux-ssh-access-distinguish-keys-c explanation="客户端会用主机密钥做那项检查。"}
::option[尝试以 ops 身份登录的客户端。]{#linux-ssh-access-distinguish-keys-a .correct explanation="用户身份验证关注客户端尝试使用的账户。"}
:::

## 保留维护通道

对 SSH 策略进行获准的变更之前，先确认预期使用的账户和访问方式。另建测试连接，在预期的登录验证成功之前保留已有的恢复通道。旧会话可能在变更后继续存在，即使新登录已经失败。

:::single-choice{#linux-ssh-access-test-new-login} 策略更改后，已有会话仍然开着。怎样确认维护人员依然能够登录？

::option[只看 ping 有没有响应。]{#linux-ssh-access-test-new-login-a explanation="有网络响应并不能证明 SSH 身份验证通过了。"}
::option[使用预期账户和方式建立一次经授权的新 SSH 会话。]{#linux-ssh-access-test-new-login-c .correct explanation="这直接检验未来的登录会遇到的策略。"}
::option[让旧会话保持空闲。]{#linux-ssh-access-test-new-login-b explanation="该会话是在旧条件下通过身份验证的。"}
:::

## 总结

现在，你可以检查 SSH 维护访问中的不同身份及相关设置。

1. 用主机密钥验证服务器身份。
2. 区分服务器身份核对与用户身份验证。
3. 变更后验证一条获准的新连接。
