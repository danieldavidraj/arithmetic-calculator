%{
    #include<stdio.h>
    #include<math.h>
    #include<stdlib.h>

    void yyerror(char *);
    int yylex(void);

    extern double eval(char* input);

    int factorial(int n) {
        if (n < 0) {
            fprintf(stderr, "Error: Factorial is not defined for negative numbers\n");
            exit(1);
        }
        if (n == 0 || n == 1)
            return 1;
        return n * factorial(n - 1);
    }
%}

%union { double p;}
%token<p>num
%token SIN COS TAN LOG SQRT SINH COSH TANH ACOS ASIN ATAN POW BIN_DEC DEC_BIN FACT

/*Defining the Precedence and Associativity*/
%left '+''-'                   //lowest precedence
%left '*''/'                    //highest precedenc
%nonassoc uminu                 //no associativity
%type<p>exp                     //Sets the type for non - terminal

%%

/* for storing the answer */
ss: exp {printf("Answer = %g\n",$1);}

/* for binary arithmatic operators */
exp :  exp'+'exp      { $$=$1+$3; }
       | exp'-'exp    { $$=$1-$3; }
       | exp'*'exp    { $$=$1*$3; }
       | exp'/'exp    {
            if($3==0)
            {
                printf("Divide By Zero");
                exit(0);
            }
            else $$=$1/$3;
        }
        | '-'exp             {$$=-$2;}
        | SIN'('exp')'       {$$=sin($3);}
        | COS'('exp')'       {$$=cos($3);}
        | TAN'('exp')'       {$$=tan($3);}
        | LOG'('exp')'       {$$=log($3);}
        | SQRT'('exp')'      {$$=sqrt($3);}
        | SINH'('exp')'      {$$=sinh($3);}
        | COSH'('exp')'      {$$=cosh($3);}
        | TANH'('exp')'      {$$=tanh($3);}
        | ASIN '(' exp')'    {$$ = asin($3); }
        | ACOS '(' exp')'    {$$ = acos($3); }
        | ATAN '(' exp')'    {$$ = atan($3); }
        | POW '(' exp ',' exp ')' { $$ = pow($3, $5); }
        | BIN_DEC '(' exp ')'{
            int n = $3;
            int dec = 0, i = 0, rem;
            while (n != 0) {
                rem = n % 10;
                n /= 10;
                dec += rem * pow(2, i);
                i++;
            }
            $$ = dec;
        }
        | DEC_BIN '(' exp ')'  {
            int n = $3;
            int binary = 0, base = 1, rem;
            while (n > 0) {
                rem = n % 2;
                binary += rem * base;
                n /= 2;
                base *= 10;
            }
            $$ = binary;
        }
        | FACT '(' exp')'  { $$ = factorial($3); }
        | '('exp')'        {$$=$2;}
        | num;
%%

/* extern FILE *yyin; */
int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <expression>\n", argv[0]);
        return 1;
    }

    double result = eval(argv[1]);
    //printf("Answer = %g\n", result);

    return 0;
}

void yyerror(s)

char *s;

{
    printf("ERROR");
}

double eval(char* input) {
    // Pass the expression to yylex
    yy_scan_string(input);

    int success = yyparse();

    if (success == 0) {
        return yylval.p;
    } else {
        fprintf(stderr, "Error evaluating expression.\n");
        return 0.0;
    }
}