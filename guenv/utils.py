import os
import json
from json.decoder import JSONDecodeError
import subprocess

default_dir = os.path.dirname(__file__)
os.makedirs(os.path.join(default_dir, 'guenv'), exist_ok=True)

CONFIG_PATH = os.path.join(default_dir, 'config.json')
ACTIVATE_PATH = os.path.join(default_dir, 'activate')


def save_config(config_list):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config_list, f)


def save_activate(activated_config):
    with open(ACTIVATE_PATH, 'w') as f:
        f.write(activated_config)


def load_config():
    if os.path.isfile(ACTIVATE_PATH):
        with open(ACTIVATE_PATH, 'r') as f:
            activated_config = f.read().strip()
    else:
        with open(ACTIVATE_PATH, 'a') as f:
            activated_config = ''

    if os.path.isfile(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            try:
                config_list = json.load(f)
            except JSONDecodeError:
                config_list = {}
    else:
        with open(CONFIG_PATH, 'a') as f:
            config_list = {}

    return activated_config, config_list


def set_gitconfig(activated_config, config_list):
    user_name = config_list[activated_config]['user_name']
    email = config_list[activated_config]['email']

    name_out = subprocess.Popen(['git', 'config', '--global', 'user.name', user_name],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

    email_out = subprocess.Popen(['git', 'config', '--global', 'user.email', email],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

