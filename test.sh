#!/bin/bash

if [ "$TP" = "1" ]; then
    nosetests -s -v `pwd`/tests/test_pare.py:TestPare
else
    nosetests -s -v --with-coverage --cover-package=jsonpare `pwd`/tests
fi
