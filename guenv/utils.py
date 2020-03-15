import json
import subprocess

CONFIG_PATH = 'config.json'
ACTIVATE_PATH = 'activate'


def save_config(config_list):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config_list, f)


def save_activate(activated_config):
    with open(ACTIVATE_PATH, 'w') as f:
        f.write(activated_config)


def load_config():
    with open(ACTIVATE_PATH, 'r') as f:
        activated_config = f.read().strip()
    with open(CONFIG_PATH, 'r') as f:
        config_list = json.load(f)
    return activated_config, config_list


def set_gitconfig():
    activated_config, config_list = load_config()
    user_name = config_list[activated_config]['user_name']
    email = config_list[activated_config]['email']

    name_out = subprocess.Popen(['git', 'config', '--global', 'user.name', user_name],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

    email_out = subprocess.Popen(['git', 'config', '--global', 'user.email', email],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

