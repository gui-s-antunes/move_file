from shutil import move
from os import path
from utils.helper import verify_directory, verify_file, get_time


class Mapeamento:

    def __init__(self, arquivos: list[str], diretorio: str) -> None:
        """
        :param arquivos: files chosen by user (their absolute pathes).
        :param diretorio: directory chosen by user (its absolute path).
        """
        self.__arquivos = arquivos
        self.__diretorio = diretorio

    @property
    def arquivos(self) -> list[str]:
        """
        :return: the list of chosen files pathes.
        """
        return self.__arquivos

    @property
    def diretorio(self) -> str:
        """
        :return: directory chosen by user.
        """
        return self.__diretorio

    @arquivos.setter
    def arquivos(self, camin: str) -> None:
        """
        Add a new file path to the file list.
        :param camin: new path to be added to the list of file pathes.
        """
        """Adiciona arquivos que o usuário adiciona, vai sendo adicionado quantas vezes ele quiser"""
        self.__arquivos += camin

    @diretorio.setter
    def diretorio(self, caminho: str) -> None:
        """
        Set the directory path chosen by user.
        :param caminho: directory path
        """
        self.__diretorio = caminho

    def move_arquivos(self) -> None:
        """
        Moves each chosen file to the new directory
        """
        if verify_directory(self.diretorio):
            for file in self.arquivos:
                try:
                    if verify_file(file):
                        move(file, self.diretorio)
                except Exception as e:
                    print(e)

    def mostra_arquivos(self) -> str:
        """
        It returns a list (string) of the files chosen by user.
        :return: a string with easier view format.
        """
        lista = '\nArquivos:'
        for arquivo in self.__arquivos:
            lista += f'\n{arquivo}'
        return lista

    def log_arquivos(self) -> None:
        """
        It creates a logfile that records added files (their original pathes).
        """
        file_log = self.diretorio + '/logfile-' + get_time() + '.txt'
        with open(file_log, 'w') as file:
            file.write(f'LogFile\n\n---\n\nBy: Guilherme Antunes\n\n---\n\nDestination folder: '
                       f'{self.diretorio}\n\nDate-time: {get_time()}')
            for arq in self.arquivos:
                file.write(f'\n{arq}')
