import unittest
import logging
import json

import jsonpare.pare

_LOGGER = logging.getLogger(__name__)


class TestPare(unittest.TestCase):
    def test_pare(self):
        data_encoded = """\
{
    "aa": 123,
    "bb": {
        "cc": 456
    }
}
"""

        data = json.loads(data_encoded)

        result = jsonpare.pare.pare(data, 'bb.cc')

        expected = 456

        self.assertEquals(result, expected)
