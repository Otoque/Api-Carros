from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Configuração do Banco de Dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./carros.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Esquema do Pydantic 
class CarroCreate(BaseModel):

    # Identificação do veículo
    vin: str
    marca: str
    idMarca: int
    modelo: str
    idModelo: int
    anoModelo: int 
    serie: Optional[str] = None  
    trim: Optional[str] = None
    tipoVeiculo: str
    modeloMotor: str
    configuracaoMotor: str
    numeroCilindros: int
    potenciaHP: float  
    potenciaKW: float
    cilindradaL: float
    cilindradaCC: int
    cilindradaPC: float 
    principalCombustivel: str
    secundarioCombustivel: Optional[str] = None

    # Fabricante
    fabricante: str
    idFabricante: int
    nomeFabricante: str
    cidadeFabrincante: str
    estadoFabricante: str
    paisFabricante: str

# Tabela Carros
class CarroModel(Base):
    __tablename__ = "carros"

    # Identificação do veículo
    id = Column(Integer, primary_key=True, index=True)
    vin = Column(String, unique=True, index=True)
    marca = Column(String)
    idMarca = Column(Integer)
    modelo = Column(String)
    idModelo = Column(Integer)
    anoModelo = Column(Integer)
    serie = Column(String, nullable=True)
    trim = Column(String, nullable=True)
    tipoVeiculo = Column(String)

    # Detalhes do Motor
    modeloMotor = Column(String)
    configuracaoMotor = Column(String)
    numeroCilindros = Column(Integer)
    
    # Medidas técnicas 
    potenciaHP = Column(Float)
    potenciaKW = Column(Float)
    cilindradaL = Column(Float)
    cilindradaCC = Column(Integer)
    cilindradaPC = Column(Float)
    
    # Combustíveis
    principalCombustivel = Column(String)
    secundarioCombustivel = Column(String, nullable=True)

    # Chave estrangeira ligando ao fabricante
    fabricante_id = Column(Integer, ForeignKey("fabricantes.id"))
    fabricante_obj = relationship("FabricanteModel", back_populates="carros")

# Tabela Fabricante
class FabricanteModel(Base):
    __tablename__ = "fabricantes"
    id = Column(Integer, primary_key=True, index=True)
    fabricante = Column(String)
    idFabricante = Column(Integer)
    nomeFabricante = Column(String)
    cidadeFabricante = Column(String)
    estadoFabricante = Column(String)
    paisFabricante = Column(String)
    
    # Relação: Um fabricante pode ter vários carros
    carros = relationship("CarroModel", back_populates="fabricante_obj", lazy="select")
# Cria as tabelas no arquivo .db
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência para abrir/fechar a conexão por requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas da API
@app.get("/carros")
def listar_carros(db: Session = Depends(get_db)):
    return db.query(CarroModel).all()

@app.get("/carros/aleatorio")
def carro_aleatorio(db: Session = Depends(get_db)):
    carro = db.query(CarroModel).options(joinedload(CarroModel.fabricante_obj)).order_by(func.random()).first()
    if not carro:
        raise HTTPException(status_code=404, detail="Nenhum carro encontrado no banco") 
    return carro

@app.get("/carros/{carro_id}")
def obter_carro(carro_id: int, db: Session = Depends(get_db)):
    carro = db.query(CarroModel).filter(CarroModel.id == carro_id).first()
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    return carro

@app.get("/carros/buscar")
def buscar_carros(
    marca: Optional[str] = None, 
    modelo: Optional[str] = None, 
    db: Session = Depends(get_db)
):
    query = db.query(CarroModel)
    
    if marca:
        # O 'ilike' faz uma busca insensível a maiúsculas/minúsculas
        query = query.filter(CarroModel.marca.ilike(f"%{marca}%"))
    
    if modelo:
        query = query.filter(CarroModel.modelo.ilike(f"%{modelo}%"))
    
    return query.all()

@app.post("/carros")
def criar_carro(carro: CarroCreate, db: Session = Depends(get_db)):
    # 1. Cria o fabricante 
    novo_fabricante = FabricanteModel(
        fabricante=carro.fabricante,
        idFabricante=carro.idFabricante,
        nomeFabricante=carro.nomeFabricante,
        cidadeFabricante=carro.cidadeFabrincante,
        estadoFabricante=carro.estadoFabricante,
        paisFabricante=carro.paisFabricante
    )
    db.add(novo_fabricante)
    db.commit() 
    db.refresh(novo_fabricante)

    # 2. Cria o carro 
    novo_carro = CarroModel(
        vin=carro.vin,
        marca=carro.marca,
        idMarca=carro.idMarca,
        modelo=carro.modelo,
        idModelo=carro.idModelo,
        anoModelo=carro.anoModelo,
        serie=carro.serie,
        trim=carro.trim,
        tipoVeiculo=carro.tipoVeiculo,
        modeloMotor=carro.modeloMotor,
        configuracaoMotor=carro.configuracaoMotor,
        numeroCilindros=carro.numeroCilindros,
        potenciaHP=carro.potenciaHP,
        potenciaKW=carro.potenciaKW,
        cilindradaL=carro.cilindradaL,
        cilindradaCC=carro.cilindradaCC,
        cilindradaPC=carro.cilindradaPC,
        principalCombustivel=carro.principalCombustivel,
        secundarioCombustivel=carro.secundarioCombustivel,
        fabricante_id=novo_fabricante.id 
    )
    db.add(novo_carro)
    db.commit()
    db.refresh(novo_carro)
    
    return {"carro": novo_carro, "fabricante": novo_fabricante}