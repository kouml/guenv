import json

CONFIG_PATH = 'config.json'
ACTIVATE_PATH = 'activate'


# io utils
def save_config(config_list):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config_list, f)


def save_activate(activated_config):
    with open(ACTIVATE_PATH, 'w') as f:
        f.write(activated_config)


def load_config():
    # load activate
    with open(ACTIVATE_PATH, 'r') as f:
        activated_config = f.read().strip()
    # load config
    with open(CONFIG_PATH, 'r') as f:
        config_list = json.load(f)
    return activated_config, config_list


def _gitconfig_set():
    activated_config, config_list = load_config()
    user_name = config_list[activated_config]['user_name']
    email = config_list[activated_config]['email']



def gitconfig_setter(func):
    def wrapper():
        func()
        _gitconfig_set()
    return wrapper


# @gitconfig_setter
# def say_whee():
#     print("Whee!")

