---
index: 3
lang: "pt"
title: "Servidor HTTP Simples"
meta_title: "Servidor HTTP Simples - Compartilhamento de Rede"
meta_description: "Aprenda a criar um servidor HTTP simples usando o módulo http.server do Python. Compartilhe arquivos rapidamente em sua rede com este tutorial de Linux para iniciantes."
meta_keywords: "http.server, SimpleHTTPServer, servidor web Python, compartilhamento de arquivos, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Python tem uma ferramenta super útil para servir arquivos via HTTP. Isso é ótimo se você quiser apenas criar um compartilhamento de rede rápido que outras máquinas na sua rede possam acessar. Para fazer isso, basta ir para o diretório que você deseja compartilhar e executar:

```bash
python -m http.server
```

Ou, se você ainda estiver no Python 2:

```bash
python -m SimpleHTTPServer
```

Isso configura um servidor web básico que você pode acessar via endereço localhost. Então, pegue o endereço IP da máquina onde você executou isso e, em outra máquina, acesse-o no navegador com: `http://IP_ADDRESS:8000`. Na sua própria máquina, você pode visualizar os arquivos disponíveis digitando: `http://localhost:8000` no seu navegador web.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da conectividade de rede e endereçamento IP, que são essenciais para compartilhar arquivos em uma rede:

1. **[Explorar Tipos de Endereço IP e Acessibilidade no Linux](https://labex.io/pt/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Pratique a identificação de diferentes tipos de endereço IP e o teste de acessibilidade de rede, crucial para garantir que seu servidor HTTP Python esteja acessível.
2. **[Identificar Endereços MAC e IP no Linux](https://labex.io/pt/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Aprenda a usar o comando `ip a` para encontrar o endereço IP da sua máquina, um passo necessário antes de acessar seus arquivos compartilhados de outro dispositivo.
3. **[Gerenciar Resolução de Hostname Local no Linux](https://labex.io/pt/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Aprenda a gerenciar a resolução de hostname local no Linux editando o arquivo /etc/hosts, uma habilidade chave para desenvolvimento web e testes de rede.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com operações básicas de rede no Linux.

## Quiz Question

Qual ferramenta você pode usar para criar um servidor HTTP simples com Python?

## Quiz Answer

http.server
