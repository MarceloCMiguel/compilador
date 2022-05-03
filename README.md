# compilador

![git status](http://3.129.230.99/svg/MarceloCMiguel/compilador)

## Diagrama sintático 

![alt_text](images/diagrama.png)

## EBNF

BLOCK = "{", { STATEMENT }, "}" ;

STATEMENT = ( λ | ASSIGNMENT | PRINT | BLOCK | WHILE | IF), ";" ;

ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;

PRINT = "printf", "(", EXPRESSION, ")" ;

RELEXPRESSION = EXPRESSION , {("<" | ">" | "==") , EXPRESSION } ;

EXPRESSION = TERM, { ("+" | "-" | "||"), TERM } ;

TERM = FACTOR, { ("*" | "/" | "&&"), FACTOR } ;

FACTOR = NUMBER | IDENTIFIER | (("+" | "-" | "!") , FACTOR) | "(" , RELEXPRESSION , ")" | SCANF;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;

WHILE = "while", "(", RELEXPRESSION ,")", STATEMENT;

IF = "if", "(", RELEXPRESSION ,")", STATEMENT, (("else", STATEMENT) | λ );

PRINT = "printf", "(" , EXPRESSION, ")" ;

SCANF = "scanf", "(", ")" ;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;

NUMBER = DIGIT , { DIGIT } ;

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
