import sqlalchemy as db
from sqlalchemy.orm  import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Float

engine = db.create_engine('mysql+pymysql://root:@localhost:3306/acervo')
Base = declarative_base()

class Filmes(Base):
    __tablename__ = 'filmes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80), nullable=False)
    genero = Column(String(60))
    diretor = Column(String(100))
    duracao = Column(Integer)
    ano = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()