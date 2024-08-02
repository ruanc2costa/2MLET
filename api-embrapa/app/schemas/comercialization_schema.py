from pydantic import BaseModel

class ComercializationScrapedDataBase(BaseModel):
    produto: str
    ano: int
    quantidade: str

class ScrapedDataCreate(ComercializationScrapedDataBase):
    pass

class ScrapedData(ComercializationScrapedDataBase):
    id: int

    class Config:
        from_attributes = True 