# -*- coding:utf-8 -*-
from pydocumentdb import document_client
import requests

class DocumentDB(object):
	def __init__(self, credentials):
		self.HOST = credentials.DOCUMENTDB_HOST
		self.KEY = credentials.DOCUMENTDB_KEY
		self.client = document_client.DocumentClient(self.HOST, {'masterKey': self.KEY})
	def create_db(self, db_id):
		db = self.client.CreateDatabase({'id': db_id})
		return db
	def create_collection(self, db_id, coll_id):
		db = self.get_db(db_id)
		coll = self.client.CreateCollection(db['_self'], {'id': coll_id})
		return coll
	def get_db(self, db_id):
		db = next((data for data in self.client.ReadDatabases() if data['id'] == db_id))
		return db
	def get_collection(self, db_id, coll_id):
		db = self.get_db(db_id)
		coll = next((data for data in self.client.ReadCollections(db['_self']) if data['id'] == coll_id))
		return coll
	def get_document(self, db_id, coll_id, doc_id):
		coll = self.get_collection(db_id, coll_id)
		docs = self.client.QueryDocuments(coll['_self'], 'SELECT * FROM {coll} coll WHERE coll.id="{id}"'.format(coll=coll['id'],id=doc_id))
		return docs.fetch_next_block()[0]
	def get_documents(self, db_id, coll_id):
		coll = self.get_collection(db_id, coll_id)
		docs = self.client.ReadDocuments(coll['_self'])
		return docs

	def replace_document(self, doc):
		doc = self.client.ReplaceDocument(doc['_self'], doc)
		return doc