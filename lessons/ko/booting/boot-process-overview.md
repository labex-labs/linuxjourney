---
lang: "ko"
title: "부팅 프로세스 개요"
meta_description: "Linux 부팅 프로세스 단계: BIOS, bootloader, kernel, init 을 학습합니다. 전원 켜기부터 로그인까지 Linux 가 어떻게 시작되는지 이해합니다. 필수 Linux 초보자 가이드."
meta_keywords: "Linux 부팅 프로세스, BIOS, bootloader, kernel, init, Linux 튜토리얼, Linux 가이드, 초보자"
---

## Lesson Content

이제 Linux 의 몇 가지 중요한 구성 요소에 대해 꽤 잘 이해했으니, 시스템이 어떻게 부팅되는지 학습하여 이 모든 것을 하나로 묶어봅시다. 컴퓨터를 켜면 로고 화면이 표시되고, 여러 메시지가 실행된 다음, 마지막에는 로그인 창이 나타나는 멋진 일들이 일어납니다. 사실 전원 버튼을 누르는 순간부터 로그인할 때까지 수많은 일들이 일어나며, 이 과정에서 우리는 그것들을 논의할 것입니다.

Linux 부팅 프로세스는 4 가지 간단한 단계로 나눌 수 있습니다:

### 1. BIOS

BIOS("Basic Input/Output System"의 약자) 는 하드웨어를 초기화하고 POST(Power-on Self-Test) 를 통해 모든 하드웨어가 준비되었는지 확인합니다. BIOS 의 주요 임무는 bootloader 를 로드하는 것입니다.

### 2. Bootloader

bootloader 는 kernel 을 메모리로 로드한 다음 일련의 kernel 매개변수와 함께 kernel 을 시작합니다. 가장 일반적인 bootloader 중 하나는 GRUB 이며, 이는 보편적인 Linux 표준입니다.

### 3. Kernel

kernel 이 로드되면 즉시 장치와 메모리를 초기화합니다. kernel 의 주요 임무는 init 프로세스를 로드하는 것입니다.

### 4. Init

init 프로세스는 시작되는 첫 번째 프로세스라는 것을 기억하십시오. Init 은 시스템에서 필수 서비스 프로세스를 시작하고 중지합니다. Linux 배포판에는 init 의 세 가지 주요 구현이 있습니다. 우리는 그것들을 간략하게 살펴보고 다른 과정에서 더 자세히 다룰 것입니다.

이것이 Linux 부팅 프로세스에 대한 (매우) 간단한 설명입니다. 다음 강의에서 이러한 단계에 대해 더 자세히 설명할 것입니다.

## Exercise

시스템을 재부팅하고 컴퓨터가 부팅될 때 각 단계를 찾을 수 있는지 확인하십시오.

## Quiz Question

Linux 부팅 프로세스의 마지막 단계는 무엇입니까?

## Quiz Answer

init
