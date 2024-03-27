class PostgresDB:
    def __init__(self) -> None:
        self.__conexao = 'Post gre'

    def conectar(self) -> str:
        print(f'Conectado {self.__conexao}')
        return self.__conexao
    def desconectar(self) -> str:
        print('desconectar')
        return self.__conexao