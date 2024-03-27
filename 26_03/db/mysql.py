class MySQLDB:
    def __init__(self) -> None:
        self.__conexao = 'MySQLDB'

    def conectar(self) -> str:
        print(f'Conectado {self.__conexao}')
        return self.__conexao
    def desconectar(self) -> str:
        print('desconectar')
        return self.__conexao