---
index: 3
lang: "pt"
title: "Servidor HTTP Simples"
meta_title: "Servidor HTTP Simples - Compartilhamento de Rede"
meta_description: "Aprenda a configurar rapidamente um servidor HTTP simples no Linux usando o módulo http.server do Python. Este guia explica como criar um servidor web Linux simples para facilitar o compartilhamento de arquivos em sua rede."
meta_keywords: "servidor http simples linux, servidor http simples no linux, servidor web linux simples, python http.server, o que é python simplehttpserver, compartilhamento de arquivos, servidor de rede"
---

## Lesson Content

O Python inclui um módulo integrado que permite criar instantaneamente um servidor web, o que é incrivelmente útil para compartilhar arquivos em uma rede. Configurar um **servidor http simples linux** é um processo direto que requer apenas um único comando.

### Iniciando um Servidor HTTP Simples no Linux

Para começar, navegue até o diretório que deseja compartilhar usando seu terminal. Depois de estar no diretório desejado, você pode iniciar um ambiente de **servidor http simples linux** com o seguinte comando se estiver usando Python 3:

```bash
python -m http.server
```

Este comando inicia um servidor web básico, tornando o conteúdo do seu diretório atual acessível via HTTP.

### Método Legado para Python 2

Para sistemas mais antigos que ainda usam Python 2, o comando é ligeiramente diferente. O módulo era anteriormente chamado de `SimpleHTTPServer`. Se você já se perguntou **o que é python simplehttpserver**, é simplesmente o equivalente do Python 2 para o módulo `http.server`. Você pode executá-lo com:

```bash
python -m SimpleHTTPServer
```

### Acessando Seu Servidor Web Linux Simples

Após executar o comando, seu **servidor web linux simples** estará ativo. Você pode acessar os arquivos compartilhados de outra máquina na mesma rede abrindo um navegador da web e navegando para `http://ENDERECO_IP:8000`, substituindo `ENDERECO_IP` pelo IP local da máquina que executa o servidor.

Para visualizar os arquivos na mesma máquina, você pode usar o endereço localhost: `http://localhost:8000`.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de conectividade de rede e endereçamento IP, que são essenciais para compartilhar arquivos em uma rede:

1. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Pratique a identificação de diferentes tipos de endereço IP e o teste de acessibilidade da rede, crucial para garantir que seu servidor HTTP Python seja acessível.
2. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Aprenda a usar o comando `ip a` para encontrar o endereço IP da sua máquina, um passo necessário antes de acessar seus arquivos compartilhados de outro dispositivo.
3. **[Gerenciar a Resolução de Nome de Host Local no Linux](https://labex.io/pt/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Aprenda a gerenciar a resolução de nome de host local no Linux editando o arquivo /etc/hosts, uma habilidade chave para desenvolvimento web e testes de rede.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança com operações básicas de rede no Linux.

## Quiz Question

Para o Python 3, qual é o nome do módulo usado para criar um servidor HTTP simples? (Por favor, responda em inglês, prestando atenção à sensibilidade de maiúsculas e minúsculas).

## Quiz Answer

http.server
