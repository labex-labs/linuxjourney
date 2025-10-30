---
index: 2
lang: "pt"
title: "route"
meta_title: "route - Configuração de Rede"
meta_description: "Aprenda como adicionar e excluir rotas de rede usando os comandos Linux route e ip. Entenda o gerenciamento da tabela de roteamento para usuários iniciantes e intermediários."
meta_keywords: "comando route, ip route, adicionar rota, excluir rota, redes Linux, tabela de roteamento, tutorial Linux, guia para iniciantes"
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

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre roteamento de rede e endereçamento IP:

1. **[Gerenciar Endereçamento IP no Linux](https://labex.io/pt/labs/comptia-manage-ip-addressing-in-linux-592736)** - Pratique a configuração de um IP estático, a definição de um gateway padrão e a verificação da configuração de rede usando o comando `ip`.
2. **[Explorar a Interação da Camada de Rede com ping e arp no Linux](https://labex.io/pt/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Aprenda como o gateway padrão lida com o tráfego remoto e observe as interações da camada de rede.

Esses laboratórios o ajudarão a aplicar os conceitos de endereçamento IP e roteamento em cenários reais e a construir confiança com redes Linux.

## Quiz Question

Qual é a flag de comando para excluir uma rota?

## Quiz Answer

del
