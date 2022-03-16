# compilador

![git status](http://3.129.230.99/svg/MarceloCMiguel/compilador)

## Diagrama sintático 

![alt_text](images/diagrama.png)

## EBNF

EXPRESSION = TERM, { ("+" | "-"), TERM } ;

TERM = FACTOR, { ("*" | "/"), FACTOR } ;

FACTOR = ("+" | "-") FACTOR | "(" EXPRESSION ")" | number ;