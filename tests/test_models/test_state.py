#!/usr/bin/python3
"""
   TestState module
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    TestState class
    """
    def test_state_creation(self):
        """
        Test instance creation
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_state_variables(self):
        """
        test variables creation
        """
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_id(self):
        """
        test unique id for state
        """
        state_id_1 = State()
        state_id_2 = State()
        self.assertNotEqual(state_id_1, state_id_2)

if __name__ == '__main__':
    unittest.main()
