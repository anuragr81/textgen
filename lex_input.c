
%{
    #include "y.tab.h"
    void yyerror(char *);
%}

%%

is { return VERB_IS_PRES;}
were { return VERB_IS_PAST; }
do { return VERB_DO_SINGLE_PRES;}
did { return VERB_DO_SINGLE_PAST;}

where|Where { return WHERE;}
[A-Za-z]+       { yylval.sValue=(char*)malloc(sizeof(char)*strlen(yytext)); strcpy(yylval.sValue,yytext); return NAME; }

\(          { return BRACKET_OPEN; }
\)          { return BRACKET_CLOSE; }

[\,]        { return COMMA; }
[ \t]       { return BLANK; }       /* skip whitespace */
[\.]        { return STOP; }

[\;]       { return SEMICOLON; }

.           yyerror("Unknown character");

%%

int yywrap(void) {
    return  1 ;
}

