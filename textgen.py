import sys
import logging
import argparse
from exceptions import RuntimeError

import dsl

loglevel=logging.DEBUG
LOGGER_NAME="main"

FORMAT='%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT);
logger = logging.getLogger(LOGGER_NAME);
logger.setLevel(loglevel)


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



if __name__ == "__main__":
    # input string
    parser     = argparse.ArgumentParser()
    parser.add_argument("-i","--input-file", help="read input file" , action="store")
    parser.add_argument("-s","--string", help="read string" , action="store")
    parsedArgs = parser.parse_args()
    if parsedArgs.input_file is None and parsedArgs.string is None:
        raise RuntimeError("Must have either string or input-file populated")

    if parsedArgs.input_file is not None and parsedArgs.string is not None:
        raise RuntimeError("Cannot have both string or input-file populated")

    if parsedArgs.input_file is not None:
        for s in open(parsedArgs.input_file).readlines():
            kt = dsl.parse_knowledge_tree(s)
    if parsedArgs.string is not None:
        kt = dsl.parse_knowledge_tree(parsedArgs.string)
        
    print "KT=",kt
    
    # parse input string
    #kt = dsl.parse_knowledge_tree(inputString)
    #print "inputString=",inputString, " KT=",kt

    
    
    
    
