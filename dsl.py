import sys
import logging

loglevel=logging.DEBUG
LOGGER_NAME="parser"

FORMAT='%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT);
logger = logging.getLogger(LOGGER_NAME);
logger.setLevel(loglevel)

from pyparsing import Word,alphanums,OneOrMore,Optional,Literal,QuotedString



"""

 Grammar for knowledge tree - how would a knowledge bank look like
 Every command is that of a context - there are predefined contexts for now
 "#start-context Company" (Company predefined contexts)
 Company::name = "Herodotus Publishing"
 Company::stock = "HRP"
 Company::prices = {date(2012,11,1):10, date(2012,11,12):10,}

"""

#Document template

#knowledge tree to be populated by the parser
class UnknownVariableException(Exception):
    pass

kt = {'contexts':{},'globals':{},'rvalues':[],'functions':[]}


# parse handlers

def print_single_line(s,l,t):
    logger.debug("print_single_line-"+str(t))
    
def start_context(s,l,t):
    logger.debug("start-context: "+str(t))
    kt ['contexts'][t[1]]={'attributes':{}}

def update_variable(s,l,t):
    logger.debug("update_variable - t="+str(t) + " comparator:'"+str(t[1])+"\'")
    kt['globals'][t[0]]=t[2]
    
def update_attribute(s,l,t):
    logger.debug("update_attribute - "+str(t)+ " comparator:'"+str(t[3])+"\'")
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
        attributeNames = reduce(lambda x,y: x+y, [context['attributes'].keys() for name,context in kt['contexts'].items()])
        if any( var not in attributeNames and var not in kt['globals'] for var in variables ):
            raise UnknownVariableException()
	

def print_comment(s,l,t):
    logger.debug("print_comment - "+str(t))



# define grammar
startContext          = "start_context" + Word(alphanums)
variable              = Word(alphanums) | Word(alphanums)+ "::"+ Word(alphanums)
freeformText          = "freeform"+"("+ OneOrMore(Word(alphanums))+")"
rvalue                = freeformText | Word(alphanums)
comparison            = Literal("=") | Literal("<") | Literal(">")
setAttributeValue     = variable + "::" + Word(alphanums) + comparison + rvalue 
setVariableValue      = variable + comparison + rvalue
argument              = Word(alphanums) + Optional(",")
funcDef               = Word(alphanums) + "(" + OneOrMore(argument) + ")"
comment               = QuotedString('/*', endQuoteChar='*/')
line                  = startContext + ";" | setVariableValue + ";" | setAttributeValue + ";" | funcDef + ";" | comment

# grammar to be exported
grammar               = OneOrMore(line)


def parse_knowledge_tree(s):
    """ return knowledge tree after parsing with the grammar"""
    grammar.parseString(s)
    return kt



#parse actions
setAttributeValue.setParseAction(update_attribute)
setVariableValue.setParseAction(update_variable)
startContext.setParseAction(start_context)
rvalue.setParseAction(set_rvalue)
funcDef.setParseAction(set_function)
comment.setParseAction(print_comment)



