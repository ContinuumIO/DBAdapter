# DBAdapter
Database adapters forked from IOPro

DBAdapter is a Python module containing optimized data adapters for importing
data from a variety of database sources into NumPy arrays and Pandas DataFrame.
Database adapter leverages an optimized pyodbc module for accessing any
relational database that supports the ODBC interface (SQL Server, PostgreSQL,
MySQL, etc).

Build Requirements
------------------

Building DBAdapter requires a number of dependencies. In addition to a C/C++ dev
environment, the following modules are needed, which can be installed via conda:

* NumPy
* Pandas
* unixodbc 2.3.4 (C lib, Linux only)

Building Conda Package
----------------------

Note: If building under Windows, make sure the following commands are issued
within the Visual Studio command prompt for version of Visual Studio that
matches the version of Python you're building for.  Python 2.6 and 2.7 needs
Visual Studio 2008, Python 3.3 and 3.4 needs Visual Studio 2010, and Python
3.5 needs Visual Studio 2015.

1. Build DBAdapter using the following command:
   ```
   conda build buildscripts/condarecipe --python 3.5
   ```

1. DBAdapter can now be installed from the built conda package:
   ```
   conda install dbadapter --use-local
   ```

Building By Hand
----------------

Note: If building under Windows, make sure the following commands are issued
within the Visual Studio command prompt for version of Visual Studio that
matches the version of Python you're building for.  Python 2.6 and 2.7 needs
Visual Studio 2008, Python 3.3 and 3.4 needs Visual Studio 2010, and Python
3.5 needs Visual Studio 2015.

For building DBAdapter for local development/testing:

1. Install most of the above dependencies into environment called 'dbadapter':
   ```
   conda env create -f environment.yml
   ```

   Be sure to activate new dbadapter environment before proceeding.

1. Build DBAdapter using Cython/distutils:
   ```
   python setup.py build_ext --inplace
   ```

Testing
-------

Tests can be run by calling the dbadapter module's test function.  By default
only the TextAdapter tests will be run:

TODO: The pyodbc tests live in the `dbadapter/pyodbc/test*` directories. They are not being run (yet).
```python
python -Wignore -c 'import dbadapter; dbadapter.test()'
```

(Note: `numpy.testing` might produce a FurtureWarning that is not directly
relevant to these unit tests).


Related projects
----------------

- TextAdapter (CSV, JSON, etc): https://github.com/ContinuumIO/TextAdapter
- PostgresAdapter (PostgreSQL): https://github.com/ContinuumIO/PostgresAdapter
- AccumuloAdapter (Apache Accumulo): https://github.com/ContinuumIO/AccumuloAdapter
- MongoAdapter (MongoDB): https://github.com/ContinuumIO/MongoAdapter

