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


mapEnglish = { 
     'comparators' : {
        ('#have','1') : "has",
        ('#have','n'):'have',
        ('=','1') : 'is',
        ('=','n') : 'are',
        ('>','1') : 'greater than',
        ('>','n') : 'greater than',
        }, 

     }

def document_from_doctemplate(kt,mapEnglish):
    """ generates the english text """
    # uses the mapping of functions and comaparators to a natural language
    for contextName,context in kt['contexts'].items():
        print ("context name="+contextName)
        print (context)
        




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
    document_from_doctemplate(kt,mapEnglish)
    print "KT=",kt
        



    
    
    
    
