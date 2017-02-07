Pyzure-DocumentDB
=================

A simple python wrapper for the python client of Azure DocumentDB

Installation
------------

Using pip::

    pip install pyzure_documentdb

Note: pydocumentdb requires requests of version 2.10.0

Usage
-----

A credential file containing secret things is needed::

    # credentials.py
    DOCUMENTDB_NAME = 'mydocdb'
    DOCUMENTDB_HOST = 'https://mydocdb.documents.azure.com:443/'
    DOCUMENTDB_KEY = '!@#!@#!@#YOUR_SECRET_KEY!@#!@#!@#'

Import and initiate::

    import credentials
    from pyzure_docdb.documentdb import DocumentDB

    docdb = DocumentDB(credentials)

Get
~~~

Get a database or a collection with each id::

    db = docdb.get_database('mydb')
    coll = docdb.get_collection('mydb', 'mycoll')

Get a single document with a series of id (database - collection - document)::

    doc = docdb.get_document('mydb', 'mycoll', 'mydoc')

Or get all documents::

    docs = docdb.get_documents('mydb', 'mycoll')

Query
~~~~~
Query with your custom sql::

    sql = 'SELECT * FROM c WHERE c.type=1'
    docs = docdb.query_documents('mydb', 'mycoll', sql)

Create
~~~~~~

Create a database, a collection by its id::

    newdb = docdb.create_db('mynewdb')
    newcoll = docdb.create_collection('mynewdb', 'mynewcoll')

Create a document giving a dictionary::

    data = {'field1': 'value1', 'field2': 'value2'}
    newdoc = docdb.create_document('mynewdb', 'mynewcoll', data)

Upsert (update or insert) a document::

    doc = docdb.upsert_document('mynewdb', 'mynewcoll', data)

Replace
~~~~~~~

Replace a document by modifying the original one::

    doc = docdb.get_document('mydb', 'mycoll', 'mydoc')
    doc['type'] = 3
    doc.update(another_dict)
    docdb.replace_document(doc)

Delete
~~~~~~

Empty a collection by deleting all documents of the collection::

    docdb.empty_documents('mydb', 'mycoll')
