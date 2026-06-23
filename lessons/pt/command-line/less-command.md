---
index: 8
lang: "pt"
title: "less"
meta_title: "less - Linha de Comando"
meta_description: "Aprenda o comando Linux less com exemplos para visualizar arquivos grandes, rolar, buscar, pular para linhas, seguir logs e sair do less."
meta_keywords: "comando less, linux less, visualizar arquivo grande linux, buscar no less, sair do less, less -N, less +F, visualizador de texto linux"
---

## Lesson Content

Ao visualizar arquivos de texto que são grandes demais para caber em uma única tela, o comando `less` é uma ferramenta indispensável. Como diz o antigo ditado do Unix, "menos é mais". Isso é um trocadilho pelo fato de que também existe um comando `more` com funcionalidade semelhante.

A utilidade `less` exibe texto em formato paginado, permitindo que você navegue por um arquivo sem inundar seu terminal.

### Começando com o Comando Less

Para começar a visualizar um arquivo, use `less` seguido do nome do arquivo.

```bash
$ less /home/pete/Documents/text1
```

Uma vez dentro do visualizador `less`, seus comandos padrão do shell não funcionarão. Em vez disso, você usa um conjunto específico de teclas para navegar e interagir com o texto.

### Navegação e Controles

Você pode usar várias teclas para se mover pelo documento:

- **Teclas de Seta e de Página**: Use `Page Up`, `Page Down`, `Up` e `Down` para navegar linha a linha ou página a página.
- **Ir para o Início**: Pressione `g` para ir diretamente ao começo do arquivo de texto.
- **Ir para o Fim**: Pressione `G` (Shift + g) para pular para o final do arquivo de texto.
- **Mover meia página**: Pressione `u` para subir e `d` para descer.
- **Menu de Ajuda**: Se você esquecer os comandos enquanto estiver no `less`, basta pressionar `h` para exibir um resumo útil.

### Buscando no Less

Um recurso poderoso do `less` é sua capacidade de buscar texto. Digite `/` seguido do texto que deseja encontrar e então pressione Enter.

- `/termo_de_busca`: Busca para frente por "termo_de_busca".
- `?termo_de_busca`: Busca para trás por "termo_de_busca".
- `n`: Vai para a próxima ocorrência do termo de busca.
- `N`: Vai para a ocorrência anterior.

### Como Sair do Less

Quando terminar de visualizar o arquivo, você precisa saber como `sair do less` e voltar ao seu prompt de comando.

- **Sair**: Simplesmente pressione `q` para sair do visualizador `less` e voltar ao seu shell.

### Opções Úteis do less

Você pode iniciar o `less` com opções:

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`: Mostrar números das linhas.
- `+G`: Abrir no final do arquivo.
- `+F`: Seguir o conteúdo novo conforme é adicionado, similar ao `tail -f`.

Enquanto estiver seguindo um arquivo com `+F`, pressione `Ctrl-C` para parar de seguir e voltar à navegação normal, depois pressione `q` para sair.

### Perguntas Comuns

**O less é melhor que o cat?** Use `cat` para arquivos curtos e `less` para arquivos longos ou arquivos que você precisa buscar.

**Como faço busca sem diferenciar maiúsculas de minúsculas?** Inicie o `less` com `-i`, ou digite buscas normalmente quando o padrão não tiver letras maiúsculas em muitos sistemas.

**O less pode abrir a saída de comandos?** Sim. Encaminhe a saída para ele, como `dmesg | less`.

## Exercise

Praticar é essencial! Aqui estão alguns laboratórios práticos para reforçar seu entendimento sobre visualização e navegação de arquivos de texto no Linux:

1. **[Comando Linux less: Paginação de Arquivos](https://labex.io/pt/labs/linux-linux-less-command-file-paging-214301)** - Aprenda o comando Linux 'less' para visualização eficiente de arquivos de texto e navegação, incluindo busca, números de linha e correspondência de padrões.
2. **[Comando Linux more: Rolagem de Arquivos](https://labex.io/pt/labs/linux-linux-more-command-file-scrolling-214299)** - Aprenda o comando Linux 'more' para visualização eficiente de arquivos de texto, cobrindo uso básico, início em linhas específicas e personalização da exibição.
3. **[Visualizando Arquivos de Log e Configuração no Linux](https://labex.io/pt/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Aprenda habilidades essenciais de linha de comando Linux para visualizar e navegar eficientemente arquivos de texto, incluindo logs do sistema e arquivos de configuração, usando comandos como `cat`, `more` e `less`.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e ganhar confiança na manipulação e navegação de arquivos de texto.

## Quiz Question

Como você sai do comando `less`? Por favor, forneça a tecla de caractere único como sua resposta. Nota: a resposta é uma letra inglesa sensível a maiúsculas.

## Quiz Answer

q
