from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from typing import Optional, List
from app.models.production_scraped_data import ProductionScrapedData
from app.models.comercialization_scraped_data import ComercializationScrapedData    
from app.models.processing_scraped_data import ProcessingScrapedData
from app.models.import_scraped_data import ImportScrapedData
from app.models.export_scraped_data import ExportScrapedData


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/producao')
def getProducao(db: Session = Depends(get_db)):
    producao_data = db.query(ProductionScrapedData).all()
    if not producao_data:
        return "Sua tabela está vazia, cadastre os dados no banco com o endpoint /scrap/producao", 
    return producao_data

@router.get('/producao/{ano}')
def get_export_data_by_year(ano: int, db: Session = Depends(get_db)):
    producao_data = db.query(ProductionScrapedData).filter(ProductionScrapedData.ano == ano).all()
    return producao_data
    
@router.get('/processamento')
def getProcessamento(db: Session = Depends(get_db)):
    processamento_data = db.query(ProcessingScrapedData).all()
    if not processamento_data:
        return "Sua tabela está vazia, cadastre os dados no banco com o endpoint /scrap/processamento", 
    return processamento_data

@router.get('/processamento/{ano}')
def get_export_data_by_year(ano: int, db: Session = Depends(get_db)):
    processamento_data = db.query(ProcessingScrapedData).filter(ProcessingScrapedData.ano == ano).all()
    return processamento_data

@router.get('/comercializacao')
def getComercializacao(db: Session = Depends(get_db)):
    comercializacao_data = db.query(ComercializationScrapedData).all()
    if not comercializacao_data:
        return "Sua tabela está vazia, cadastre os dados no banco com o endpoint /scrap/comercializacao", 
    return comercializacao_data

@router.get('/comercializacao/{ano}')
def get_export_data_by_year(ano: int, db: Session = Depends(get_db)):
    comercializacao_data = db.query(ComercializationScrapedData).filter(ComercializationScrapedData.ano == ano).all()
    return comercializacao_data

@router.get('/importacao')
def getImportacao(db: Session = Depends(get_db)):
    importacao_data = db.query(ImportScrapedData).all()
    if not importacao_data:
        return "Sua tabela está vazia, cadastre os dados no banco com o endpoint /scrap/importacao", 
    return importacao_data

@router.get('/importacao/{ano}')
def get_export_data_by_year(ano: int, db: Session = Depends(get_db)):
    importacao_data = db.query(ImportScrapedData).filter(ImportScrapedData.ano == ano).all()
    return importacao_data

@router.get('/exportacao')
def getExportacao(db: Session = Depends(get_db)):
    exportacao_data = db.query(ExportScrapedData).all()
    if not exportacao_data:
        return "Sua tabela está vazia, cadastre os dados no banco com o endpoint /scrap/exportacao", 
    return exportacao_data

@router.get('/exportacao/{ano}')
def get_export_data_by_year(ano: int, db: Session = Depends(get_db)):
    export_data = db.query(ExportScrapedData).filter(ExportScrapedData.ano == ano).all()
    return export_data