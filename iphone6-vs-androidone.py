import nltk
nltk.data.path.append('/home/shikhar/Documents/Shikhar/namo/nltk_data')
import  re, pprint
from nltk.corpus import stopwords
from neo4jrestclient.client import GraphDatabase
from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import Tree
from neo4jrestclient.client import GraphDatabase
from nltk.chunk import RegexpParser
from py2neo import neo4j
from py2neo import Graph


gdb = GraphDatabase("http://localhost:7474/db/data/",username="neo4j",password="bshikhar13")



def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def traverse(t):
    print('cc')
    try:
        t.node
    except AttributeError:
        return
    else:
        if t.node == 'SUBJECT': print t # or do something else
        else:
            for child in t:
                traverse(child)


def insert_database(n1,v1):
    
    n_1 = n1[0]
    n_2 = n1[1]
    v_1 = v1[0]

    print(n_1+"  =>  "+v_1+"  =>  "+n_2)
    
    none = gdb.nodes.create(name=n_1)
    ntwo = gdb.nodes.create(name=n_2)
    none.relationships.create(v_1,ntwo)

    # flipkart = gdb.labels.create("Nodes")
    # flipkart.add(none,ntwo)
    # mynode1 = gdb.find(Nodes, name=n_1)
    # mynode2 = gdb.find(Nodes, name=n_2)
    #print("sssssssssssssssssss")
    # if len(mynode1)>0 and len(mynode2)==0 :
    #     target_node = gdb.nodes.create(name=n_2)
    #     for the_node in mynode1:
    #         relationship = gdb.create((the_node, "Nodes", target_node, {"key": v_1}))


    # if len(mynode1)>0 and len(mynode2)>0 :
    #      for the_node in mynode1:
    #         for target_node in mynode2:
    #             relationship = gdb.create((the_node, "Nodes", target_node, {"key": v_1}))

    # if len(mynode1)==0 and len(mynode2)==0 :
    #       none = gdb.nodes.create(name=n_1)
    #       ntwo = gdb.nodes.create(name=n_2)
    #       none.relationships.create(v_1,ntwo)

    #       flipkart = gdb.labels.create("Nodes")
    #       flipkart.add(none,ntwo)

    # if len(mynode1)==0 and len(mynode2)>0 :
    #       target_node = gdb.nodes.create(name=n_1)
    #       for the_node in mynode1:
    #         relationship = gdb.create((the_node, "Nodes", target_node, {"key": v_1}))  
    
    
def find_chunk(s):
   # print("bmb")
    #pattern = "SB: {<DT>?<JJ>*<NN>*}"
    #pattern = "SB: {<NN>* <NNP>* <VBD>* <VBZ>* <NN>*<NNP>*}"
    pattern = '''SUBJECT:{<JJ>(<NN>|<NNP>|<CD>)*}
                        {(<NN>|<NNP>|<CD>)*}
                 VERB:{(<VB>|<VBD>|<VBZ>)*}

    '''

    # pattern = '''SUBJECT:{(<NN>|<NNP>|<CD>)*}<.>* 
    #               VERB:{(<VB>|<VBD>|<VBZ>)*}
    #  '''

    NPChunker = RegexpParser(pattern)
    result = NPChunker.parse(s)
   # print(result)
   # traverse(result)
    return result 

            

document = """Android One is good. Iphone has battery Drain problem. Andrid One has good design. Android one includes SnapDragon Processor. Android one has high RAM. iPhone has nice display. """

sentences = nltk.sent_tokenize(document)
sentences = [nltk.word_tokenize(sent) for sent in sentences]
sentences = [w for w in sentences if not w in stopwords.words('english')]

sentences = [nltk.pos_tag(sent) for sent in sentences]

for s in sentences:
   # print("****************************************************************")
    chunked = find_chunk(s)
    s1 = []
    v1 = []
    
    p=0;
    print(chunked)
   # print(len(chunked))
    for i in range(0,len(chunked)-1):
        a = chunked[i]
        #print("----------")
        len_of_chunk = len(a)
        
        test=""
        counter=0;
        for i in range(0,len_of_chunk):
            test = test + str(a[i][0]) + " "
        p=p+1
        #print(p)    
       # print(a.node)
       # print("Ris@@")

        if a.node == "VERB":
            v1.append(test)
        #
        if a.node == "SUBJECT":
            s1.append(test)
            

    #print(s1)        
    #print(v1)

    insert_database(s1,v1)

    #print("----------------")
   # print(sentences)
#tagged_text = sentences
#gold_chunked_text = tagstr2tree(tagged_text)
#print(gold_chunked_text)

final_list=[]
for se in sentences:
    for ne in se:
        if (ne[1]=='NN' or ne[1]=='NNS' or ne[1]=='NNP' or ne[1]=='NNPS') and ne[0]!='[' and ne[0]!=']' and ne[0]!='':
            #print(ne[0])
            final_list.append(ne[0])
        #   print("\n")


