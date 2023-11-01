yacc -d calc.y
lex calc.l
cc lex.yy.c y.tab.c -ll -lm
./a.out 5+6