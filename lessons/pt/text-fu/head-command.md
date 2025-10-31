---
index: 8
lang: "pt"
title: "cabeçalho"
meta_title: "cabeçalho - Text-Fu"
meta_description: "Um guia Linux para iniciantes sobre como usar o comando head para visualizar o início de um arquivo. Aprenda a usar a opção head -n para controlar a contagem de linhas, uma habilidade essencial para qualquer tutorial Linux."
meta_keywords: "comando head, Linux head, visualizar início arquivo, tutorial Linux, comandos Linux, Linux iniciante, head -n, guia Linux, arquivos de texto, linha de comando"
---

## Lesson Content

No Linux, muitas vezes você precisa inspecionar o conteúdo de arquivos muito grandes, como logs de sistema. Por exemplo, se você executar `cat /var/log/syslog`, verá páginas de texto rolando, dificultando a obtenção de uma visão geral rápida. Então, e se você quiser apenas **visualizar o início de um arquivo**? O comando `head` é a ferramenta perfeita para este trabalho.

### Comportamento Padrão do Comando head

Por padrão, o comando `head` exibe as primeiras 10 linhas de qualquer arquivo fornecido. Esta é uma parte fundamental do nosso **guia Linux para iniciantes** para lidar com texto. Para vê-lo em ação, basta fornecer um nome de arquivo como argumento:

```bash
head /var/log/syslog
```

Este comando exibirá as primeiras 10 linhas de `/var/log/syslog`, permitindo que você verifique rapidamente o conteúdo inicial do arquivo sem abri-lo em um editor.

### Personalizando a Contagem de Linhas

O comando **Linux head** é flexível. Você pode facilmente alterar o número de linhas que ele exibe usando a flag `-n`, que significa "número de linhas". Por exemplo, se você quiser ver as primeiras 15 linhas de um arquivo, você usaria a opção `head -n` assim:

```bash
head -n 15 /var/log/syslog
```

Isso torna o `head` um dos **comandos Linux** mais úteis para inspecionar rapidamente cabeçalhos de arquivos ou entradas de log.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre a visualização do início de arquivos e manipulação geral de arquivos de texto:

1. **[Comando Linux head: Exibição do Início do Arquivo](https://labex.io/pt/labs/linux-linux-head-command-file-beginning-display-214302)** - Este laboratório o guiará no uso do comando `head` para exibir as linhas iniciais de arquivos de texto, incluindo a modificação da contagem de linhas.
2. **[Visualizando Arquivos de Log e Configuração no Linux](https://labex.io/pt/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Pratique habilidades essenciais de linha de comando Linux para visualizar e navegar eficientemente por arquivos de texto, incluindo logs de sistema e arquivos de configuração, que frequentemente exigem comandos como `head`.
3. **[Detecção Rápida de Ameaças](https://labex.io/pt/labs/linux-rapid-threat-detection-387930)** - Aplique seu conhecimento de `head` (e `tail`) para extrair e analisar rapidamente entradas de log recentes, simulando análises de segurança cibernética do mundo real.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a construir confiança na visualização e análise de arquivos de texto no Linux.

## Quiz Question

Qual flag você usaria com o comando `head` para alterar o número de linhas que deseja visualizar? Por favor, responda usando apenas a flag em inglês, prestando atenção à sensibilidade a maiúsculas e minúsculas.

## Quiz Answer

-n
