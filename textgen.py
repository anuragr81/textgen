import sys
from pyparsing import Word,alphas,OneOrMore

kt = {}

def updateKT(s,location,tokens):
        print "location=",location, "s=",s, "tokens=",tokens
	kt[tokens[0]]=tokens[2:]

def print_rvalue(s,l,t):
    print "rvalue - t=",t

"""
relations of a context's attribute are of types : [ property, supertype/subtype, composition/aggregation, containment/ownership ]
"""
def template_tree (contexts):
	templateTree = {contexts['company']: {'relation':'property', 'nodes':[contexts['company']['name'] ]},
	              }

"""
generates the english text from the tree
"""
def document_from_template(templateTree):
	return parseString(templateTree) # this would generate the english text


# define grammar
variable = Word(alphas) | Word(alphas)+ "::"+ Word(alphas)
freeformText = "freeform"+"("+ OneOrMore(Word(alphas))+")"
rvalue = freeformText | Word(alphas)
grammar= variable + "::" + Word(alphas) + "=" + rvalue | variable + "=" + rvalue
grammar.setParseAction(updateKT)
rvalue.setParseAction(print_rvalue)


if __name__ == "__main__":
    # input string
    inputString = sys.argv[1]
    
    # parse input string
    print inputString, "->", grammar.parseString( inputString )
    print "KT=",kt
else:
    print "__name__=",__name__
    
    
    
    
### Grammar for knowledge tree - how would a knowledge bank look like
# Every command is that of a context - there are predefined contexts for now
# "#start-context Company" (Company predefined contexts)
# Company::name = "Herodotus Publishing"
# Company::stock = "HRP"
# Company::prices = {date(2012,11,1):10, date(2012,11,12):10,}


#Document template
