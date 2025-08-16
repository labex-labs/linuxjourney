---
lang: "pt"
title: "Servidor HTTP Simples"
description: "Aprenda a criar um servidor HTTP simples usando o módulo http.server do Python. Compartilhe arquivos rapidamente em sua rede com este tutorial de Linux para iniciantes."
keywords: "http.server, SimpleHTTPServer, servidor web Python, compartilhamento de arquivos, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Python possui uma ferramenta super útil para servir arquivos via HTTP. Isso é ótimo se você quiser apenas criar um compartilhamento de rede rápido que outras máquinas em sua rede possam acessar. Para fazer isso, basta ir para o diretório que você deseja compartilhar e executar:

```bash
python -m http.server
```

Ou, se você ainda estiver usando Python 2:

```bash
python -m SimpleHTTPServer
```

Isso configura um servidor web básico que você pode acessar via endereço localhost. Então, pegue o endereço IP da máquina onde você executou isso e, em outra máquina, acesse-o no navegador com: `http://IP_ADDRESS:8000`. Em sua própria máquina, você pode visualizar os arquivos disponíveis digitando: `http://localhost:8000` em seu navegador web.

## Exercise

Experimente configurar um `http.server`!

## Quiz Question

Qual ferramenta você pode usar para criar um servidor HTTP simples com Python?

## Quiz Answer

http.server
