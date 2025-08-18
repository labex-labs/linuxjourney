---
lang: "ko"
title: "권한 수정"
meta_description: "Linux 에서 chmod 명령어를 사용하여 파일 권한을 수정하는 방법을 배웁니다. 안전한 파일 관리를 위한 심볼릭 및 숫자 모드를 이해합니다. 지금 학습을 시작하세요!"
meta_keywords: "chmod 명령어, Linux 권한, 파일 권한, chmod 튜토리얼, Linux 보안, 초보자 Linux, Linux 가이드, chmod 숫자"
---

## Lesson Content

권한 변경은 `chmod` 명령어를 사용하여 쉽게 할 수 있습니다.

먼저, 변경하려는 권한 세트 (user, group, 또는 other) 를 선택합니다. `+` 또는 `-`를 사용하여 권한을 추가하거나 제거할 수 있습니다. 몇 가지 예시를 살펴보겠습니다.

### Adding permission bit on a file

```bash
chmod u+x myfile
```

위 명령어는 다음과 같이 해석됩니다: `myfile`에 대한 권한을 변경하는데, user 세트에 실행 권한 비트를 추가합니다. 이제 사용자는 이 파일에 대한 실행 권한을 갖게 됩니다!

### Removing permission bit on a file

```bash
chmod u-x myfile
```

### Adding multiple permission bits on a file

```bash
chmod ug+w
```

숫자 형식을 사용하여 권한을 변경하는 또 다른 방법이 있습니다. 이 방법을 사용하면 권한을 한 번에 모두 변경할 수 있습니다. 권한을 나타내기 위해 r, w, 또는 x 를 사용하는 대신, 단일 권한 세트에 대한 숫자 표현을 사용합니다. 따라서 `g`로 그룹을 지정하거나 `u`로 사용자를 지정할 필요가 없습니다.

숫자 표현은 다음과 같습니다:

- 4: read permission
- 2: write permission
- 1: execute permission

예시를 살펴보겠습니다:

```bash
chmod 755 myfile
```

이 파일에 어떤 권한을 부여하는지 짐작할 수 있나요? 분석해 봅시다: `755`는 모든 세트에 대한 권한을 포함합니다. 첫 번째 숫자 (7) 는 user 권한을 나타내고, 두 번째 숫자 (5) 는 group 권한을 나타내며, 마지막 5 는 other 권한을 나타냅니다.

잠깐, 7 과 5 는 위에 나열되지 않았습니다. 이 숫자들이 어디서 나온 걸까요? 이제 모든 권한을 하나의 숫자로 결합하고 있다는 것을 기억하세요. 따라서 약간의 계산이 필요합니다.

7 = 4 + 2 + 1 이므로, 7 은 user 권한이며, 읽기, 쓰기, 실행 권한을 가집니다.

5 = 4 + 1, group 은 읽기 및 실행 권한을 가집니다.

5 = 4 + 1, 그리고 모든 other 사용자는 읽기 및 실행 권한을 가집니다.

한 가지 유의할 점: 무작정 권한을 변경하는 것은 좋지 않습니다. 민감한 파일을 모든 사람이 수정할 수 있도록 노출시킬 수 있습니다. 그러나 많은 경우 합법적으로 권한을 변경해야 할 때가 있습니다. `chmod` 명령어를 사용할 때는 주의를 기울이세요.

## Exercise

일부 기본 텍스트 파일 권한을 변경하고 `ls -l`을 실행할 때 비트가 변경되는 것을 확인하세요.

## Quiz Question

숫자 형식을 사용할 때 읽기 권한을 나타내는 숫자는 무엇입니까?

## Quiz Answer

4
