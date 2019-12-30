from pymongo import MongoClient

mongo = MongoClient()
db = mongo.db
class ImportLogic:

    @staticmethod
    def GetImports(): # -> List(Dict)
        """

        """
        return(list(db.user.find({})))
        