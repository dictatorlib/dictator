# Dictator

Dictator is an experimental Python library aimed to make work with Redis DB transparent as a simple dict object.

It's easy to start by creating `Dictator` object

    dc = Dictator(host='localhost', port=6379, db=0)
    
For the moment it handles not all features of Python Dict but basics:

* `.set(key, value)`

    ```
    >>> dc.set('Planets', ['Mercury', 'Venus', 'Earth'])
    >>> dc['Stars'] = ['Sun'] 
    ```

* `.get(key)`

    ```
    >>> dc['Stars']
    ['Sun']
    >>> dc.get('Planets')
    ['Mercury', 'Venus', 'Earth']
    ```
    
    You can set default value for `get()` function just like for a `dict`-object:
    
    ```
    >>> dc.get('Comets', 'No data')
    'No data'
    ```

* `.pop(key, default=None)`
    
    ```
    >>> dc.pop('Stars')
    ['Sun']
    >>> dc.pop('Comets')
    
    ```
    
* `.delete(key)`

    ```
    >>> dc.pop('Comets', 'No data')
    'No data'
    ```

* `.keys()` and `.values()`

    ```
    >>> dc.keys()
    ['Planets', 'Stars']
    >>> dc.values()
    [['Mercury', 'Venus', 'Earth']]
    ```
        
* `.items()`

    ```
    >>> dc.iterms()
    [('Planets', ['Mercury', 'Venus', 'Earth'])]
    ```
    
* also it supports iteration via generator object:

    * `.iterkeys()`
    * `.itervalues()`
    * `.iteritems()`
    
* and of course 'len()'

    ```
    >>> len(dc)
    2
    ```
