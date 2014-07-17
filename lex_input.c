
%{
    #include "y.tab.h"
    void yyerror(char *);
%}

%%

\-\> { return RES ; }
\= { return EQUALS ; } 
\< { return LT ;}
\> { return GT ;}
\: { return COLON;} 
\, { return COMMA;} 
\? {return WHAT;}
atoms { return ATOMS;} 

sub { return SUB;}
add { return ADD;}
mult { return MULT;}
div { return DIV;} 

OR { return OR;}
AND { return AND;}
NOT { return NOT;}

\{ { return CURLYBRACES_OPEN; }
\} { return CURLYBRACES_CLOSED; }


[A-Za-z_]+       { yylval.sValue=(char*)malloc(sizeof(char)*strlen(yytext)); strcpy(yylval.sValue,yytext); return NAME; }


%%

//.           yyerror("Unknown character");

int yywrap(void) {
    return  1 ;
}

