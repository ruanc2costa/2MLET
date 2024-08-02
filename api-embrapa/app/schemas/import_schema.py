from pydantic import BaseModel

class ImportScrapedDataBase(BaseModel):
    paises: str
    quantidade:str
    valor: str
    ano: int
    classificacao_derivado: str

class ScrapedDataCreate(ImportScrapedDataBase):
    pass

class ScrapedData(ImportScrapedDataBase):
    id: int

    class Config:
        from_attributes = True 