---
lesson_id: "web-authentication"
course_id: "web-security"
lang: "zh"
order_index: 4
title: "身份验证"
description: "了解 Web 服务如何核实身份，以及两种验证因素为什么能提供不同的证据。"
meta_title: "身份验证 - Web 安全"
meta_description: "区分用户声称的身份与证明，了解密码和安全密钥如何提供不同的验证因素。"
meta_keywords: "身份验证, 验证因素, 密码, 安全密钥, Web 安全, Linux Journey"
---

**身份验证**是核实用户所声称身份的步骤。登录表单可能要求输入账户名和密码。账户名告诉服务用户声称自己是谁，密码则是服务可以核查的证明。

## 识别用户声称的身份

假设用户输入账户名 `alex`。任何知道这个名称的人都能输入它。服务会根据该账户的信息和策略，检查用户提交的证明。

:::single-choice{#web-authentication-username-claim} 哪项输入表明用户想访问哪个账户？

::option[密码检查的结果。]{#web-authentication-username-claim-a explanation="这是决定接受还是拒绝所声称身份的证据。"}
::option[账户名。]{#web-authentication-username-claim-b .correct explanation="它告诉服务需要核实哪个身份。"}
::option[主页的响应格式。]{#web-authentication-username-claim-c explanation="内容类型与登录身份无关。"}
:::

## 比较身份验证因素

**因素**指一类身份证明。密码属于用户知道的信息。已注册的安全密钥则能证明用户持有某个物件。使用密码和单独注册的密钥，可以提供两种不同的证据。

:::single-choice{#web-authentication-independent-factors} 哪组示例同时用了用户知道的信息和持有的物件？

::option[密码和已经注册的安全密钥。]{#web-authentication-independent-factors-a .correct explanation="一个核查用户知道的内容，另一个核查用户能否使用密钥。"}
::option[密码和另外一个背下来的密码。]{#web-authentication-independent-factors-b explanation="两者都属于用户知道的信息。"}
::option[用户名和网页标题。]{#web-authentication-independent-factors-c explanation="这些名称几乎无法为身份提供证明。"}
:::

## 理解验证成功意味着什么

核对证明后，服务可能会允许用户打开会话。身份验证成功说明服务认定哪个账户已经登录。要知道这个账户可以做什么，还得查看具体权限。访问某项资源时，服务会应用相应的访问规则。

:::single-choice{#web-authentication-auth-limit} 某个账户已经成功登录，又请求访问管理员页面。下一步应该怎样做？

::option[自动向所有已登录账户返回该页面。]{#web-authentication-auth-limit-a explanation="这个账户仍需要具备该页面要求的权限。"}
::option[用原来那个网页的标题来决定权限。]{#web-authentication-auth-limit-b explanation="网页标题并不包含用户的权限。"}
::option[应用应该检查该账户能否访问这个资源。]{#web-authentication-auth-limit-c .correct explanation="身份验证和资源访问权限解决的是两个问题。"}
:::

## 总结

现在，你可以说明一次身份验证能确认什么。

1. 区分用户声称的身份与用于核实它的证明。
2. 识别两种不同类型的身份验证因素。
3. 用服务的授权策略来判断能否访问具体资源。
