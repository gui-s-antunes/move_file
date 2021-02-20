import tkinter as tk
from tkinter import filedialog, Label
from os import startfile

from models.mapping import Mapeamento
from utils.helper import user_action


class Janela1:

    def __init__(self, master) -> None:
        self.master = master
        self.frame = tk.Frame(self.master)

        self.fra_texto_arquivos = tk.Frame(self.master)
        self.fra_texto_diretorio = tk.Frame(self.master)

        self.mapeamento = Mapeamento([], '')
        self.button_list = []

        self.texto_arquivos = Label(self.fra_texto_arquivos, text='Files added here')
        self.texto_diretorio = Label(self.fra_texto_diretorio, text='The chosen directory will be here')

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

        self.button_to_list()
        self.button_controller(0)

    def listando_arquivos(self) -> None:
        """Add files"""
        file_path = list(filedialog.askopenfilename(multiple=True))
        self.mapeamento.arquivos = [arquivo for arquivo in file_path if arquivo not in self.mapeamento.arquivos]
        self.button_controller(user_action(self.mapeamento.arquivos, self.mapeamento.diretorio))
        self.texto_arquivos.config(text=f'{self.mapeamento.mostra_arquivos()}')

    def selecionando_diretorio(self) -> None:
        """Set directory"""
        self.mapeamento.diretorio = filedialog.askdirectory()
        self.button_controller(user_action(self.mapeamento.arquivos, self.mapeamento.diretorio))
        self.texto_diretorio.config(text=f'Directory: {self.mapeamento.diretorio}')

    def aplica_move(self):
        """It moves the files chosen by user to the new directory, goes to the logfile maker and abre_diretorio func"""
        if self.mapeamento.arquivos != 0 and self.mapeamento.diretorio != '':
            self.button_controller(3)
            self.mapeamento.move_arquivos()
        self.mapeamento.log_arquivos()
        self.abre_diretorio()

    def abre_diretorio(self):
        """Open destination directory"""
        startfile(self.mapeamento.diretorio)

    def resetar(self):
        """Undo all user changes"""
        self.texto_arquivos.config(text='Files added here')
        self.texto_diretorio.config(text='The chosen directory will be here')
        self.mapeamento.diretorio = ''
        self.mapeamento.arquivos.clear()
        self.button_controller(0)

    def button_to_list(self) -> None:
        self.button_list.extend([self.Bset_file, self.Bset_dir, self.Bapply, self.Bcancel, self.Bclear])

    def button_controller(self, mode) -> None:
        choice = {
            0: ['normal', 'normal', 'disabled', 'normal', 'disabled'],  # Start or After pressed clear button
            1: ['normal', 'normal', 'disabled', 'normal', 'normal'],  # after some user action
            2: ['normal', 'normal', 'normal', 'normal', 'normal'],  # after dir and at least 1 file are chosen
            3: ['disabled', 'disabled', 'disabled', 'disabled', 'normal']  # after pressed apply button
        }

        # for state in choice.get(mode):
        choice_mode = choice.get(mode)
        # dicio = zip(self.button_list, choice_mode)
        for position in zip(self.button_list, choice_mode):  # zip: (buttons[1], choice[1], buttons[2], choice[2]...)
            position[0]['state'] = position[1]  # button[1]['state'] = choice[1]...
        # print(list(dicio))


