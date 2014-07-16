
%{
    #include "y.tab.h"
    void yyerror(char *);
%}

%%

\-\> { return RES ; }
\= { return EQUALS ; } 
\< { return LT ;}
\> { return GT ;}

OR { return OR;}
AND { return AND;}
NOT { return NOT;}


[A-Za-z_]+       { yylval.sValue=(char*)malloc(sizeof(char)*strlen(yytext)); strcpy(yylval.sValue,yytext); return NAME; }

.           yyerror("Unknown character");

%%

int yywrap(void) {
    return  1 ;
}

