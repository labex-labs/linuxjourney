---
lesson_id: "etc-shadow-file"
course_id: "user-management"
lang: "zh"
order_index: 4
title: "/etc/shadow"
description: "学习本地 shadow 记录如何表示密码哈希和期限策略，同时避免暴露敏感数据。"
meta_title: "/etc/shadow - 用户管理"
meta_description: "探索 Linux 中的 /etc/shadow 文件，它是用户身份验证的关键组件。了解如何使用 'cat /etc/shadow' 查看它，并理解存储加密密码和策略信息的 etc shadow 文件结构。"
meta_keywords: "etc shadow, etc/shadow 文件在 linux, cat /etc/shadow, linux 中的 etc shadow, /etc/shadow, 用户身份验证，密码安全，Linux 系统管理"
---

`/etc/shadow` 存储受保护的本地密码哈希和密码期限字段。把这些值与通常可读的 `/etc/passwd` 数据库分开，可以降低它们暴露于离线密码猜测攻击的风险。

## 保护 Shadow 数据

密码并不是以可逆“加密”形式存储，等待之后显示。本地密码条目通常包含单向密码哈希，并编码算法标识符、盐和参数。获得哈希的攻击者可以离线猜测候选密码，因此该数据库应保持受限。

确切的所有权和权限细节因系统而异，但访问通常仅限 root 和少数获准的系统组件。不要只为了检查账户状态就打印、复制、记录或分享 shadow 内容。

:::single-choice{#shadow-restricted-reason} 为什么本地 shadow 数据通常不允许一般读取访问？

::option[该文件包含每个用户未加密的当前密码。]{#shadow-plaintext-passwords explanation="正确的 shadow 条目存储单向密码哈希或特殊标记，而不是可取回的明文密码。"}
::option[密码哈希一旦泄露就可能遭到离线攻击。]{#shadow-offline-guessing .correct explanation="攻击者可以针对窃取的哈希测试密码猜测，而无需与登录服务交互。"}
::option[读取它会自动更改所有密码过期日期。]{#shadow-read-changes explanation="读取本身不会更新策略字段；风险在于敏感认证材料泄露。"}
:::

## 阅读九字段格式

本地 shadow 记录包含九个冒号分隔字段。以下是一个示意记录，其中有意省略了哈希：

```text
alice:<password-field>:20000:0:90:7:14:20500:
```

各字段为：

1. **登录名**。
2. **密码哈希或特殊密码标记**。
3. **上次更改密码的日期**，以自 1970-01-01 起的天数表示；在常见工具中，`0` 会要求用户在下次使用密码认证登录时更改密码。
4. **最短密码期限**，单位为天。
5. **最长密码期限**，单位为天。
6. 密码过期前的**警告期**，单位为天。
7. 密码过期后的**非活动期**，单位为天。
8. **账户过期日期**，以自 1970-01-01 起的天数表示。
9. **保留字段**。

空字段和特殊数值都有既定含义，具体可能随字段和工具而异。请使用账户管理命令，不要凭目测编辑数值。

:::single-choice{#shadow-account-expiration-field} 哪个 shadow 字段把账户过期日期存储为自 1970-01-01 起的天数？

::option[字段 3]{#shadow-field-three explanation="字段 3 记录上次更改密码的日期，而不是账户过期日期。"}
::option[字段 8]{#shadow-field-eight .correct explanation="第八个字段是账户过期日期的绝对天数。"}
::option[字段 5]{#shadow-field-five explanation="字段 5 记录最长密码期限。"}
:::

## 谨慎解释密码字段

字段 2 中的有效哈希支持本地 Unix 密码验证。以 `!` 开头的值通常会锁定该密码哈希，而 `*` 或其他无效哈希标记会阻止通过该字段成功验证密码。空值具有安全敏感性，并可能根据 PAM 策略允许无密码行为。

这些标记描述本地密码路径，而不是所有可能的认证方式。SSH 公钥、证书、令牌和应用特定凭据可能仍然可用，除非另行限制。字段 8 中的账户过期也不同于密码锁定。

:::single-choice{#shadow-password-lock-scope} 对于以 `!` 开头的 shadow 密码字段，可以安全得出什么结论？

::option[存储的 Unix 密码哈希已无法用于普通密码验证。]{#shadow-password-locked .correct explanation="在哈希前加 `!` 会阻止它通过 shadow 密码路径与所提供密码匹配。"}
::option[该账户的每一种可能登录方式都已禁用。]{#shadow-all-login-disabled explanation="其他认证方式可能相互独立，因此仅凭密码标记不能证明账户被完全锁定。"}
::option[该账户已从所有身份数据库中删除。]{#shadow-account-deleted explanation="shadow 记录仍然存在，删除账户是另一项独立的账户管理操作。"}
:::

## 区分密码日期和账户日期

字段 3 至 7 涉及密码期限：上次更改时间、何时允许再次更改、何时过期、何时开始警告，以及密码过期后还能在多长时间内登录。字段 8 会在绝对日期让账户过期，不受密码期限影响。

例如，最长密码期限为 90 天，并不等同于账户过期日期。前者相对于上次密码更改而移动，后者在管理员更改前是固定日期。

:::single-choice{#shadow-max-age-versus-expire} shadow 字段 5 和字段 8 有什么区别？

::option[字段 5 存储用户名，字段 8 存储登录 shell。]{#shadow-username-shell explanation="用户名是字段 1，登录 shell 记录在 `/etc/passwd` 中，而不是 shadow 记录中。"}
::option[字段 5 存储密码哈希，字段 8 存储其盐。]{#shadow-hash-salt explanation="密码哈希编码位于字段 2，期限字段不会另行存储其盐。"}
::option[字段 5 是最长密码期限，字段 8 是绝对账户过期日期。]{#shadow-password-vs-account-expiry .correct explanation="密码期限相对于上次更改，而账户过期以绝对天数存储。"}
:::

## 通过工具检查和更改策略

管理员应只查询任务所需的信息：

```bash
$ sudo passwd -S alice
$ sudo chage -l alice
```

`passwd -S` 汇总本地密码状态，`chage -l` 以可读形式列出期限信息。输出格式和授权要求可能随发行版而异。

使用 `passwd`、`chage`、`usermod` 和相关账户工具进行更改。如果无法避免手工修复本地 shadow 数据库，`vipw -s` 会提供锁定；请使用 `pwck` 验证账户数据库。远程更改认证前应保留恢复会话。

:::single-choice{#shadow-list-aging-policy} 哪个命令专门用于列出本地账户 `alice` 的可读密码期限信息？

::option[`cat /etc/shadow`]{#shadow-cat-entire-file explanation="这会暴露每一条本地 shadow 记录，披露的信息远超任务所需。"}
::option[`passwd -d alice`]{#shadow-passwd-delete explanation="`-d` 操作会删除密码哈希，是改变状态且安全敏感的操作，不是列表命令。"}
::option[`chage -l alice`]{#shadow-chage-list .correct explanation="小写 `-l` 选项会让 `chage` 以可读形式显示账户的密码期限字段。"}
:::

PAM 和 NSS 可以整合本地 shadow 文件之外的认证与身份来源。因此，系统账户可能没有本地 shadow 记录，也可能通过其他服务认证。

要在受控环境中练习账户状态和期限策略，可以尝试以下动手实验：

1. **[使用 useradd、usermod 和 userdel 管理 Linux 用户账户](https://labex.io/zh/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 练习用户管理的完整生命周期，从使用 `useradd` 和 `passwd` 创建并保护新账户，到修改和删除账户。
2. **[在 Linux 中配置用户账户和 Sudo 权限](https://labex.io/zh/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 学习管理用户账户和 sudo 权限的重要技术，包括实施密码策略和保护账户。

## 总结

现在，你可以在不暴露完整密码数据库的情况下解释 shadow 策略。

1. 把密码哈希视为受限认证材料。
2. 按用途阅读九个 shadow 字段。
3. 区分密码锁定与禁用每一种登录方式。
4. 区分密码期限和绝对账户过期。
5. 通过范围明确的账户工具检查和更改策略。
