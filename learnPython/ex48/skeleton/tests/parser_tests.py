from nose.tools import *
from ex48.parser import *
from ex48 import lexicon


def test_1():
    ''' test # 1 - testing verb, and directions '''
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(x.subject, "player")
    assert_equal(x.verb, "run")


def test_2():
    ''' test # 2 - incorporate lexicon tests.  '''
    result = lexicon.scan("go north")
    print(result)
    x = parse_sentence(result)
    assert_equal(x.subject, "player")
    assert_equal(x.verb, "go")
