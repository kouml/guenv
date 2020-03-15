import unittest
from guenv.cli import command_list, command_new

class TestCommandList(unittest.TestCase):
    """test class of command list
    """

    def test_command_list(self):
        """test method for command list
        """
        test_dic = {
            "user_hoge": {"user_name": "hoge", "email": "hoge@example.com"},
            "user_fuga": {"user_name": "fuga", "email": "fuga@example.com"}
        }
        test_activate = "user_fuga"

        command_list(test_dic, test_activate)


    def test_command_new(self):
        """test method for command new
        """

        test_config_name = "user_hoge"
        test_user_name = "hoge"
        test_email = "hoge@example.com"

        print(command_new(test_config_name, test_user_name, test_email))


if __name__ == "__main__":
    unittest.main()
