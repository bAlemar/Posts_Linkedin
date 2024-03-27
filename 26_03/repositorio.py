class Repositorio:
    def select(self,db_connection:any) -> None:
        db_connection.conectar()
        
        #faz algo
        db_connection.desconectar()

        
        # criar prints para indicar o que seu código ta fazendo por ex: # 2000 Produtos unicos encontrados etc...
    def insert(self,db_connection: any) -> None:
        db_connection.conectar()
        #faz algo
        db_connection.desconectar()