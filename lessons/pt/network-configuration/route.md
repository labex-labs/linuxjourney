---
index: 2
lang: "pt"
title: "route"
meta_title: "route - Configuração de Rede"
meta_description: "Aprenda como adicionar e excluir rotas de rede usando os comandos Linux route e ip. Entenda o gerenciamento da tabela de roteamento para usuários iniciantes e intermediários."
meta_keywords: "comando route, ip route, adicionar rota, excluir rota, rede Linux, tabela de roteamento, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Já discutimos a visualização de nossas tabelas de roteamento com o comando `route`. Se você quiser adicionar ou remover rotas, pode fazê-lo manualmente.

### Adicionar uma nova rota

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### Excluir uma rota

```bash
sudo route del -net 192.168.2.1/23
```

Você também pode realizar essas alterações com o comando **ip**:

### Para adicionar uma rota

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### Para excluir uma rota

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

Não há exercícios para esta lição, mas você pode ler mais informações sobre os comandos discutidos aqui nas páginas man.

```bash
man route
```

```bash
man ip-route
```

## Quiz Question

Qual é a flag de comando para excluir uma rota?

## Quiz Answer

del
