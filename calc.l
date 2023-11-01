%{
    #include<math.h>
    #include"y.tab.h"
%}


%%
[0-9]+|[0-9]*\.[0-9]+   {yylval.p = atof(yytext); return num;}

sin return SIN;
cos return COS;
tan return TAN;
log return LOG;
sqrt return SQRT;
sinh return SINH;
cosh return COSH;
tanh return TANH;
asin return ASIN;
acos return ACOS;
atan return ATAN;
pow return POW;
bin_dec return BIN_DEC;
dec_bin return DEC_BIN;
fact return FACT;
[\t];
\n return 0;
. return yytext[0];
%%

int yywrap(void) {
    return 1;
}