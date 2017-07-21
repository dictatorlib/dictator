[![Build Status](https://travis-ci.org/amka/dictator.svg?branch=master)](https://travis-ci.org/amka/dictator)
[![Python version](https://img.shields.io/badge/python-2.7-blue.svg)]()
[![Python version](https://img.shields.io/badge/python-3.6-blue.svg)]()
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]()
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/81816e720b7b48cd8ab217383051dfd5)](https://www.codacy.com/app/meamka/dictator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=amka/dictator&amp;utm_campaign=Badge_Grade)
[![Lintly](https://lintly.com/gh/amka/dictator/badge.svg)](https://lintly.com/gh/amka/dictator/)

# Dictator

Dictator is a tiny library for Robots™ to work with Redis as a Dict.

It handles Redis API commands and represent itself as a dict-like object.

### Install

```bash
$ pip install dictator
```

### Usage

It's easy to start by creating `Dictator` object

```python
>>> dc = Dictator(host='localhost', port=6379, db=0)
```

For the moment it handles not all features of Python Dict but basics:

* `.set(key, value)`

    ```python
    >>> dc.set('Planets', ['Mercury', 'Venus', 'Earth'])
    >>> dc['Stars'] = ['Sun'] 
    ```

* `.get(key)`

    ```python
    >>> dc['Stars']
    ['Sun']
    >>> dc.get('Planets')
    ['Mercury', 'Venus', 'Earth']
    ```
    
    You can set default value for `get()` function just like for a `dict`-object:
    
    ```python
    >>> dc.get('Comets', 'No data')
    'No data'
    ```
* `.update(other=None, **kwargs)`

    ```python
    >>> dc.update({'Stars': ['Sun', 'Vega']})
    >>> dc.update(Stars=['Sun'])
    
    ```
    
* `.pop(key, default=None)`
    
    ```python
    >>> dc.pop('Stars')
    ['Sun']
    >>> dc.pop('Comets')
    
    ```
    
* `.delete(key)`

    ```python
    >>> dc.delete('Comets')
    ```
    or
    ```python
    >>> del dc['Comets']
    ```

* `.keys()` and `.values()`

    ```python
    >>> dc.keys()
    ['Planets', 'Stars']
    >>> dc.values()
    [['Mercury', 'Venus', 'Earth']]
    ```
        
* `.items()`

    ```python
    >>> dc.items()
    [('Planets', ['Mercury', 'Venus', 'Earth'])]
    ```
    
* also it supports iteration via generator object:

    * `.iterkeys()`
    * `.itervalues()`
    * `.iteritems()`

* `.lock(name, timeout=None, sleep=0.1, blocking_timeout=None, lock_class=None, thread_local=True)` will return `redis-py`'s `Lock` object.

    * Manually acquire-release:
    
    ```python
        >>> lock = dc.lock('foo')
        >>> lock.acquire()
        >>> dc.get('foo')
        '776bf70c6de811e799f6c4b301cdb05d'
        >>> lock.release()
        >>> dc.get('foo')
    ```

    * With context manager:

    ```python
        >>> with dc.lock('foo'):
        >>>    print(dc.get('foo'))
        '776bf70c6de811e799f6c4b301cdb05d'
        >>> dc.get('foo'))
    ```

* a copy of a `Dictator` object will be Python's standard `dict`:

    ```python
        >>> from copy import copy, deepcopy
        >>> d = dc.copy()
        >>> d
        {'Planets': ['Mercury', 'Venus', 'Earth']}
        >>> type(d)
        dict
        >>> copy(dc) == deepcopy(dc) == dc.copy()
        True
    ```
    
* and more 
