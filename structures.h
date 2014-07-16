#ifndef STRUCTURES_H_INCLUDED
#define STRUCTURES_H_INCLUDED

#include <stdlib.h>
#include <string.h>

#define DECLARE_ALLOC_STRUCT(STRUCT,PTR) struct STRUCT * PTR = (struct STRUCT*) malloc(sizeof(struct STRUCT));
#define ALLOC_ARRAY(TYPE,ARRNAME,LEN) ARRNAME = (TYPE*) malloc(sizeof(TYPE)*LEN);

typedef enum { PAST=-1,PRESENT=0,FUTURE=1} TENSE;

struct TVerb
{
    char * name;
    TENSE tense;
};

struct TVerb* createVerb(char * str, TENSE tense)
{
    DECLARE_ALLOC_STRUCT(TVerb,ptr);
    size_t sz = strlen(str);
    ALLOC_ARRAY(char,ptr->name,sz);
    strncpy(ptr->name,str,sz);
    ptr->tense = tense;
    return ptr;
}

#endif // STRUCTURES_H_INCLUDED
