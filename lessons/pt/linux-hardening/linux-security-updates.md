---
lesson_id: "linux-security-updates"
course_id: "linux-hardening"
lang: "pt"
order_index: 7
title: "Atualizações de segurança"
description: "Aprenda a revisar atualizações de pacotes disponíveis e a verificar um serviço após uma manutenção autorizada."
meta_title: "Atualizações de segurança - Hardening do Linux"
meta_description: "Aprenda a revisar atualizações de pacotes disponíveis e a verificar um serviço após uma manutenção autorizada."
meta_keywords: "atualizações de segurança, pacotes Linux, hardening do Linux, cibersegurança, Linux Journey"
---

Uma atualização de segurança pode corrigir um defeito em um software instalado. Comece descobrindo qual versão está instalada e qual correção está disponível para seu sistema operacional. Planeje a mudança tendo em vista o serviço usado pelas pessoas.

## Consultando as atualizações disponíveis

Em um host Ubuntu de prática, este comando de consulta lista os pacotes que o APT sabe que podem ser atualizados. Ele usa informações de pacotes que já estão no host.

```bash
$ apt list --upgradable
```

Cada pacote listado tem uma versão candidata mais recente nos dados disponíveis. Consulte o aviso de segurança da sua distribuição para saber se a atualização contém a correção necessária. Uma lista vazia também pode indicar que as informações disponíveis estão desatualizadas.

:::single-choice{#linux-security-updates-candidate-is-listed} Um pacote aparece na lista. O que isso informa?

::option[A atualização já foi aplicada.]{#linux-security-updates-candidate-is-listed-a explanation="A lista mostra uma versão candidata disponível para atualização."}
::option[O APT conhece uma versão candidata mais recente para o pacote instalado.]{#linux-security-updates-candidate-is-listed-b .correct explanation="É isso que os dados locais dos pacotes indicam no momento."}
::option[Toda versão candidata mais recente é uma atualização de segurança.]{#linux-security-updates-candidate-is-listed-c explanation="Consulte o comunicado da distribuição para saber o motivo da atualização."}
:::

## Planejando a mudança

Uma mudança aprovada deve indicar o serviço, a versão desejada e a janela de manutenção. Algumas atualizações só entram em vigor depois que o serviço ou a máquina reinicia. Planeje uma requisição de verificação e uma forma de recuperação antes de alterar o host.

:::single-choice{#linux-security-updates-reboot-check} Uma atualização de pacote corrige código usado por um serviço que está em execução há algum tempo. O que verificar depois da instalação?

::option[Se o serviço precisa reiniciar para usar o código atualizado.]{#linux-security-updates-reboot-check-a .correct explanation="Um processo em execução ainda pode ter o código antigo carregado."}
::option[Se a atualização estava na lista de pacotes antes da instalação.]{#linux-security-updates-reboot-check-b explanation="A disponibilidade ajuda a planejar a manutenção. A versão carregada pelo processo exige outra verificação."}
::option[Se a lista agora deixou de mostrar atualizações pendentes.]{#linux-security-updates-reboot-check-c explanation="Mesmo com os pacotes atualizados, um processo ainda pode estar usando o código antigo."}
:::

## Verificando o resultado

Confirme que a versão instalada corresponde à aprovada. Teste o serviço pelo caminho usado pelos usuários e anote o resultado. Se a correção envolver um componente em execução, confirme também que a versão atualizada está em uso.

:::single-choice{#linux-security-updates-security-verification} Qual par de observações dá mais evidência de que a atualização do serviço foi concluída?

::option[O comando de listagem é executado duas vezes.]{#linux-security-updates-security-verification-a explanation="Repetir a listagem não mostra se o serviço funciona."}
::option[O chamado de manutenção recebeu um novo título.]{#linux-security-updates-security-verification-b explanation="O título não mostra o estado do serviço em execução."}
::option[A versão aprovada está em uso e uma requisição representativa funciona.]{#linux-security-updates-security-verification-c .correct explanation="Isso confirma o estado do software e o serviço de que as pessoas dependem."}
:::

## Lendo dois sinais sobre a versão

Um pacote instalado e o programa que atende às requisições podem temporariamente estar em versões diferentes. Por exemplo, o inventário pode mostrar a versão corrigida enquanto um processo iniciado antes da atualização continua em execução. Para concluir a revisão, consulte evidências sobre o processo em execução.

:::single-choice{#linux-security-updates-final-application} O que ainda precisa ser verificado quando a versão instalada foi corrigida e o processo antigo continua presente?

::option[Se todos os outros processos da máquina precisam ser substituídos.]{#linux-security-updates-final-application-c explanation="A pergunta diz respeito ao serviço atualizado e aos requisitos de manutenção aprovados para ele."}
::option[Se o programa atualizado é o que atende às requisições.]{#linux-security-updates-final-application-a .correct explanation="O inventário verifica os arquivos instalados. A verificação do processo mostra qual versão o serviço usa."}
::option[Se havia algum pacote de atualização disponível.]{#linux-security-updates-final-application-b explanation="O pacote instalado já mostra a versão corrigida."}
:::

## Resumo

Agora você consegue acompanhar uma atualização desde a identificação da versão candidata até a verificação.

1. Distinga atualizações disponíveis de mudanças já instaladas.
2. Preveja reinicializações e opções de recuperação no plano.
3. Verifique a versão em execução e o comportamento esperado do serviço.
