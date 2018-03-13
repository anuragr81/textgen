import sys
import logging

loglevel=logging.DEBUG
LOGGER_NAME="parser"

FORMAT='%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT);
logger = logging.getLogger(LOGGER_NAME);
logger.setLevel(loglevel)

from pyparsing import Word,alphas,OneOrMore,Optional


class UnknownVariableException(Exception):
    pass

kt = {'contexts':{},'globals':{},'rvalues':[],'functions':[]}

def print_single_line(s,l,t):
    logger.debug("print_single_line-"+str(t))
    
def start_context(s,l,t):
    logger.debug("start-context: "+str(t))
    kt ['contexts'][t[1]]={'attributes':{}}

def update_variable(s,l,t):
    logger.debug("update_variable - t="+str(t))
    kt['globals'][t[0]]=t[2]
    
def update_attribute(s,l,t):
    logger.debug("update_attribute - "+str(t))
    kt['contexts'][t[0]]['attributes'][t[2]]=t[4]

def updateKT(s,location,tokens):
    logger.debug("location="+str(location)+ " s=\""+str(s)+" tokens="+str(tokens))

def set_rvalue(s,l,t):
    logger.debug("rvalue - t="+str(t))
    if t[0] not in kt['rvalues']:
        kt['rvalues'].append(t[0])

def set_function(s,l,t):
	logger.debug("set_function - t"+str(t))
	if t[0] not in kt['functions']:
		kt['functions'].append(t[0])
	variables      = [t[i] for i in xrange(2,len(t),2)]
        print "function has variables : ", variables
        attributeNames = reduce(lambda x,y: x+y, [context['attributes'].keys() for name,context in kt['contexts'].items()])
        if any( var not in attributeNames and var not in kt['globals'] for var in variables ):
            raise UnknownVariableException()
	



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
argument              = Word(alphas) + Optional(",")
funcDef               = Word(alphas) + "(" + OneOrMore(argument) + ")"
line                  = startContext + ";" | setVariableValue + ";" | setAttributeValue + ";" | funcDef + ";"

grammar               = OneOrMore(line)


setAttributeValue.setParseAction(update_attribute)
setVariableValue.setParseAction(update_variable)
#line.setParseAction(print_single_line)
startContext.setParseAction(start_context)
rvalue.setParseAction(set_rvalue)
funcDef.setParseAction(set_function)

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
