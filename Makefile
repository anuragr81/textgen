

all:
	flex lex_input.c
	yacc -d yacc_input.c
	cc -o test lex.yy.c y.tab.c 
