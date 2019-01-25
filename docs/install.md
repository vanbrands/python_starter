# Install

## Install Mac OS X

```bash
❯ brew install python
```
#### Check Version
```bash
❯ python -V
Python 2.7.15
```
#### Interactive Shell
```bash
❯ python

Python 2.7.15 (default, Aug 22 2018, 16:36:18)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```


- Python 2.x legacy version
  - 2.7 final version (2010)
- Pyhton 3.x present version

## Concepts
- [**pip**](https://packaging.python.org/tutorials/installing-packages/): package manager
- [**pypi**](https://pypi.org/): package repository
- [**virtualenv**](https://virtualenv.pypa.io/en/latest/userguide/): create isolated environments
- [**ipython**](https://ipython.org/): improved interactive shell

## Manage Packages

#### Install
```bash
❯ pip install <lib_name>
```
#### List
```bash
❯ pip list
```
#### Save requirements
```bash
❯ pip freeze > requirements.txt
```
#### Install from requirements
```bash
❯ pip install -r requirements.txt
```

## Virtual Environments

#### Install
```bash
❯ pip install virtualenv
```
#### Create
```bash
❯ virtualenv <folder_name>
```
#### Activate & Deactivate
```bash
❯ source <folder_name>/bin/activate ## Activate
❯ deactivate ## Deactivate Environment
```
#### Delete
```bash
❯ rm -rf <folder_name>
```

## IPython

- tab-completion
- object introspection
- system shell access
- command history
- special command system

#### Install
```bash
❯ pip install ipython
```
#### Version
```bash
❯ ipython -V
5.8.0
```

#### Start
```bash
❯ ipython

Python 2.7.15 (default, Aug 22 2018, 16:36:18)
Type "copyright", "credits" or "license" for more information.

IPython 5.8.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:
```
