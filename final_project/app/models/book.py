from pydantic import BaseModel


class BookModel(BaseModel):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"

# db -> collection -> documnet
