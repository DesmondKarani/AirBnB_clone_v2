import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import models


class TestConsole(unittest.TestCase):
    """Test cases for the console."""

    def setUp(self):
        """Set up test cases."""
        self.cli = HBNBCommand()

    def test_do_create(self):
        """Test `do_create` with parameters."""
        with patch('sys.stdout', new=StringIO()) as f:
            # Test creating a new User with parameters
            cmd = ('create User email="test@example.com" '
                   'password="password123" first_name="John" last_name="Doe"')
            self.cli.onecmd(cmd)
            # Here, we adjust how user_id is captured
            output = f.getvalue().strip()
            # Assuming the last line of output contains the user_id
            user_id_lines = output.split("\n")
            user_id = user_id_lines[-1]  # Get the last line as the user ID

            self.assertTrue(user_id)

            # Construct the key using the captured user_id
            key = 'User.' + user_id
            self.assertIn(key, models.storage.all(), "User ID not found")

            # Access the user object using the key
            user = models.storage.all()[key]

            # Verify attributes
            self.assertEqual(user.email, "test@example.com")
            self.assertEqual(user.password, "password123")
            self.assertEqual(user.first_name, "John")
            self.assertEqual(user.last_name, "Doe")

    def tearDown(self):
        """Clean up after tests."""
        all_objs = models.storage.all()
        for obj_id in list(all_objs.keys()):
            del all_objs[obj_id]
        models.storage.save()


if __name__ == "__main__":
    unittest.main()
