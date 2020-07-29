"""Unit testing for files extension
   Could test all extensions, but going to test only the most used ones for now: CSV and JSON.
"""

import pandas as pd
import pytest
import src.fhandler as sf


def test_fHandler_csv():
    p = 'dataframe.csv'
    with pytest.raises(OSError) as e:
        sf.fHandler(p)
    message = str(e.value)
    assert message.startswith('[Errno 2]')
    assert 'No such file or directory' in message or 'does not exist' in message


def test_fHandler_json():
    p = 'dataframe.json'
    with pytest.raises(ValueError) as e:
        sf.fHandler(p)
    assert str(e.value) == 'Expected object or value'


def test_warn_read():
    with pytest.warns(UserWarning):
        sf.warn_read('test')
        