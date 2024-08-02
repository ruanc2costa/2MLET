from pydantic import BaseModel

class ProductionScrapedDataBase(BaseModel):
    title: str
    year: int
    quantity: str

class ScrapedDataCreate(ProductionScrapedDataBase):
    pass

class ScrapedData(ProductionScrapedDataBase):
    id: int

    class Config:
        from_attributes = True 