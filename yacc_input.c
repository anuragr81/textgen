

%{
#include <stdio.h>
#include "structures.h"

void processAssignment(char * subject, struct TVerb * tverb , char* object){
}

struct Message {
 char * input, * output;
};
    int yylex(void);
    void yyerror(char *);


%}

%union
{
    int iValue;
    char * sValue;
    struct Entity * pEntity;
    struct TVerb * pVerb;
};

%token INTEGER
%token<sValue> NAME
%type<sValue> subject
%type<sValue> object

%token AND
%token OR
%token NOT
%token ADD
%token SUB
%token MULT
%token DIV
%token EQUALS

%token RES
%token LT
%token GT


// %type<pVerb> verb

// SAMPLE:
// verb: blank s_verb { $$ = $2;} | s_verb blank { $$ = $1; } | s_verb { $$ = $1;} | blank s_verb blank { $$ = $2;}

%%

subject: NAME { $$ = $1; }
object : NAME { $$ = $1; }


%%

// TODO: -- Active vs Passive voice

void yyerror(char *s)
{
    fprintf(stderr, "%s\n", s);
}

#ifdef __BUILD_LIB__
void parseString(struct Message * m){
yy_scan_string(m->input);
printf("\n<xml>");
printf("<!--Input: %s-->\n",m->input);
yyparse();
printf("\n</xml>");
strcpy(m->output,output);
}
#else
int main(int argc,char * argv[])
{
    if (argc < 2)
    {
        printf("Usage: %s <input-string>",argv[1]);
        return 1;
    }
    else
    {
        printf("\n<xml>");
        printf("<!--Input: %s-->\n",argv[1]);
    }
    yy_scan_string(argv[1]);
    yyparse();
    printf("\n</xml>");
    return 0;
}
#endif
