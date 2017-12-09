# Язык ассемблера

## О чем говорили

- В ассебмлере есть такая область памяти - стек
- В некоторых представлениях стек растет не вверх, а вниз
- `rsp` всегда указывает на последнюю `ЗАНЯТУЮ` ячейку
- push - положить значение на верхушку стека
- pop - достать значение из верхушки стека
- call / ret - инструкции вызова и возврата из функции
	- call - вызов по адресу и сохранение адреса следующей инструкции после `call` в стеке
	- ret - возврат по адресу следующей инструкции после `call` (этот адрес достается из стека)


## Что почитать

`0`. [Лекции](http://isc.tsu.ru/lectures/asm/)  по ассемблеру

`1`. [Справочник](http://isc.tsu.ru/lectures/asm/instructions.html) основных инструкций ассемблера на русском!

`2`.* [Сборник](https://www.xorpd.net/pages/xchg_rax/snip_00.html) различных интересных снипетов.

## Что порешать

<details><summary> Задание 0</summary>

```assembly
foo:
    call bar
    mov ebx, 7
    mul [esp+4]
    lea ebx, [ebx * 4]
    add eax, ebx
    ret

bar:
    mov eax, 328
    mov ecx, 3
bar.while:
    div 2
    dec ecx
    test ecx, ecx
    jnz bar.while
    ret

start:
    push 4
    call foo
    cmp eax, 200
    jg exit
    mul ebx
exit:

    eax == ?
```
</details>

<details><summary> Задание 1</summary>

    Сопоставьте эквивалентный код на ассемблере и на C. Ответ в форме: 1A2B3C

    1 - https://pastebin.com/2czncEhU
    2 - https://pastebin.com/qeK4HYXv
    3 - https://pastebin.com/nzEFVseR

    A - https://pastebin.com/LzeEpNJa
    B - https://pastebin.com/DiNEx4Y1
    C - https://pastebin.com/PMyTW1hG
	

</details>
