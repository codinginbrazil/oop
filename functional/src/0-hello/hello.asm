section .data
msg db "Hello World!",0x0a
len equ $-msg
section .text
global _start
; string "Hello world!"
; calcula o tamanho da string msg
; início da seção de texto
; onde deve começar a execução (assim como a main da ling. C)
_start:
; write
mov ebx, 1
mov ecx, msg
mov edx, len
mov eax, 4
int 0x80
; label start - a execução começa nesse ponto
; arquivo de saída - stdin
; apontador para o buffer
; tamanho do buffer
; chamada write ao sistema
; chamada de sistema para o kernel
; exit
mov eax, 1
 ; move o valor 1 para o registo eax
mov ebx, 0
 ; move o valor 0 para o registo ebx
int 0x80
 ; chamada de sistema para o kernel