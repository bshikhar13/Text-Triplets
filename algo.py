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


def extract_attributes(word):
	print(word[0][1])


def subtree_NP(sentence):
	#print(sentence)
	sentence = nltk.pos_tag(sentence.split())
	#print(sentence)
	grammar = """NP: {<DT>?<JJ>*<NN>}
				{(<NN>|<NNP>|<CD>)*}"""
	cp = nltk.RegexpParser(grammar)
	result = cp.parse(sentence)
	print(result)
	return result

def subtree_VP(sentence):
	#print(sentence)
	sentence = nltk.pos_tag(sentence.split())
	#print(sentence)
	grammar = "VP: {<VB.*><NP|PP>}"
	cp = nltk.RegexpParser(grammar)
	result = cp.parse(sentence)
	#tree = nltk.Tree(result)
	#print(result)
	return result   

def VP_siblings(sentence):
	print('ss')

def triplet_extraction(sentence):
	result = []

	
	result.append(extract_subject(subtree_NP(sentence)))
	result.append(extract_predicate(subtree_VP(sentence)))
	result.append(extract_object(VP_siblings(sentence)))
		
	return result


def extract_subject(np_subtree):
	subject = np_subtree[0]
	print(subject)
	subject_attributes = extract_attributes(subject)
	result = []
	result.append(subject)
	result.append(subject_attributes)

	return result


def extract_predicate(vp_subtree):
	print('f')

document = """Android One is good. Iphone has battery Drain problem. Andrid One has good design. Android one includes SnapDragon Processor. Android one has 4 GB RAM"""

for sent in nltk.sent_tokenize(document):
	print(sent)
	temp = triplet_extraction(sent)
	print(temp)