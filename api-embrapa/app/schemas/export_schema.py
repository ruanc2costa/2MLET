from pydantic import BaseModel

class ExportationScrapedDataBase(BaseModel):
    paises: str
    quantidade:str
    valor: str
    ano: int
    classificacao_derivado: str

class ScrapedDataCreate(ExportationScrapedDataBase):
    pass

class ScrapedData(ExportationScrapedDataBase):
    id: int

    class Config:
        from_attributes = True 