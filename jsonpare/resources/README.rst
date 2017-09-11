|build-status|

============
Introduction
============

*jsonpare* is an efficient command-line utility that simply picks a single item
out of a JSON object/dictionary or list and prints another JSON string. You can
pick an item at the top-level, or provide a "key path" that picks down through
multiple levels.

Example
=======

Example data (example.json)::

    {"a": [9, 6, {"b": [99, 88, 77, "text", 55]}]}

Example usage::

    $ cat example.json | jp a
    [9, 6, {"b": [99, 88, 77, "text", 55]}]

    $ cat example.json | jp a.2.b.3
    "text"

    $ cat example.json | jp a.2 | jp b.3
    "text"

The "-p" option can be used to convert a scalar result to plaintext (with a
return code of 1, rather than 0)::

    $ cat example.json | jp a.2 -p | jp -p b.3
    text

.. |build-status| image:: https://travis-ci.org/dsoprea/JsonPare.svg?branch=master
