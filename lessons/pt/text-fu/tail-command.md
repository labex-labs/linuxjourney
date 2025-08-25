---
index: 9
lang: "pt"
title: "tail"
meta_title: "tail - Text-Fu"
meta_description: "Aprenda a usar o comando `tail` no Linux para visualizar o final de arquivos e monitorar logs. Descubra `tail -f` para atualizações em tempo real. Comece sua jornada no Linux!"
meta_keywords: "comando tail, tail Linux, tail -f, visualizar logs, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Semelhante ao comando `head`, o comando `tail` permite que você veja as últimas 10 linhas de um arquivo por padrão.

```bash
tail /var/log/syslog
```

Assim como o `head`, você pode alterar o número de linhas que deseja ver.

```bash
tail -n 10 /var/log/syslog
```

Outra ótima opção que você pode usar é a flag `-f` (follow); isso seguirá o arquivo à medida que ele cresce. Experimente e veja o que acontece.

```bash
tail -f /var/log/syslog
```

Seu arquivo `syslog` estará em constante mudança enquanto você interage com seu sistema, e usando `tail -f` você pode ver tudo o que está sendo adicionado a esse arquivo.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do comando `tail` e suas aplicações:

1. **[Comando tail do Linux: Exibição do Final do Arquivo](https://labex.io/pt/labs/linux-linux-tail-command-file-end-display-214303)** - Aprenda o comando `tail` do Linux para visualizar e monitorar o final de arquivos de texto, incluindo a opção `-f` para atualizações em tempo real.
2. **[Visualizando Arquivos de Log e Configuração no Linux](https://labex.io/pt/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Pratique o uso de `tail` (juntamente com `cat` e `more`) para visualizar e navegar eficientemente em arquivos de log e configuração, o que é crucial para o monitoramento do sistema.
3. **[Detecção Rápida de Ameaças](https://labex.io/pt/labs/linux-rapid-threat-detection-387930)** - Aplique seu conhecimento de `tail` para extrair e analisar rapidamente entradas de log recentes, simulando a detecção rápida de ameaças em um contexto de cibersegurança.

Esses laboratórios o ajudarão a aplicar os conceitos de visualização e monitoramento de conteúdo de arquivos em cenários reais e a construir confiança com o comando `tail`.

## Quiz Question

Qual é a flag usada para seguir um arquivo em `tail`?

## Quiz Answer

-f
