
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END, ttk
import sqlalchemy as db
from arquitetura import Filmes, session

engine = db.create_engine('mysql+pymysql://root:@localhost:3306/acervo')

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

# FUNÇÕES
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def nome():
    nome = caixa_nome.get("1.0", END)
    return nome

def genero():
    genero = caixa_genero.get("1.0", END)
    return genero

def diretor():
    diretor = caixa_diretor.get("1.0", END)
    return diretor

def duracao():
    duracao = caixa_duracao.get("1.0", END)
    return duracao

def ano():
    ano = caixa_ano.get("1.0", END)
    return ano


def comitar():
    filme = Filmes(nome=nome(),
                   genero=genero(),
                   diretor=diretor(),
                   duracao=duracao(),
                   ano=ano())
    
    session.add(filme)
    session.commit()

    caixa_nome.delete('1.0',END)
    caixa_genero.delete('1.0',END)
    caixa_diretor.delete('1.0',END)
    caixa_duracao.delete('1.0',END)
    caixa_ano.delete('1.0',END)

    visualizar()

def remover():
    item_selecionado = visualizacao.selection()
    if item_selecionado:
        nome_filme = visualizacao.item(item_selecionado)['values'][0]
        nome_genero = visualizacao.item(item_selecionado)['values'][1]
        nome_diretor = visualizacao.item(item_selecionado)['values'][2]
        nome_duracao = visualizacao.item(item_selecionado)['values'][3]
        nome_ano = visualizacao.item(item_selecionado)['values'][4]

        

        filme_selecionado = session.query(Filmes).filter_by(nome=nome_filme,
                                                            genero=nome_genero,
                                                            diretor=nome_diretor,
                                                            duracao=nome_duracao,
                                                            ano=nome_ano).first()
        session.delete(filme_selecionado)v
        session.commit()
        visualizar()



window = Tk()

window.geometry("800x423")
window.configure(bg = "#55548F")


canvas = Canvas(
    window,
    bg = "#55548F",
    height = 423,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

#subistituir o retangulo branco pelas informações
# canvas.create_rectangle(
#     14.0,
#     33.0,
#     785.0,
#     256.0,
#     fill="#FFFFFF",
#     outline="")

def visualizar():
    global visualizacao
    visualizacao = ttk.Treeview(window, selectmode="browse")
    visualizacao.place(x=14.0,
                    y=33.0,
                    width=771.0,
                    height=223)

    #QUANTIDADE DE COLULAS
    visualizacao['columns'] = ('1','2','3','4','5')

    #TAMANHO E ALINHAMENTO
    visualizacao.column('1',width= 130)
    visualizacao.column('2',width= 50)
    visualizacao.column('3',width= 60)
    visualizacao.column('4',width= 20)
    visualizacao.column('5',width= 20)

    # NOMEANDO AS COLUNAS
    visualizacao['show'] = 'headings' #Para mostrar apenas colunas com títulos

    visualizacao.heading('1',text='Nome')
    visualizacao.heading('2',text='Gênero')
    visualizacao.heading('3',text='Diretor')
    visualizacao.heading('4',text='Duração')
    visualizacao.heading('5',text='Ano')


    #para anexar os dados do banco de dados feito no xampp + mysql
    lista_de_filmes = session.query(Filmes).all()

        # Essas aspas duplas "" querem de dizer, do inicio ao fim da lista ( END)
    for filme in lista_de_filmes:
        visualizacao.insert("", END,
                            values=(filme.nome,filme.genero,
                                    filme.diretor,filme.duracao,filme.ano))
    
visualizar()





caixa_nome = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
caixa_nome.place(
    x=19.0,
    y=289.0,
    width=231.0,
    height=19.0
)

caixa_genero = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
caixa_genero.place(
    x=284.0,
    y=289.0,
    width=231.0,
    height=19.0
)
caixa_diretor = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
caixa_diretor.place(
    x=554.0,
    y=289.0,
    width=231.0,
    height=19.0
)
caixa_duracao = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
caixa_duracao.place(
    x=19.0,
    y=343.0,
    width=231.0,
    height=19.0
)
caixa_ano = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
caixa_ano.place(
    x=284.0,
    y=343.0,
    width=231.0,
    height=19.0
)



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=comitar,
    relief="flat"
)
button_1.place(
    x=67.0,
    y=386.0,
    width=120.0,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=remover,
    relief="flat"
)
button_2.place(
    x=340.0,
    y=386.0,
    width=120.0,
    height=26.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_3.place(
    x=617.0,
    y=386.0,
    width=120.0,
    height=26.0
)

canvas.create_text(
    283.0,
    8.0,
    anchor="nw",
    text="F I L M E S   A S S I S T I D O S",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    18.0,
    265.0,
    anchor="nw",
    text="NOME",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    283.0,
    269.0,
    anchor="nw",
    text="GÊNERO",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    554.0,
    265.0,
    anchor="nw",
    text="DIRETOR",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    21.0,
    327.0,
    anchor="nw",
    text="DURAÇÃO",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    283.0,
    324.0,
    anchor="nw",
    text="ANO",
    fill="#FFFFFF",
    font=("Inter", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
