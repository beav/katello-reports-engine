#!/usr/bin/python

from mongoengine.connection import connect
from mongoengine import connection, register_connection
from pymongo import Connection
from subprocess import call, PIPE

import os

DUMP_DIR = 'data/db_dump'

def setup_database():
    # Disconnect from the default mongo db, and use a test db instead.
    
    conn = Connection()
    checkin_service = conn["checkin_service"]
    results = conn["results"]
      
    for collection in ['splice_server', 'marketing_product_usage']:
        checkin_service.drop_collection(collection)
        print 'importing %s collection' % collection
        call(['mongoimport', '--db', 'checkin_service', '-c', collection, '--file', 
              '%s.json' % os.path.join(DUMP_DIR, collection)]
              )
    """    
    for collection in ['marketing_report_data']:
            results.drop_collection(collection)
            print 'importing %s collection' % collection
            call(['mongoimport', '--db', 'results', '-c', collection, '--file', 
                  '%s.json' % os.path.join(DUMP_DIR, collection)]
                  ) 
    """

            
    conn.disconnect()

    


setup_database()
