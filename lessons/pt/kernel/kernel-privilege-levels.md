---
lesson_id: "kernel-privilege-levels"
course_id: "kernel"
lang: "pt"
order_index: 2
title: "Níveis de Privilégio"
description: "Aprenda como o privilégio do processador separa a execução de usuário da execução confiável do kernel."
meta_title: "Níveis de Privilégio - Kernel"
meta_description: "Explore os conceitos centrais dos níveis de privilégio do Linux. Esta lição explica a diferença entre modo kernel e modo usuário, o papel dos anéis de proteção e como as chamadas de sistema fornecem acesso privilegiado ao hardware. Entenda como o kernel gerencia a segurança e os privilégios do kernel."
meta_keywords: "Níveis de privilégio Linux, modo kernel, modo usuário, anéis de proteção, chamadas de sistema, acesso privilegiado, privilégios do kernel, qual a diferença entre modo kernel e modo usuário, segurança Linux"
---

Os processadores oferecem modos de privilégio que restringem instruções sensíveis e acesso à memória. O Linux usa esse limite do hardware para que falhas comuns em aplicativos não sobrescrevam diretamente a memória do kernel nem reconfigurem dispositivos. O kernel controla as transições para a execução privilegiada.

## Modo usuário

Um processo comum é executado em modo usuário dentro de seu espaço de endereços virtual. Ele pode realizar cálculos e acessar os mapeamentos concedidos pelo kernel, que podem ser grandes; modo usuário não significa “apenas pouca memória”. Ele não acessa diretamente qualquer endereço físico, mapeamentos privados de outro processo nem controles privilegiados do processador.

Tabelas de páginas e bits de proteção impõem o acesso. Se uma thread referencia um endereço inválido ou proibido, o processador entra no kernel, que pode resolver um page fault válido ou entregar um sinal como `SIGSEGV`.

:::single-choice{#kernel-privilege-user-mode-memory} Que memória um processo em modo usuário normalmente acessa diretamente?

::option[Todos os endereços da RAM física e toda a memória do kernel.]{#kernel-privilege-all-physical explanation="O privilégio e a proteção da memória virtual impedem esses acessos."}
::option[Apenas um byte fixo escolhido no início do processo.]{#kernel-privilege-one-byte explanation="Um processo pode ter muitas regiões mapeadas sem deixar de ser não privilegiado."}
::option[Mapeamentos permitidos em seu próprio espaço de endereços virtual.]{#kernel-privilege-own-mappings .correct explanation="As proteções de páginas restringem o processo aos mapeamentos estabelecidos com o acesso apropriado."}
:::

## Modo kernel

O modo kernel permite instruções privilegiadas e acesso aos mapeamentos protegidos necessários para memória, escalonamento, interrupções e drivers. Em x86, a divisão do Linux costuma ser descrita como ring 0 para o kernel e ring 3 para processos de usuário. O Linux normalmente não usa rings 1 e 2 para isolamento comum.

Outras arquiteturas têm nomes e mecanismos diferentes, como exception levels. A virtualização acrescenta relações entre hypervisor e guests que não cabem num desenho simples de dois anéis. A ideia essencial é o privilégio controlado, não os números do x86.

:::single-choice{#kernel-privilege-x86-kernel-ring} Qual anel de proteção x86 normalmente executa o kernel Linux?

::option[Ring 3.]{#kernel-privilege-ring-three explanation="Ring 3 é o nível convencional do modo usuário."}
::option[Ring 0.]{#kernel-privilege-ring-zero .correct explanation="O kernel usa o anel tradicional mais privilegiado do x86."}
::option[Ring 7.]{#kernel-privilege-ring-seven explanation="Os anéis de proteção tradicionais do x86 vão de 0 a 3."}
:::

## Transições controladas

Vários eventos transferem o controle a um ponto de entrada do kernel:

- uma instrução de chamada de sistema solicita um serviço
- uma exceção informa um page fault ou instrução inválida
- uma interrupção de hardware informa um evento externo

O processador salva o contexto, muda o privilégio pelo mecanismo configurado e começa a executar código confiável do kernel. O kernel valida o pedido, realiza ou rejeita o trabalho e retorna ao modo usuário quando apropriado.

O aplicativo não se transforma temporariamente em código do kernel. A CPU executa um handler do kernel em nome da thread, com pilhas e mapeamentos controlados pelo kernel.

:::single-choice{#kernel-privilege-system-call-transition} O que acontece durante uma transição de chamada de sistema?

::option[O código do aplicativo recebe execução irrestrita em ring 0.]{#kernel-privilege-user-ring-zero explanation="Somente código confiável do kernel é executado depois da entrada controlada."}
::option[O processo muda permanentemente seu UID para zero.]{#kernel-privilege-uid-zero explanation="A transição do modo do processador não reescreve credenciais."}
::option[O controle entra em um handler definido do kernel que valida o pedido.]{#kernel-privilege-kernel-handler .correct explanation="O processador muda de modo por um caminho configurado e preserva o contexto do usuário para retornar."}
:::

## Privilégio da CPU não é identidade do usuário

Um aplicativo executado como usuário `root` continua normalmente em modo usuário. O UID 0 influencia verificações de autorização, mas não permite que suas instruções acessem diretamente a memória do kernel. Inversamente, o código do kernel executa em modo privilegiado qualquer que seja o usuário que causou a chamada.

Capabilities, namespaces, seccomp, módulos de segurança e cgroups restringem ainda mais o que um processo solicita. Essa política em camadas é separada do limite de hardware.

:::single-choice{#kernel-privilege-root-distinction} Qual afirmação compara corretamente a identidade root e o modo kernel?

::option[Root é uma credencial do espaço do usuário; modo kernel é um privilégio de execução do processador.]{#kernel-privilege-credential-versus-mode .correct explanation="Um processo root faz pedidos autorizados do modo usuário, enquanto código confiável do kernel realiza a execução privilegiada."}
::option[Toda instrução pertencente ao root roda como código carregável do kernel.]{#kernel-privilege-root-kernel-code explanation="O UID proprietário não transforma um executável em módulo do kernel."}
::option[Modo kernel é outro nome de usuário armazenado em `/etc/passwd`.]{#kernel-privilege-kernel-username explanation="Modos do processador são estados de hardware, não contas de login."}
:::

## Por que o limite importa

O limite reduz o dano de falhas comuns e cria um ponto para verificações de acesso, mas vulnerabilidades no kernel e módulos maliciosos podem derrotá-lo. Atualize kernel e firmware por canais confiáveis, reduza o código privilegiado e não carregue módulos desconhecidos.

Execução especulativa e canais laterais também mostram que o isolamento exige mitigação contínua; “outro anel” é uma base, não uma prova completa de segurança.

:::single-choice{#kernel-privilege-boundary-limit} A separação entre modo usuário e kernel garante segurança completa?

::option[Sim; vulnerabilidades do kernel não afetam processos de usuário.]{#kernel-privilege-no-kernel-vulns explanation="Uma vulnerabilidade do kernel pode comprometer todo o sistema."}
::option[Não; falhas no código privilegiado e canais laterais ainda podem cruzar limites.]{#kernel-privilege-not-complete .correct explanation="A divisão reduz a superfície de ataque, mas exige código correto e mitigação adicional."}
::option[Sim; os modos eliminam a necessidade de políticas de acesso.]{#kernel-privilege-no-policy explanation="Credenciais e políticas continuam essenciais para compartilhar recursos com autorização."}
:::

## Resumo

Agora você consegue distinguir privilégio de execução do hardware de autoridade da conta Linux.

1. Relacionar modo usuário a espaços virtuais protegidos.
2. Relacionar modo kernel a instruções e mapeamentos privilegiados.
3. Tratar chamadas, exceções e interrupções como entradas controladas.
4. Separar autorização do UID 0 de execução em ring 0.
5. Ver modos de privilégio como uma camada da segurança.
