import tkinter as tk
from tkinter import filedialog, Label
from os import startfile

from models.mapping import Mapeamento


class Janela1:

    def __init__(self, master) -> None:
        self.master = master
        self.frame = tk.Frame(self.master)

        self.fra_texto_arquivos = tk.Frame(self.master)
        self.fra_texto_diretorio = tk.Frame(self.master)

        self.mapeamento = Mapeamento([], '')

        self.texto_arquivos = Label(self.fra_texto_arquivos, text='Files added here')
        self.texto_diretorio = Label(self.fra_texto_diretorio, text='Directory chosen will be here')

        self.Bset_file = tk.Button(self.frame, text='Select files', command=self.listando_arquivos)
        self.Bset_dir = tk.Button(self.frame, text='Select directory', command=self.selecionando_diretorio)
        self.Bapply = tk.Button(self.frame, text='Apply', command=self.aplica_move)
        self.Bcancel = tk.Button(self.frame, text='Cancel', command=self.master.destroy)
        self.Bclear = tk.Button(self.frame, text='Clear', command=self.resetar)

        self.Bset_file.pack(side='left', expand=True, fill='both', pady=10, padx=5)
        self.Bset_dir.pack(side='left', expand=True, fill='both', pady=10, padx=5)
        self.Bapply.pack(side='left', expand=True, fill='both', pady=10, padx=5)
        self.Bcancel.pack(side='left', expand=True, fill='both', pady=10, padx=5)
        self.Bclear.pack(side='left', expand=True, fill='both', pady=10, padx=5)

        self.texto_arquivos.pack(side='bottom')
        self.texto_diretorio.pack(side='bottom')

        self.frame.pack()
        self.fra_texto_arquivos.pack(side='bottom')
        self.fra_texto_diretorio.pack(side='bottom')

    def listando_arquivos(self) -> None:
        """Add files"""
        file_path = list(filedialog.askopenfilename(multiple=True))
        self.mapeamento.arquivos = [arquivo for arquivo in file_path if arquivo not in self.mapeamento.arquivos]
        self.texto_arquivos.config(text=f'{self.mapeamento.mostra_arquivos()}')

    def selecionando_diretorio(self) -> None:
        """Set directory"""
        self.mapeamento.diretorio = filedialog.askdirectory()
        self.texto_diretorio.config(text=f'Directory: {self.mapeamento.diretorio}')

    def aplica_move(self):
        """It moves the files chosen by user to the new directory, goes to the logfile maker and abre_diretorio func"""
        if self.mapeamento.arquivos != 0 and self.mapeamento.diretorio != '':
            self.mapeamento.move_arquivos()
        self.mapeamento.log_arquivos()
        self.abre_diretorio()

    def abre_diretorio(self):
        """Open destination directory. Bloqueia botãoes 1-4. Cria txt com arquivos enviados."""
        startfile(self.mapeamento.diretorio)
        self.Bset_file['state'] = 'disabled'
        self.Bset_dir['state'] = 'disabled'
        self.Bapply['state'] = 'disabled'
        self.Bcancel['state'] = 'disabled'

    def resetar(self):
        """Undo all user changes"""
        self.texto_arquivos.config(text='Files added here')
        self.texto_diretorio.config(text='Directory chosen will be here')
        self.mapeamento.diretorio = ''
        self.mapeamento.arquivos.clear()

        if self.Bset_file['state'] == 'disabled':
            self.Bset_file['state'] = 'normal'
            self.Bset_dir['state'] = 'normal'
            self.Bapply['state'] = 'normal'
            self.Bcancel['state'] = 'normal'
