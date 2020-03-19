import click

from guenv.utils import *


activated_config, config_list = load_config()


@click.group(invoke_without_command=False)
@click.pass_context
def cli(ctx):
    pass

@cli.command()
@click.argument('config_name')
def add(config_name):
    if config_name in config_list.keys():
        print('already exist [{}] in user list '.format(config_name))
    else:
        print('user_name: ', end='')
        user_name = input()
        print('email: ', end='')
        email = input()
        config_list[config_name] = {"user_name": user_name, "email": email}
        save_config(config_list)
        print('added {}'.format(config_name))

@cli.command()
@click.argument('config_name')
def edit(config_name):
    if config_name in config_list.keys():
        print('user_name(now:[{}]): '.format(config_list[config_name]['user_name']), end='')
        user_name = input()
        print('email(now:[{}]): '.format(config_list[config_name]['email']), end='')
        email = input()
        config_list[config_name] = {"user_name": user_name, "email": email}
        save_config(config_list)
        print('edited [{}]'.format(config_name))
    else:
        print('not exist [{}] in user list '.format(config_name))
    set_gitconfig(activated_config, config_list)

@cli.command()
@click.argument('config_name')
def delete(config_name):
    if config_name in config_list.keys():
        del config_list[config_name]
        save_config(config_list)
        print('deleted {}'.format(config_name))
    else:
        print('Error: not exist [{}] in user list'.format(config_name))

@cli.command()
def list():
    if len(config_list) == 0:
        print('Error: need config with following command \n guenv add {config_name}')
        return
    if activated_config not in config_list.keys():
        if not activated_config:
            print('Error: activated user is empty. execute following command \n guenv activate {config_name}')
        else:
            print('Error: activated user [{}] is not exist in user list'.format(activated_config))
    print('----guenv list---')
    for k, v in config_list.items():
        if activated_config == k:
            print("* [{}]".format(k))
        else:
            print("  [{}]".format(k))
        for l, m in v.items():
            print("  {}:{}".format(l, m))

@cli.command()
@click.argument('config_name')
def activate(config_name):
    if config_name in config_list.keys():
        save_activate(config_name)
        print('activate with [{}]'.format(config_name))
        activated_config = config_name
    else:
        print('not exist [{}] in user list'.format(config_name))
    set_gitconfig(activated_config, config_list)


# TODO: implement in future
# @cli.command()
# def replace():
#     click.echo('The subcommand')


if __name__ == "__main__":
    cli()
