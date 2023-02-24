import unittest
from main import Persona
from unittest.mock import patch


class TestPersona(unittest.TestCase):

    @patch('builtins.input', side_effect=[43279706, 'Freytes', 'Abril'])
    def test_persona(self, mock_input):
        persona = Persona()
        persona.input()
        self.assertEqual(persona.__repr__(), "Persona: 43279706 - Freytes, Abril")


if __name__ == "__main__":
    unittest.main()