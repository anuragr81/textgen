

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
%type<sValue> atom
%type<sValue> userdef


%token ATOMS
%token WHAT

%token AND
%token OR
%token NOT
%token ADD
%token SUB
%token MULT
%token DIV
%token EQUALS
%token COLON
%token COMMA
%token CURLYBRACES_OPEN
%token CURLYBRACES_CLOSED

%token RES
%nonassoc RES
%token LT
%nonassoc LT
%token GT


// %type<pVerb> verb

// SAMPLE:
// verb: blank s_verb { $$ = $2;} | s_verb blank { $$ = $1; } | s_verb { $$ = $1;} | blank s_verb blank { $$ = $2;}

%%

statement : definition | atoms | result | question

result: atom RES atom  { printf("atom:%s results in atom:%s",$1,$3); } | userdef RES userdef { printf("%s results in %s",$1,$3); } | userdef RES atom { printf("%s results in %s",$1,$3); } | atom RES userdef { printf("%s results in %s",$1,$3); }

question: userdef RES WHAT {printf("what does %s lead to",$1); } | atom RES WHAT {printf("what does atom:%s lead to",$1);}  // question creates conflicts in the syntax

userdef :  CURLYBRACES_OPEN NAME CURLYBRACES_CLOSED { $$=$2;}

definition: 
//userdef COLON condition { printf("<!--definition -->");}   |
  userdef : result {} 

//condition: NAME LT NAME

atom : NAME { $$=$1;}

atoms: ATOMS CURLYBRACES_OPEN atoms_list CURLYBRACES_CLOSED
atoms_list : atoms_list COMMA atom {printf ("\"%s\"",$3);} | atom { printf("\"%s\"",$1);}

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
        printf("<!--Input: \"%s\"-->\n",argv[1]);
    }
    yy_scan_string(argv[1]);
    yyparse();
    printf("\n</xml>");
    return 0;
}
#endif
