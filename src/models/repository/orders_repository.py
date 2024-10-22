from bson import ObjectId

class OrdersRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_ofdocuments: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_ofdocuments)

    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data

    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
        return response


    def select_many_with_properties(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter, # filtro de busca
            {"_id": 0, "cupom": 0} # Opções de retorno
        )
        return data

    def select_if_propery_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find({"addres": {"$exists": True}})
        return response

    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({ "_id": ObjectId(object_id)})
        return data

    def edit_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id": ObjectId("67165266c5cc553a2ca0a3c9") }, # Filtro
            { "$set": {"itens.pizza.quantidade": 30} } # Edição
        )

    def edit_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            { "itens": { "$exists": True }  }, # Filtro
            { "$set": {"itens.refrigerante.quantidade": 100} } # Edição
        )
    def edit_registry_with_increment(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id": ObjectId("67165266c5cc553a2ca0a3c9")}, # Filtro
            { "$inc": {"itens.pizza.quantidade": 50} } # Edição
        )
