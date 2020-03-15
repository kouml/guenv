# Simple git user environment management tools: guenv
guenv is the simplest git user environemnt management tools.
Mainly, It has 2 features.
1. easily switch to git user like "pyenv"or "rbenv"
2. easily replace git user in previous commit

# Requirements
Python (3.2<=)

# Installation
```
$ pip install guenv
```


# Usage

## 1. swtich guenv
```
$ guenv add {example1}
$ guenv list
$ guenv activate {example1}
```

After guenv activate, You can commit with {example1} config.

## 2. replace previous commit
```
$ guenv replace {example1}
```

guenv replace can rewrite the previous commiter and author.


# Commands Usage
```
Commands:
  activate
  edit
  list
  new
  remove
  replace
```


```
$ guenv list
[config_name1]
hoge
hoge@example.com

*[config_name1]
fuga
fuga@example.com
```

```
$ guenv activate {config_name1}
active user is [].
```

```
$ guenv replace {config_name1} {config_name2}
```


```
$ guenv new
```

```
$ guenv edit
```

```
$ guenv remove {config_name1}
removed [].
```
