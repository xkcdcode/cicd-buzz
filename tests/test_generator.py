from buzz import generator
import unittest

def test_sample_single_word():
    pop = ('foo', 'bar', 'foobar')
    word = generator.sample(pop)
    assert word in pop


def test_sample_multiple_words():
    pop = ('foo', 'bar', 'foobar')
    words = generator.sample(pop, 2)
    assert len(words) == 2
    assert words[0] in pop
    assert words[1] in pop
    assert words[0] is not words[1]


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
