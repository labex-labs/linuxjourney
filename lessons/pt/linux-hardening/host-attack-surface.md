---
lesson_id: "host-attack-surface"
course_id: "linux-hardening"
lang: "pt"
order_index: 1
title: "Superfície de ataque"
description: "Aprenda a identificar o que um host Linux precisa expor e quais caminhos de acesso merecem revisão."
meta_title: "Superfície de ataque - Hardening do Linux"
meta_description: "Aprenda a identificar o que um host Linux precisa expor e quais caminhos de acesso merecem revisão."
meta_keywords: "superfície de ataque, hardening do Linux, cibersegurança, Linux Journey"
---

Um host Linux pode ter uma página pública, acesso para manutenção e serviços em segundo plano. Comece anotando o que cada serviço faz e quem precisa acessá-lo. Depois, procure acessos sem uma finalidade clara.

## Listando os acessos previstos

Um inventário simples associa cada recurso às pessoas ou aos programas que precisam dele. Veja o exemplo de um host de prática.

```text
Resource           Intended access
Public homepage    Visitors
Maintenance SSH    Operations team
Preview panel      Local staff on this host only
```

Um **caminho de acesso** é a forma pela qual uma pessoa ou um programa chega a um recurso. O conjunto de interfaces acessíveis pelas quais alguém pode afetar um sistema faz parte de sua **superfície de ataque**.

:::single-choice{#host-attack-surface-intended-audience} Qual recurso desse inventário precisa ser acessível pela rede pública?

::option[O SSH de manutenção.]{#host-attack-surface-intended-audience-b explanation="O acesso destina-se à equipe de operações."}
::option[A página inicial pública.]{#host-attack-surface-intended-audience-a .correct explanation="O público inclui visitantes de fora do host."}
::option[O painel de pré-visualização.]{#host-attack-surface-intended-audience-c explanation="O uso previsto é local ao host."}
:::

## Comparando o acesso previsto com o observado

Imagine que o painel de pré-visualização esteja acessível pela rede, embora o inventário ainda indique acesso exclusivamente local. Confirme a finalidade com a pessoa responsável e verifique o caminho de acesso antes de fazer mudanças. Um serviço pode precisar ficar em execução sem aceitar requisições remotas.

:::single-choice{#host-attack-surface-mismatch} Qual observação merece revisão segundo a política descrita?

::option[Um visitante consegue acessar o painel de pré-visualização.]{#host-attack-surface-mismatch-b .correct explanation="Isso dá acesso ao painel a quem está fora do público previsto."}
::option[Um visitante consegue abrir a página inicial.]{#host-attack-surface-mismatch-a explanation="Esse é o uso previsto da página inicial."}
::option[A equipe consegue abrir a pré-visualização no próprio host.]{#host-attack-surface-mismatch-c explanation="O acesso local atende à necessidade descrita."}
:::

## Definindo prioridades

Comece pelos acessos desnecessários que podem ter consequências mais graves. No exercício, um painel de pré-visualização que permite alterar o site tem prioridade sobre um serviço sem uso nem dados importantes. Registre o público previsto, a exposição observada e o teste que confirmaria a restrição proposta sem atrapalhar os usuários legítimos.

:::single-choice{#host-attack-surface-priority-check} Depois de mudar o acesso à pré-visualização, quais duas observações confirmariam que a restrição atingiu o objetivo?

::option[O painel ainda aceita uma requisição local.]{#host-attack-surface-priority-check-a explanation="Isso confirma o acesso necessário. Ainda falta verificar o caminho remoto indevido."}
::option[A máquina reiniciou e usa o mesmo nome de host.]{#host-attack-surface-priority-check-b explanation="O estado do host não mostra se a política foi cumprida."}
::option[A equipe local mantém o acesso e o caminho remoto indevido está fechado.]{#host-attack-surface-priority-check-c .correct explanation="As duas verificações confirmam tanto o acesso necessário quanto a restrição."}
:::

## Resumo

Agora você consegue identificar quais caminhos de acesso merecem uma revisão de segurança.

1. Descreva o recurso e seu público previsto.
2. Compare o acesso previsto com o observado.
3. Após uma mudança, verifique tanto a proteção quanto o uso legítimo.
