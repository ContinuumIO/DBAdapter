"""
    DBAdapter
    ~~~~~

    DBAdapter provides tools to interface SQL databases in a fast, memory-efficient way.
"""
from __future__ import absolute_import

from dbadapter._version import get_versions
__version__ = get_versions()['version']
del get_versions

from dbadapter.lib.errors import (AdapterException, AdapterIndexError,
                                  ArgumentError, ConfigurationError,
                                  DataIndexError, DataTypeError,
                                  InternalInconsistencyError, NoSuchFieldError,
                                  ParserError, SourceError, SourceNotFoundError)


def test(verbosity=1, num_records=100000, results=[]):
    #from textadapter.tests.test_DBAdapter import run as run_dbadapter_tests
    #result_text = run_dbadapter_tests(verbosity=verbosity,
    #                                    num_records=num_records)
    #results.append(result_text)
    
    #from textadapter.tests.test_io import run as run_io_tests
    #result_text = run_io_tests(verbosity=verbosity)
    #results.append(result_text)
    
    for result in results:
        if not result.wasSuccessful():
            return False
    return True

# pyodbc module import triggers license message
import dbadapter.pyodbc
