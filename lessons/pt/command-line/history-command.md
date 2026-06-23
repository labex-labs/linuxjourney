---
index: 9
lang: "pt"
title: "history"
meta_title: "history - Linha de Comando"
meta_description: "Aprenda o comando history no Linux com exemplos para visualizar o histórico de comandos, executar comandos novamente, busca reversa, excluir entradas e limpar o terminal."
meta_keywords: "comando history linux, histórico bash, history -c, history -d, history -w, Ctrl-R, histórico de comandos, comando clear"
---

## Lesson Content

Seu shell mantém um registro dos comandos que você digitou anteriormente. Você pode acessar essa lista quando quiser encontrar e reutilizar um comando sem precisar digitá-lo novamente. O comando `history` é uma ferramenta fundamental no Bash e em muitos ambientes de shell semelhantes ao Unix.

### Visualizando seu Histórico de Comandos

Para ver a lista de comandos que você usou, digite `history`.

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

Cada linha tem um número do histórico seguido pelo comando.

### Executando Comandos Anteriores Novamente

O shell oferece vários atalhos para facilitar a execução de comandos anteriores.

- **Seta para cima**: Quer executar o mesmo comando que acabou de usar? Basta pressionar a tecla de seta para cima para navegar para trás pelo seu histórico.
- **Atalho `!!`**: Para executar o comando mais recente novamente, você pode usar `!!`. Por exemplo, se você acabou de rodar `cat file1`, digitar `!!` e pressionar Enter executará `cat file1` novamente.
- **Executar por número**: Use `!102` para executar o comando número 102 do seu histórico.
- **Executar por prefixo**: Use `!cat` para executar o comando mais recente que começou com `cat`.

### Buscando no Seu Histórico

Um dos atalhos mais poderosos do histórico é `Ctrl-R`. Isso inicia uma busca reversa. Após pressionar `Ctrl-R`, comece a digitar qualquer parte do comando que você está procurando, e o shell exibirá a correspondência mais recente. Você pode pressionar `Ctrl-R` repetidamente para navegar por correspondências mais antigas. Quando encontrar o comando desejado, basta pressionar Enter para executá-lo.

Se quiser editar o comando encontrado antes de executá-lo, pressione a tecla de seta para a direita ou para a esquerda em vez de Enter.

### Gerenciando a Lista de Histórico

Além de apenas visualizar seu histórico, você também pode gerenciá-lo diretamente.

- **Limpar a lista atual de histórico**: `history -c` remove todas as entradas da lista de histórico na memória.
- **Gravar histórico no arquivo**: `history -w` salva o histórico da sessão atual no seu arquivo de histórico, geralmente `~/.bash_history`.
- **Excluir uma entrada específica**: `history -d <offset>` remove um comando pelo seu número no histórico.

Exemplos:

```bash
$ history -d 101
$ history -w
```

Tenha cuidado com comandos de expansão do histórico como `!!` e `!102`. Use `history` primeiro para confirmar o que será executado.

### Outras Ferramentas Úteis no Terminal

À medida que a janela do seu terminal vai se enchendo, você pode querer limpá-la. Use o comando `clear` para apagar a tela e começar com um display limpo.

```bash
$ clear
```

Outra funcionalidade indispensável é o preenchimento automático com a tecla Tab. Se você começar a digitar o início de um comando, nome de arquivo ou diretório e pressionar a tecla Tab, o shell tentará completar automaticamente. Se houver múltiplas possibilidades, ele pode mostrar as opções ou não fazer nada. Pressionar Tab uma segunda vez geralmente lista todas as possíveis conclusões.

### Perguntas Comuns

**Onde o histórico do Bash é armazenado?** Geralmente em `~/.bash_history`, embora o comportamento exato dependa das configurações do shell.

**O histórico inclui todos os comandos imediatamente?** Nem sempre. Alguns shells gravam o histórico apenas quando a sessão termina, a menos que configurados de outra forma.

**O histórico pode conter dados sensíveis?** Sim. Evite digitar senhas, tokens ou segredos diretamente em comandos.

**Qual a diferença entre history -c e clear?** `history -c` limpa o histórico de comandos na memória. `clear` apenas limpa a tela do terminal.

## Exercise

Embora não existam laboratórios específicos para este tópico, recomendamos explorar o abrangente [Caminho de Aprendizado Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual é o comando para limpar o terminal? (Por favor, responda apenas com letras minúsculas em inglês)

## Quiz Answer

clear
