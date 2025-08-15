# sysfs

## Conteúdo da lição

O Sysfs foi criado há muito tempo para gerenciar melhor os dispositivos em nosso sistema que o diretório / dev não conseguiu fazer. O Sysfs é um sistema de arquivos virtual, geralmente montado no diretório / sys. Isso nos fornece informações mais detalhadas do que poderíamos ver no diretório / dev. Ambos os diretórios / sys e / dev parecem ser muito semelhantes e são em alguns aspectos, mas eles têm grandes diferenças. Basicamente, o diretório / dev é simples, ele permite que outros programas acessem os próprios dispositivos, enquanto o sistema de arquivos / sys é usado para visualizar informações e gerenciar o dispositivo.

O sistema de arquivos / sys contém basicamente todas as informações de todos os dispositivos do sistema, como o fabricante e o modelo, onde o dispositivo está conectado, o estado do dispositivo, a hierarquia dos dispositivos e muito mais. Os arquivos que você vê aqui não são nós de dispositivos, portanto, você não interage de fato com dispositivos do diretório / sys, em vez disso, está gerenciando dispositivos.

Dê uma olhada no conteúdo do diretório / sys:

<pre>
pete @ icebox: ~ $ ls / sys / block / sda
alignment_offset discard_alignment detentores de rastreamento sda6 removível
bdi events em voo ro size uevent
capacidade events_async power sda1 slaves
dev status da fila de eventos_poll_msecs sda2
subsistema sda5 do intervalo ext_range do dispositivo
</ pre>


## Exercício

Confira o conteúdo do diretório / sys e veja quais arquivos estão localizados lá.

## Questionário

Qual diretório é usado para visualizar informações detalhadas sobre dispositivos?

## Resposta do questionário

/ sys