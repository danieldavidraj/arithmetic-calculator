%{
#include <stdio.h>
%}

%token NUMBER

%%
program: /* empty */
    | program line '\n' { printf("= %d\n", $2); }
    ;

line: expr { $$ = $1; }
    ;

expr: expr '+' term { $$ = $1 + $3; }
    | expr '-' term { $$ = $1 - $3; }
    | term { $$ = $1; }
    ;

term: term '*' factor { $$ = $1 * $3; }
    | term '/' factor { if ($3 == 0) { yyerror("Division by zero"); } else { $$ = $1 / $3; } }
    | factor { $$ = $1; }
    ;

factor: NUMBER { $$ = $1; }
    | '(' expr ')' { $$ = $2; }
    ;

%%

void yyerror(const char* msg) {
    fprintf(stderr, "%s\n", msg);
}

int main() {
    yyparse();
    return 0;
}
