
; constantes
SYS_EXIT equ 1
SYS_READ equ 3
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1
True equ 1
False equ 0

segment .data

segment .bss  ; variaveis
  res RESB 1

section .text
  global _start

print:  ; subrotina print

  PUSH EBP ; guarda o base pointer
  MOV EBP, ESP ; estabelece um novo base pointer

  MOV EAX, [EBP+8] ; 1 argumento antes do RET e EBP
  XOR ESI, ESI

print_dec: ; empilha todos os digitos
  MOV EDX, 0
  MOV EBX, 0x000A
  DIV EBX
  ADD EDX, '0'
  PUSH EDX
  INC ESI ; contador de digitos
  CMP EAX, 0
  JZ print_next ; quando acabar pula
  JMP print_dec

print_next:
  CMP ESI, 0
  JZ print_exit ; quando acabar de imprimir
  DEC ESI

  MOV EAX, SYS_WRITE
  MOV EBX, STDOUT

  POP ECX
  MOV [res], ECX
  MOV ECX, res

  MOV EDX, 1
  INT 0x80
  JMP print_next

print_exit:
  POP EBP
  RET

; subrotinas if/while
binop_je:
  JE binop_true
  JMP binop_false

binop_jg:
  JG binop_true
  JMP binop_false

binop_jl:
  JL binop_true
  JMP binop_false

binop_false:
  MOV EBX, False
  JMP binop_exit
binop_true:
  MOV EBX, True
binop_exit:
  RET

_start:

  PUSH EBP ; guarda o base pointer
  MOV EBP, ESP ; estabelece um novo base pointer

  ; codigo gerado pelo compilador 

PUSH DWORD 0 ;
MOV EBX, 2 ; EVALUATE DO INTVAL
MOV [EBP-4], EBX ; resultado da atribuição
IF_1:
MOV EBX, [EBP-4] ;
PUSH EBX ;
MOV EBX, 2 ; EVALUATE DO INTVAL
POP EAX ;
CMP EAX, EBX ;
CALL binop_je ;
CMP EBX, False ;
JE ELSE_1
MOV EBX, [EBP-4] ;
PUSH EBX ; Empilhe os argumentos
CALL print ; Chamada da função
POP EBX ; Desempilhe os argumentos
JMP EXIT_1
ELSE_1:
MOV EBX, 2 ; EVALUATE DO INTVAL
MOV [EBP-4], EBX ; resultado da atribuição
EXIT_1:
; interrupcao por saida
POP EBP
MOV EAX, 1
INT 0x80
