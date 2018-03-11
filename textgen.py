import sys
from pyparsing import Word,alphas

kt = {}

def updateKT(tokens):
	kt[tokens[0]]=tokens[2:]

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

greet = Word( alphas ) + "=" + Word( alphas )

greet.setParseAction(updateKT)

# input string
hello = "love=false"

# parse input string
print hello, "->", greet.parseString( hello )
print "KT=",kt




### Grammar for knowledge tree - how would a knowledge bank look like
# Every command is that of a context - there are predefined contexts for now
# "#start-context Company" (Company predefined contexts)
# Company::name = "Herodotus Publishing"
# Company::stock = "HRP"
# Company::prices = {date(2012,11,1):10, date(2012,11,12):10,}


#Document template