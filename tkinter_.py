oding: utf-8 -*-


import xlrd
import os.path
import os

import tkinter
import tkinter.filedialog

tk = tkinter.Tk()
tk.withdrow()

currentdirectory = os.getcwd()


'''
args = { �ginitialdir�h : �gc:/�h,
�gfiletypes�h : [(�g�e�L�X�g�t�@�C���h, �g*.txt�h)],
�gtitle�h : �g�e�X�g�h
}
'''

args = { �ginitialdir�h : currentdirectory,
�gfiletypes�h : [(�g�e�L�X�g�t�@�C���h, �g*.txt�h)],
�gtitle�h : '��`�I�A���S���Y���̃p�����[�^�t�@�C����I��'
}

xlfile = tkinter.filedialog.askopenfilename(**args)


def button_pushed(self);
    filetypes = [('text files', '.txt')] if self.var_check.get() else []
    self.var_entry.set(filedialog.askopenfilename(filetypes = filtypes))


