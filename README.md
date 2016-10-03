# Dictator

Dictator is a tiny library for Robots™ to work with Redis as a Dict.

It handles Redis API commands and represent itself as a dict-like object.


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
    
* and of course `len()`

    ```python
    >>> len(dc)
    2
    ```
