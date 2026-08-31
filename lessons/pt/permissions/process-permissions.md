---
lesson_id: "process-permissions"
course_id: "permissions"
lang: "pt"
order_index: 7
title: "Permissões de Processos"
description: "Aprenda como IDs de usuário reais, efetivos e salvos ajudam os processos Linux a identificar solicitantes e gerenciar privilégios."
meta_title: "Permissões de Processos - Permissões"
meta_description: "Aprenda sobre as permissões de processos Linux, incluindo IDs de usuário real, efetivo e salvo. Entenda como os UIDs afetam a segurança e a execução de comandos."
meta_keywords: "permissões de processos Linux, UID real, UID efetivo, UID salvo, segurança Linux, comando passwd, tutorial Linux, Linux para iniciantes"
---

As verificações de autorização do Linux atuam sobre as credenciais dos processos, não diretamente sobre um nome de usuário digitado. Um processo possui vários IDs de usuário e grupo relacionados, cada um com uma função diferente. A maioria dos programas comuns começa com identidades correspondentes, enquanto programas privilegiados podem usar valores distintos deliberadamente.

## ID de Usuário Real

O ID de usuário real identifica a conta que iniciou o processo ou sua sessão de login ancestral. Os programas podem consultá-lo para diferenciar o solicitante de uma identidade efetiva elevada.

Para um comando comum iniciado pelo usuário Bob, o ID de usuário real normalmente corresponde ao UID de Bob. Criar outro processo não cria uma nova conta nem altera essa identidade por si só.

:::single-choice{#process-permissions-real-uid}
O que o ID de usuário real de um processo normalmente identifica?

::option[O proprietário do arquivo aberto mais recentemente.]{#process-permissions-real-opened-file explanation="Abrir um arquivo não substitui o UID real do processo pelo proprietário desse arquivo."}
::option[A conta associada ao solicitante original do processo.]{#process-permissions-real-caller .correct explanation="O UID real registra a identidade do usuário solicitante herdada quando o processo é iniciado."}
::option[O grupo selecionado para todas as verificações de acesso.]{#process-permissions-real-group explanation="Um UID é uma identidade de usuário; as verificações de grupo usam credenciais de grupo separadas."}
:::

## ID de Usuário Efetivo

O ID de usuário efetivo é a credencial de usuário utilizada em muitas verificações de sistema de arquivos e privilégios. Normalmente, ele corresponde ao UID real. A execução de um programa setuid respeitado pode, em vez disso, inicializá-lo a partir do proprietário do executável.

Por exemplo, um utilitário de senhas cuidadosamente desenvolvido pode ser executado com um UID efetivo elevado para atualizar dados de autenticação protegidos. O programa ainda deve aplicar a política com base no solicitante, na conta requisitada, nos resultados do PAM e em outros contextos. Possuir um UID efetivo não torna automaticamente legítimas todas as operações solicitadas.

:::single-choice{#process-permissions-effective-uid}
Qual ID de usuário é usado em muitas decisões de controle de acesso realizadas em nome de um processo?

::option[O ID de usuário efetivo.]{#process-permissions-effective-active .correct explanation="O UID efetivo é a credencial de usuário ativa consultada em muitas verificações de autorização."}
::option[Somente o ID de usuário salvo.]{#process-permissions-effective-saved-only explanation="O ID salvo oferece suporte a transições de credenciais, mas geralmente não é a identidade ativa nas verificações de acesso."}
::option[O UID armazenado no diretório atual.]{#process-permissions-effective-directory explanation="A propriedade do sistema de arquivos é um metadado do objeto, não a credencial de usuário ativa do processo."}
:::

## ID Set-User-ID Salvo

O ID set-user-ID salvo permite que um programa mantenha uma identidade que poderá restaurar posteriormente, sujeito às regras das chamadas de sistema. Um programa privilegiado pode trocar temporariamente seu UID efetivo por um valor menos privilegiado, realizar um trabalho comum com autoridade reduzida e restaurar a identidade salva somente para uma operação de escopo restrito.

Isso é mais seguro do que manter autoridade elevada durante todo o programa, mas apenas quando implementado corretamente. Os programas devem descartar os privilégios permanentemente quando eles deixarem de ser necessários e verificar se cada chamada de alteração de credenciais falhou.

:::single-choice{#process-permissions-saved-uid}
Por que um programa privilegiado pode manter um ID set-user-ID salvo?

::option[Para alternar sua identidade efetiva entre fases privilegiadas e não privilegiadas controladas.]{#process-permissions-saved-switch .correct explanation="A identidade salva pode permitir uma redução temporária de privilégios e sua restauração posterior quando permitida."}
::option[Para atribuir automaticamente esse UID a todos os arquivos que ele ler.]{#process-permissions-saved-file-owner explanation="Ler um arquivo não altera sua propriedade para o UID salvo do processo."}
::option[Para substituir o banco de dados de contas do sistema para o processo.]{#process-permissions-saved-database explanation="As credenciais do processo não substituem os registros de contas nem os dados dos serviços de nomes."}
:::

## IDs de Usuário São Apenas Parte do Conjunto de Credenciais

Os processos também possuem credenciais de grupo reais, efetivas, salvas e suplementares. IDs do sistema de arquivos, capacidades, namespaces, módulos de segurança, ACLs, opções de montagem e políticas de serviços podem afetar ainda mais a autorização. Portanto, “o UID permite” muitas vezes é apenas parte de uma explicação completa.

Use ferramentas como `ps` e `/proc/PROCESS/status` para inspecionar credenciais no Linux. A disponibilidade dos campos e os formatos de exibição variam, portanto consulte a documentação local e evite alterar credenciais apenas para fazer experiências em um sistema compartilhado.

:::single-choice{#process-permissions-ordinary-identities}
Na maioria dos comandos comuns sem uma transição de privilégios, como os UIDs real e efetivo se comparam?

::option[O UID efetivo é sempre zero.]{#process-permissions-effective-root explanation="Comandos comuns não recebem automaticamente o UID do root."}
::option[O UID real sempre corresponde ao proprietário do arquivo executável.]{#process-permissions-real-file-owner explanation="O proprietário do executável afeta o comportamento setuid, não o UID real comum."}
::option[Eles normalmente correspondem ao UID do usuário solicitante.]{#process-permissions-uids-match .correct explanation="Sem setuid ou uma alteração explícita de credenciais, processos comuns geralmente são executados com identidades real e efetiva correspondentes."}
:::

## Resumo

Agora você sabe explicar por que um processo Linux pode manter várias identidades de usuário.

1. Use o UID real para identificar o solicitante original.
2. Relacione o UID efetivo às verificações de autorização ativas.
3. Use a identidade salva para compreender transições controladas de privilégios.
4. Considere os IDs de grupo e os mecanismos de segurança adicionais como parte da decisão completa.
