import subprocess
import sys
import couchdb

# def install(package):
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# try:
    
# except ModuleNotFoundError:
#     install("couchdb")
    

class MyCouchDB():
    
    def __init__(self, login, password) -> None:
        self.couchserver = couchdb.Server("http://%s:%s@127.0.0.1:5984/" % (login, password))
    
    def getDatabases(self):
        lista = []
        for dbname in self.couchserver:
            lista.append(dbname)
        return lista
    
    def createDatabase(self, name):
        if name not in self.couchserver:
            self.couchserver.create(name)
        return self.couchserver[name]
    
    def getDocs(self, name_database):
        if name_database not in self.couchserver:
            return None
        if name_database == "datasimportantes":
            for item in self.couchserver[name_database].view('getDatas/getDatas'):
                #item.key, item.id, item.value
                print(item.value)
    def insertDoc(self, name_database, document):
        #document  = [{'key': 'value1'}, {'key': 'value2'}]
        for (success, doc_id, revision_or_exception) in self.couchserver[name_database].update(document):
            print(success, doc_id, revision_or_exception)