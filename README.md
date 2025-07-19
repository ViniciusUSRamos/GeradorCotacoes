# GeradorCotacoes
Projeto desenvolvido para a empresa UJR Piscinas destinado à geração de cotações personalizadas em formato PDF desenvolvido em Python.


## ⚙️ Funcionalidades
- Interface intuitiva para entrada de dados do cliente e da piscina.
- Campos para informaões como nom, endereço, telefone, CEP, CPF, modelo da piscina, entre outras informações.
- Opção para produtos adicionais na cotação, como:
    - Skimmer
    - Lona de proteção
    - Aquecimento
    - Cascata
    - LED (Com opção de cor e quantidade)
- Geração automática de um arquivo PDF personalizado com os dados preenchidos.
- Cálculo automático do valor total da cotação com base nos valores da piscina, frete e aquecimento.

## 📚 Bibliotecas utilizadas
- tkinter
    - Biblioteca padrão do Python utilizada para desenvolvimento de GUI. Permitindo criação de janelas, botões, caixas de entrada para texto, etc...
- customtkinter
    - Biblioteca baseada em Tk com suporte nativo para temas escuros e design mais moderno.
- fpdf
    - Biblioteca usada para gerar arquivos PDF. Permite a criação de páginas, escrever textos, adicionar imagens e definir estilo e tamanho de fontes.
- Pillow (PIL)
    - Pillow é um fork do PIL (Python Imaging Library), usado para manipulação de imagens.

## ▶️ Como utilizar
1. Instale as bibliotecas utilizadas no programa

2. Execute o código

3. Preencha os campos na interface e clique em "Gerar Orçamento"
