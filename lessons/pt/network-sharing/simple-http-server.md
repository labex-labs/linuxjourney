---
lesson_id: "simple-http-server"
course_id: "network-sharing"
lang: "pt"
order_index: 3
title: "Servidor HTTP Simples"
description: "Aprenda a expor temporariamente um diretório controlado usando o servidor HTTP do Python."
meta_title: "Servidor HTTP Simples - Compartilhamento de Rede"
meta_description: "Aprenda a configurar rapidamente um servidor HTTP simples no Linux usando o módulo http.server do Python. Este guia explica como criar um servidor web Linux simples para facilitar o compartilhamento de arquivos em sua rede."
meta_keywords: "servidor http simples linux, servidor http simples no linux, servidor web linux simples, python http.server, o que é python simplehttpserver, compartilhamento de arquivos, servidor de rede"
---

O módulo `http.server` do Python pode servir arquivos estáticos para um teste curto ou transferência confiável. Não é servidor de produção e não oferece autenticação, autorização, TLS, limitação de taxa nem tratamento reforçado de tráfego hostil.

## Preparação do diretório compartilhado

Crie um diretório dedicado contendo apenas os arquivos destinados à exposição. Revise arquivos ocultos, links, permissões e metadados sensíveis. Não sirva o diretório pessoal, raiz de repositório, credenciais ou caminhos do sistema.

Use `--directory` para tornar a raiz explícita:

```bash
$ python3 -m http.server 8000 --directory /srv/temporary-share
```

Quando não há um arquivo de índice, o módulo normalmente gera uma listagem do diretório. Qualquer pessoa que consiga alcançar o socket em escuta pode enumerar e baixar o conteúdo servido.

:::single-choice{#http-server-directory-option}
Por que usar `--directory /srv/temporary-share`?

::option[Ele criptografa toda resposta HTTP automaticamente.]{#http-server-directory-tls explanation="A opção de diretório não acrescenta TLS."}
::option[Ele cria uma conta para cada pessoa que baixa.]{#http-server-directory-accounts explanation="O módulo básico não oferece autenticação."}
::option[Ele torna explícita a raiz de documentos pretendida.]{#http-server-explicit-root .correct explanation="Uma raiz explícita e revisada reduz a exposição acidental do diretório de trabalho."}
:::

## Controle do endereço de escuta

Vincule ao loopback quando somente o mesmo host deve acessar:

```bash
$ python3 -m http.server 8000 --bind 127.0.0.1 --directory /srv/temporary-share
```

Para compartilhar em rede confiável, vincule deliberadamente ao endereço apropriado e confirme o firewall. Sem bind restritivo, o comando costuma ouvir em todas as interfaces e pode expor o diretório além da rede pretendida.

:::single-choice{#http-server-loopback-bind}
Quem normalmente alcança um servidor vinculado a `127.0.0.1`?

::option[Clientes no mesmo host.]{#http-server-local-clients .correct explanation="Loopback serve a testes locais ou uso por um túnel configurado deliberadamente."}
::option[Qualquer host da Internet pública.]{#http-server-public explanation="Loopback é local ao namespace e não é interface pública."}
::option[Apenas dispositivos Bluetooth.]{#http-server-bluetooth explanation="O endereço não tem relação com Bluetooth."}
:::

## Teste do acesso

No host servidor, solicite um arquivo conhecido:

```bash
$ curl -f http://127.0.0.1:8000/example.txt
```

Para um teste remoto autorizado, use o endereço da interface selecionada em vez do loopback. Confirme tanto que o arquivo pretendido está acessível quanto que um arquivo fora da raiz de documentos não está. O sucesso no navegador por si só não comprova uma exposição apropriada nem a confidencialidade.

:::single-choice{#http-server-default-port-command}
Qual porta é escolhida em `python3 -m http.server 8000`?

::option[22]{#http-server-port-22 explanation="A porta 22 é associada ao SSH e não foi escolhida aqui."}
::option[8000]{#http-server-port-8000 .correct explanation="O operando posicional informa a porta de escuta."}
::option[443]{#http-server-port-443 explanation="O comando não configura HTTPS na porta 443."}
:::

## Encerramento e limpeza

Execute o serviço temporário num terminal supervisionado e pare com `Ctrl-C` ao concluir. Confirme que o listener sumiu:

```bash
$ ss -ltn 'sport = :8000'
```

Remova cópias temporárias conforme a política e reverta regras de firewall. Para distribuição persistente, autenticada ou pública, use servidor mantido com controle de acesso e TLS.

:::single-choice{#http-server-completion-check}
O que deve acontecer após a transferência temporária?

::option[Parar o serviço e confirmar que a porta não está mais ouvindo.]{#http-server-stop-verify .correct explanation="A verificação confirma que o serviço temporário realmente terminou."}
::option[Deixar o listener ativo para possível uso futuro.]{#http-server-leave-running explanation="A exposição desnecessária deve terminar com a finalidade autorizada."}
::option[Copiar mais arquivos privados para a raiz.]{#http-server-add-private explanation="Somente conteúdo intencional pertence ao diretório servido."}
:::

## Resumo

Agora você consegue executar um servidor HTTP temporário com exposição limitada.

1. Servir apenas um diretório dedicado e revisado.
2. Vincular ao endereço mais restrito adequado.
3. Testar acesso pretendido e limites não pretendidos.
4. Parar o listener e limpar o acesso temporário.
