---
index: 8
lang: "pt"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "Aprenda a usar o comando 'head' do Linux para visualizar o início de arquivos. Entenda opções como -n para contagem de linhas. Tutorial essencial de comando Linux."
meta_keywords: "comando head, head Linux, visualizar início de arquivo, tutorial Linux, comandos Linux, Linux para iniciantes, head -n, guia Linux"
---

## Lesson Content

Digamos que temos um arquivo muito longo; na verdade, temos muitos para escolher. Vá em frente e `cat /var/log/syslog`. Você deve ver páginas e páginas de texto. E se eu quisesse ver apenas as primeiras linhas deste arquivo de texto? Bem, podemos fazer isso com o comando `head`. Por padrão, o comando `head` mostrará as primeiras 10 linhas de um arquivo.

```bash
head /var/log/syslog
```

Você também pode modificar a contagem de linhas para o que quiser. Digamos que eu quisesse ver as primeiras 15 linhas em vez disso.

```bash
head -n 15 /var/log/syslog
```

A flag `-n` significa "número de linhas".

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre a visualização do início de arquivos e a manipulação geral de arquivos de texto:

1. **[Comando head do Linux: Exibição do Início do Arquivo](https://labex.io/pt/labs/linux-linux-head-command-file-beginning-display-214302)** - Este laboratório o guiará no uso do comando `head` para exibir as linhas iniciais de arquivos de texto, incluindo a modificação da contagem de linhas.
2. **[Visualizando Arquivos de Log e Configuração no Linux](https://labex.io/pt/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Pratique habilidades essenciais da linha de comando do Linux para visualizar e navegar eficientemente em arquivos de texto, incluindo logs do sistema e arquivos de configuração, que frequentemente exigem comandos como `head`.
3. **[Detecção Rápida de Ameaças](https://labex.io/pt/labs/linux-rapid-threat-detection-387930)** - Aplique seu conhecimento de `head` (e `tail`) para extrair e analisar rapidamente entradas de log recentes, simulando análises de segurança cibernética do mundo real.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com a visualização e análise de arquivos de texto no Linux.

## Quiz Question

Qual flag você usaria para alterar o número de linhas que deseja visualizar para o comando `head`?

## Quiz Answer

-n
