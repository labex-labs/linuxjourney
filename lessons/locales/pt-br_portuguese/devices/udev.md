# udev

## Conteúdo da lição

Nos velhos tempos e, na verdade, até hoje, se você realmente quisesse, criaria nós de dispositivo usando um comando como:

<pre> $ mknod / dev / sdb1 b 8 3 </ pre>

Este comando fará um nó de dispositivo / dev / sdb1 e fará dele um dispositivo de bloco (b) com um número maior de 8 e um número menor de 3.

Para remover um dispositivo, você simplesmente faria <b> rm </ b> no arquivo do dispositivo no diretório / dev.

Felizmente, nós realmente não precisamos mais fazer isso por causa do udev. O sistema udev cria e remove arquivos de dispositivos dinamicamente para nós, independente de estarem ou não conectados. Existe um daemon udevd que está sendo executado no sistema e ele ouve mensagens do kernel sobre dispositivos conectados ao sistema. O Udevd analisará essas informações e corresponderá os dados com as regras especificadas em /etc/udev/rules.d, dependendo dessas regras, será mais provável criar nós de dispositivos e links simbólicos para os dispositivos. Você pode escrever suas próprias regras do udev, mas isso é um pouco fora do escopo desta lição. Felizmente, o seu sistema já vem com muitas regras do udev, então você pode nunca precisar escrever o seu próprio.

Você também pode ver o banco de dados e sysfs do udev usando o comando <b> udevadm </ b>. Esta ferramenta é muito útil, mas às vezes pode ficar muito complicada, um simples comando para visualizar informações para um dispositivo seria:

<pre> $ udevadm info --query = all --name = / dev / sda </ pre>

## Exercício

Execute o comando udevadm fornecido e confira a entrada.

## Questionário

O que dinamicamente adiciona e remove dispositivos?

## Resposta do questionário

udev