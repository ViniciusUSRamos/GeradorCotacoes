# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Gerador.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from fpdf import FPDF as pdf
import os
from PIL import Image, ImageTk
import PyInstaller.__main__
doc = pdf()
doc.add_page()
doc.set_font('Arial')
doc.set_font_size(10)
doc.image('plano_de_fundo.png', x=0, y=0, w=210, h=300)

def submit():
    # pega os valores
    nome_cliente = nome_cliente_entry.get()
    endereco = endereco_entry.get()
    fone = fone_entry.get()
    cpf = cpf_entry.get()
    cep = cep_entry.get()
    valor_piscina = valor_piscina_entry.get()
    frete = frete_entry.get()
    motor = motor_entry.get()
    nome_piscina = nome_piscina_entry.get()
    quant_hidro = quant_hidro_entry.get()
    quant_canos = quant_canos_entry.get()
    skimmer = skimmer_entry.get()
    lona = lona_entry.get()
    aquecimento = aquec_entry.get()
    cascata = cascata_entry.get()
    possui_LED = LED_entry.get()
    quantidade_LED = quant_LED.get()
    cor_do_LED = cor_LED.get()
    valor_aquec = valor_aquecimento.get()

    # verifica campos obrigatórios
    campos = [nome_piscina, quant_canos, quant_hidro, nome_cliente, endereco, fone, cpf, cep, valor_piscina, frete, motor]
    if any(not campo for campo in campos):
        tk.messagebox.showerror('Erro', 'Preencha todos os campos!')
        return
        
    #testando variáveis opcionais
    if valor_aquec == None:
        valor_aquec = 0
    if quantidade_LED == None:
        quantidade_LED = 0

    # converte valores numéricos, com try para evitar crash
    try:
        valor_piscina = int(valor_piscina)
        frete = int(frete)
        valor_aquec = int(valor_aquec)
        quant_hidro = int(quant_hidro)
        quant_canos = int(quant_canos)
        quantidade_LED = int(quantidade_LED) if possui_LED else 0
    except ValueError:
        tk.messagebox.showerror('Erro', 'Valores numéricos inválidos!')
        return

    doc = pdf()
    doc.add_page()
    doc.set_font('Arial', size=10)
    doc.image('plano_de_fundo.png', x=0, y=0, w=210, h=300)

    lista_opcionais = []
    if possui_LED:
        posicao_quant_led = 185.75
        doc.text(155, posicao_quant_led, f'00{quantidade_LED}')
        doc.text(30, posicao_quant_led, f'LED {cor_do_LED}')
    if skimmer:
        lista_opcionais.append('Skimmer')
    if lona:
        lista_opcionais.append('Lona de Proteção')
    if aquecimento:
        lista_opcionais.append('Aquecimento')
    if cascata:
        lista_opcionais.append('Cascata')

    posicao_texto = 179.5
    if possui_LED:
        posicao_quant = 185.75
        posicao_texto = posicao_quant
    else:
        posicao_quant = posicao_texto

    for opcional in lista_opcionais:
        posicao_texto += 6.25
        doc.text(30, posicao_texto, opcional)
        doc.text(155, posicao_texto, '001')

    # Preenche os textos fixos e variáveis
    doc.text(46, 85, nome_cliente)
    doc.text(51.4, 91.5, endereco)
    doc.text(153, 91.5, cep)
    doc.text(50, 98.3, fone)
    doc.text(43, 105, cpf)
    doc.text(30, 135.6, f'Piscina {nome_piscina}')
    doc.text(30, 142, f'Motor de {motor}')
    doc.text(30, 148.4, 'Ponto de Hidromassagem')
    doc.text(30, 154.8, 'Dispositivo de Aspiração')
    doc.text(30, 161, 'Kit de acessórios de Limpeza Completo')
    doc.text(30, 167.4, 'Filtro de Areia')
    doc.text(30, 173.7, 'Espera para Cascata')
    doc.text(30, 179.5, 'Registros e Conexões')

    doc.text(155, 135.6, '001')
    doc.text(155, 142, '001')
    doc.text(155, 148.4, f'00{quant_hidro}')
    doc.text(155, 154.8, '001')
    doc.text(155, 161, '001')
    doc.text(155, 167.4, '001')
    doc.text(155, 173.7, '001')
    doc.text(155, 179.5, f'0{quant_canos}')

    doc.text(30, 250.57, 'Piscina')
    doc.text(30, 257.2, 'Frete')
    doc.text(30, 264, 'Aquecimento')

    valor_total = valor_piscina + frete + valor_aquec

    doc.text(149, 250.57, f'R$ {valor_piscina},00')
    doc.text(150, 257.2, f'R$ {frete},00')
    doc.text(150, 264, f'R$ {valor_aquec},00')
    doc.text(149, 270.18, f'R$ {valor_total},00')

    doc.output(f'Cotacao {nome_cliente}.pdf')
    print('Arquivo criado com Sucesso!')
    tk.messagebox.showinfo('Sucesso', 'Cotação Gerada')

def clear():
    nome_cliente_entry.delete(0, END)
    endereco_entry.delete(0, END)
    fone_entry.delete(0, END)
    cpf_entry.delete(0, END)
    cep_entry.delete(0, END)
    valor_piscina_entry.delete(0, END)
    frete_entry.delete(0, END)
    motor_entry.delete(0, END)
    nome_piscina_entry.delete(0, END)
    quant_hidro_entry.delete(0, END)
    quant_canos_entry.delete(0, END)
    quant_LED.delete(0, END)
    cor_LED.set('Escolha a Cor do LED')
    LED_entry.deselect()
    lona_entry.deselect()
    aquec_entry.deselect()
    cascata_entry.deselect()
    skimmer_entry.deselect()
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')
app = ctk.CTk()
app.geometry('1000x750')
app.title('UJR Piscinas - Gerador de Cotações')
app.resizable(0, 0)
app.iconbitmap('ujr_icon.ico')
file_path = os.path.dirname(os.path.realpath(__file__))
logo = ctk.CTkImage(Image.open(file_path + '/UJR Piscinas - Escuro Transparente.png'), size=(100, 100))
show_logo = ctk.CTkLabel(master=app, image=logo, text=' ').place(x=450, y=40)
nome_cliente_entry = ctk.CTkEntry(app, width=250, height=30, corner_radius=10, placeholder_text='Nome do Cliente')
nome_cliente_entry.place(x=30, y=150)
fone_entry = ctk.CTkEntry(app, width=190, height=30, corner_radius=10, placeholder_text='Telefone: (xx) xxxxx-xxxx')
fone_entry.place(x=300, y=150)
cep_entry = ctk.CTkEntry(app, width=220, height=30, corner_radius=10, placeholder_text='CEP do Cliente')
cep_entry.place(x=510, y=150)
cpf_entry = ctk.CTkEntry(app, width=220, height=30, corner_radius=10, placeholder_text='CPF do Cliente')
cpf_entry.place(x=750, y=150)
endereco_entry = ctk.CTkEntry(app, width=250, height=30, corner_radius=10, placeholder_text='Endereço do Cliente')
endereco_entry.place(x=30, y=205)
valor_piscina_entry = ctk.CTkEntry(app, width=190, height=30, corner_radius=10, placeholder_text='Valor da Piscina')
valor_piscina_entry.place(x=300, y=205)
frete_entry = ctk.CTkEntry(app, width=220, height=30, corner_radius=10, placeholder_text='Valor do Frete')
frete_entry.place(x=510, y=205)
motor_entry = ctk.CTkEntry(app, width=220, height=30, corner_radius=10, placeholder_text='Potência do Motor (1/2 CV, 1/3 CV)')
motor_entry.place(x=750, y=205)
nome_piscina_entry = ctk.CTkEntry(app, width=250, height=30, corner_radius=10, placeholder_text='Nome da Piscina')
nome_piscina_entry.place(x=30, y=260)
quant_hidro_entry = ctk.CTkEntry(app, width=190, height=30, corner_radius=10, placeholder_text='Quantidade de Hidromassagens')
quant_hidro_entry.place(x=300, y=260)
quant_canos_entry = ctk.CTkEntry(app, width=220, height=30, corner_radius=10, placeholder_text='Quantidade de Canos e Conexões')
quant_canos_entry.place(x=510, y=260)
valor_aquecimento = ctk.CTkEntry(app, width=220, height=30, corner_radius=10, placeholder_text='Valor Aquecimento')
valor_aquecimento.place(x=250, y=460)
titulo_opc = ctk.CTkLabel(app, width=60, height=20, text='Opcionais:', font=('Arial Black', 20))
titulo_opc.place(x=30, y=335)
skimmer_entry = ctk.CTkCheckBox(app, width=60, height=20, text='Skimmer')
skimmer_entry.place(x=30, y=380)
lona_entry = ctk.CTkCheckBox(app, height=20, width=60, text='Lona')
lona_entry.place(x=30, y=420)
aquec_entry = ctk.CTkCheckBox(app, height=20, width=60, text='Aquecimento')
aquec_entry.place(x=30, y=460)
cascata_entry = ctk.CTkCheckBox(app, height=20, width=60, text='Cascata')
cascata_entry.place(x=30, y=500)
LED_entry = ctk.CTkCheckBox(app, height=20, width=60, text='LED')
LED_entry.place(x=30, y=540)
quant_LED = ctk.CTkEntry(app, width=150, height=30, corner_radius=10, placeholder_text='Quantidade de LED(s)')
quant_LED.place(x=200, y=580)
cor_LED = ctk.CTkOptionMenu(app, values=['Azul', 'Colorido'], height=28)
cor_LED.set('Escolha a Cor do LED')
cor_LED.place(x=30, y=580)
botao_submit = ctk.CTkButton(app, text='Gerar Orçamento', command=submit, width=150, height=30)
botao_submit.place(x=240, y=650)
botao_clear = ctk.CTkButton(app, text='Limpar Informações', command=clear, width=150, height=30)
botao_clear.place(x=600, y=650)
app.mainloop()
PyInstaller.__main__.run(['Gerador.py', '--onefile', '--windowed'])