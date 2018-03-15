import sys
import logging

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
    inputString = sys.argv[1]
    
    # parse input string
    kt = dsl.parse_knowledge_tree(inputString)
    print "inputString=",inputString, " KT=",kt

else:
    print "__name__=",__name__
    
    
    
    
