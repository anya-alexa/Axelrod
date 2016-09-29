from unittest import TestCase
from axelrod import Actions
from axelrod.strategies.human import Human, ActionValidator
from .test_player import TestPlayer
from prompt_toolkit.validation import ValidationError

C, D = Actions.C, Actions.D


class TestDocument(object):

    def __init__(self, text):
        self.text = text


class TestActionValidator(TestCase):

    def test_validator(self):
        test_documents = [TestDocument(x) for x in ['C', 'c', 'd', 'D']]
        for test_document in test_documents:
            ActionValidator().validate(test_document)

        test_document = TestDocument('E')
        self.assertRaises(
            ValidationError, ActionValidator().validate, test_document)


class TestHumanClass(TestPlayer):

    name = "Human"
    player = Human
    expected_classifier = {
        'memory_depth': float('inf'),
        'stochastic': True,
        'makes_use_of': set(['length', 'game']),
        'long_run_time': True,
        'inspects_source': True,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def test_init(self):
        human = Human(name='test human', c_symbol='X', d_symbol='Y')
        self.assertEqual(human.name, 'test human')
        self.assertEqual(human.symbols, {C: 'X', D: 'Y'})
