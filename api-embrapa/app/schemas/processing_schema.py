from pydantic import BaseModel

class ProcessingScrapedDataBase(BaseModel):
    cultivo: str
    quantidade: str
    ano: int
    classificacao_uva:str

class ScrapedDataCreate(ProcessingScrapedDataBase):
    pass

class ScrapedData(ProcessingScrapedDataBase):
    id: int

    class Config:
        from_attributes = True 