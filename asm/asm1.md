# Язык ассемблера

## О чем говорили

- Язык ассемблера 
- В языке ассемблера ограниченное количество переменных (регистров)
- Размеры операндов могут быть:
	- BYTE - 1 байт,
	- WORD - 2 байта,
	- DWORD - 4 байта, 
	- QWORD - 8 байт
- Инструкции mov, lea
- Инструкции арифметических оппераций (xor, add, sub, mul, div)
- Инструкции сравнения и условных/безусловных переходов (cmp, je, jne, jg, jge, jl, jle, jmp)

## Что почитать

`0`. [Лекции](http://isc.tsu.ru/lectures/asm/)  по ассемблеру

`1`. [Справочник](http://isc.tsu.ru/lectures/asm/instructions.html) основных инструкций ассемблера на русском!

## Что порешать

`0`.  <details><summary> Задание 0</summary>

```assembly
    mov eax, 81
    mov ebx, 49
    div 10
    add ebx, edx
    mul ebx
    sub eax, 17

    eax == ?
```
</details>

`1`.  <details><summary> Задание 1</summary>

```assembly
	mov [0xAABBCC10], 6
	mov [0xAABBCC08], 1
	mov [0xAABBCC04], 1

	.loop:
		mov eax, [0xAABBCC08]
		add eax, [0xAABBCC04]
		mov ebx, [0xAABBCC08]
		mov [0xAABBCC04], ebx
		mov [0xAABBCC08], eax
		sub [0xAABBCC10], 1
		cmp [0xAABBCC10], 0
		jg .loop
	
	[0xAABBCC08] == ?
```
</details>

`2`.* <details><summary> Задание 2</summary>

```assembly
	_start:
		mov [0x1337], 0x62
		mov [0x1338], 0x65
		mov [0x1339], 0xe7
		mov [0x133a], 0x5f
		mov [0x133b], 0x48
		mov [0x133c], 0x61
		mov [0x133d], 0xe7
		mov [0x133e], 0x56
		mov [0x133f], 0xd3
		mov [0x1340], 0x4e
		mov [0x1341], 0x76
		mov [0x1342], 0xd9
		mov [0x1343], 0x5d
		mov edx, 13
		mov ebx, 0x1337
		xor eax, eax
		xor ecx, ecx
		jmp .C
		
	.A:
		add al, 0x16
		xor al, 0x1
		mov [edi], al
		jmp .next
		
	.B:
		add al, 0x11
		and al, 0x7f
		sub al, 0x5
		mov [edi], al
		jmp .next
		
	.C:
		cmp ecx, edx
		je .Done
		lea edi, [ebx + ecx]
		mov al, BYTE [edi]
		cmp al, 0x8e
		jge .B
		cmp al, 0x5f
		jle .A
		mov [edi], al
	.next:
		inc ecx
		jmp .C
	
	.Done:
	
	Что за строка теперь лежит в [0x1337-0x1343]?
```
</details>
