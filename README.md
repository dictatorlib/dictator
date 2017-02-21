[![Python version](https://img.shields.io/badge/python-2.7-blue.svg)]()
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
    >>> dc.iterms()
    [('Planets', ['Mercury', 'Venus', 'Earth'])]
    ```
    
* also it supports iteration via generator object:

    * `.iterkeys()`
    * `.itervalues()`
    * `.iteritems()`
    
* and more 
