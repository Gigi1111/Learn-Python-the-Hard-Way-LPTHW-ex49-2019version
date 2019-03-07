#this is the test LPTHW asks us to write : ex49

from nose.tools import *
from ex48 import parser
from ex48 import lexicon


def	test_sentence():
	s = parser.Sentence(('noun', 'bear'), ('verb', 'eat'), ('noun', 'door'))
	assert_equal(s.subject, 'bear')
	assert_equal(s.verb, 'eat')
	assert_equal(s.object, 'door')
	


def	test_peek():#peek returns first word's type
	word_list = lexicon.scan('princess go north to the door')
	print(word_list)
	assert_equal(parser.peek(word_list), 'noun')
	word_list = lexicon.scan('bear go down and eat the princess')
	print(word_list)
	assert_equal(parser.peek(word_list), 'noun')
	word_list = lexicon.scan('go up to open the cabinet')
	print(word_list)
	assert_equal(parser.peek(word_list), 'verb')
	word_list = lexicon.scan('east of the door')
	print(word_list)
	assert_equal(parser.peek(word_list), 'direction')
	assert_equal(parser.peek(None), None)

def	test_match():#match returns the first word's type and content
	word_list = lexicon.scan('princess go north to the door')
	print(word_list)
	assert_equal(parser.match(word_list, 'noun'), ('noun', 'princess'))
	word_list = lexicon.scan('bear go down and eat the princess')
	print(word_list)
	assert_equal(parser.match(word_list, 'noun'), ('noun', 'bear'))
	word_list = lexicon.scan('go up to open the cabinet')
	print(word_list)
	assert_equal(parser.match(word_list, 'verb'), ('verb', 'go'))
	word_list = lexicon.scan('east of the door')
	print(word_list)
	assert_equal(parser.match(word_list, 'direction'), ('direction','east'))
	assert_equal(parser.match(None, 'stop'), None)
			


def	test_skip():#skip returns the first word's type and content
	word_list = lexicon.scan('bear eat door')
	parser.skip(word_list, 'noun')#if first is type, skip it, if not, stay the same
	assert_equal(word_list, [('verb', 'eat'), ('noun', 'door')])
	word_list = lexicon.scan('eat door')
	parser.skip(word_list, 'noun')#if first is type, skip it, if not, stay the same
	assert_equal(word_list, [('verb', 'eat'), ('noun', 'door')])
	word_list = lexicon.scan('east eat door')
	parser.skip(word_list, 'noun')#if first is type, skip it, if not, stay the same
	assert_equal(word_list, [('direction', 'east'),('verb', 'eat'), ('noun', 'door')])
	word_list = lexicon.scan('the eat door')
	parser.skip(word_list, 'stop')
	assert_equal(word_list, [('verb', 'eat'), ('noun', 'door')])
	

def	test_parse_verb():
	word_list = lexicon.scan('go eat door')
	assert_equal(parser.parse_verb(word_list), ('verb', 'go'))
	word_list = lexicon.scan('bear eat door')
	assert_raises(parser.ParserError, parser.parse_verb, word_list)
	word_list = lexicon.scan('the east bear eat door')
	assert_raises(parser.ParserError, parser.parse_verb, word_list)
	word_list = lexicon.scan('I am only trying to make this longer before verb: go eat door')
	assert_raises(parser.ParserError, parser.parse_verb, word_list)

def	test_parse_object():
	word_list = lexicon.scan('bear eat door')
	assert_equal(parser.parse_object(word_list), ('noun', 'bear'))
	word_list = lexicon.scan('east eat door')
	assert_equal(parser.parse_object(word_list), ('direction', 'east'))
	word_list = lexicon.scan('go eat door')
	assert_raises(parser.ParserError, parser.parse_object, word_list)
	word_list = lexicon.scan('the east')
	assert_equal(parser.parse_object(word_list), ('direction', 'east'))
	word_list = lexicon.scan('the it')
	assert_raises(parser.ParserError, parser.parse_object, word_list)
	
def	test_parse_subject():
	word_list = lexicon.scan('eat door')
	s=parser.parse_subject(word_list,('noun', 'player'))
	assert_equal(s.subject, 'player')
	assert_equal(s.verb, 'eat')
	assert_equal(s.object, 'door')
	
def	test_parse_sentence():
	word_list = lexicon.scan('princess go the door')
	s=parser.parse_sentence(word_list)
	assert_equal(s.subject, 'princess')
	assert_equal(s.verb, 'go')
	assert_equal(s.object, 'door')
	word_list = lexicon.scan('stop at bear')
	s=parser.parse_sentence(word_list)
	assert_equal(s.subject, 'player')
	assert_equal(s.verb, 'stop')
	assert_equal(s.object, 'bear')
	
	word_list = lexicon.scan('noth eat bear')
	s=parser.parse_sentence
	assert_raises(parser.ParserError, s, word_list)
	