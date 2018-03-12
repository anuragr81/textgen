import sys
import logging

loglevel=logging.DEBUG
LOGGER_NAME="parser"

FORMAT='%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT);
logger = logging.getLogger(LOGGER_NAME);
logger.setLevel(loglevel)

from pyparsing import Word,alphas,OneOrMore,Optional

kt = {'contexts':{},'globals':{}}

def print_single_line(s,l,t):
    logger.debug("print_single_line-"+str(t))
    kt['globals'][t[0]]=t[2]

def start_context(s,l,t):
    logger.debug("start-context: "+str(t))
    kt ['contexts'][t[1]]={'attributes':{}}

def update_variable(s,l,t):
    logger.debug("update_variable - t="+str(t))


def update_attribute(s,l,t):
    logger.debug("update_attribute - "+str(t) +" kt="+str(kt))
    kt['contexts'][t[0]]['attributes'][t[2]]=t[4]

def updateKT(s,location,tokens):
    logger.debug("location="+str(location)+ " s=\""+str(s)+" tokens="+str(tokens))

def print_rvalue(s,l,t):
    logger.debug("rvalue - t="+str(t))

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

line                  = startContext + ";" | setVariableValue + ";" | setAttributeValue + ";"
grammar               = OneOrMore(line)



setAttributeValue.setParseAction(update_attribute)
setVariableValue.setParseAction(update_variable)
line.setParseAction(print_single_line)
startContext.setParseAction(start_context)
#grammar.setParseAction(updateKT)
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
