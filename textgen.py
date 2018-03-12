import sys
from pyparsing import Word,alphas,OneOrMore,Optional

kt = {}

def print_single_line(s,l,t):
    print "print_single_line-",t

def start_context(s,l,t):
    print "start-context: ",t
    kt ['context'] ={'name': t[1],'attributes':{} }

def update_attribute(s,l,t):
    print "update_attribute - ", t
    kt['context'][t[0]]['attributes'][t[2]]=t[4]

def updateKT(s,location,tokens):
        print "location=",location, "s=",s, "tokens=",tokens

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
startContext          = "start_context" + Word(alphas)
variable              = Word(alphas) | Word(alphas)+ "::"+ Word(alphas)
freeformText          = "freeform"+"("+ OneOrMore(Word(alphas))+")"
rvalue                = freeformText | Word(alphas)
setAttributeValue     = variable + "::" + Word(alphas) + '=' + rvalue 
setVariableValue      = variable + '=' + rvalue

singleline            = startContext | setAttributeValue | setVariableValue
grammar               = singleline  + ";" + Optional(singleline)

setAttributeValue.setParseAction(update_attribute)
singleline.setParseAction(print_single_line)
startContext.setParseAction(start_context)
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
