# -*- coding:utf-8 -*-
from pydocumentdb import document_client
import requests

class DocumentDB(object):
	def __init__(self, credentials):
		self.HOST = credentials.DOCUMENTDB_HOST
		self.KEY = credentials.DOCUMENTDB_KEY
		self.client = document_client.DocumentClient(self.HOST, {'masterKey': self.KEY})
	def get_db(self, db_id):
		db = next((data for data in self.client.ReadDatabases() if data['id'] == db_id))
		return db
	def get_collection(self, db_id, coll_id):
		db = self.get_db(db_id)
		coll = next((data for data in self.client.ReadCollections(db['_self']) if data['id'] == coll_id))
		return coll
	def get_document(self, db_id, coll_id, doc_id):
		coll = self.get_collection(db_id, coll_id)
		docs = self.client.QueryDocuments(coll['_self'], u'SELECT * FROM {coll} coll WHERE coll.id="{id}"'.format(coll=coll['id'],id=doc_id))
		doc = docs.fetch_next_block()
		if doc:
			return doc[0]
		else:
			return None
	def get_documents(self, db_id, coll_id):
		coll = self.get_collection(db_id, coll_id)
		docs = self.client.ReadDocuments(coll['_self'])
		return docs
	def query_documents(self, db_id, coll_id, query):
		coll = self.get_collection(db_id, coll_id)
		docs = self.client.QueryDocuments(coll['_self'], query)
		return docs
	def create_db(self, db_id):
		db = self.client.CreateDatabase({'id': db_id})
		return db
	def create_collection(self, db_id, coll_id):
		db = self.get_db(db_id)
		coll = self.client.CreateCollection(db['_self'], {'id': coll_id})
		return coll
	def create_document(self, db_id, coll_id, doc):
		coll = self.get_collection(db_id, coll_id)
		doc = self.client.CreateDocument(coll['_self'], doc)
		return doc
	def upsert_document(self, db_id, coll_id, doc):
		coll = self.get_collection(db_id, coll_id)
		doc = self.client.UpsertDocument(coll['_self'], doc)
		return doc
	def replace_document(self, doc):
		doc = self.client.ReplaceDocument(doc['_self'], doc)
		return doc

	def empty_collection(self, db_id, coll_id):
		docs = self.get_documents(db_id, coll_id)
		for doc in docs:
			self.client.DeleteDocument(doc['_self'])