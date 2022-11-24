# from itemadapter import ItemAdapter
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, declarative_base, declared_attr


class Base:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)

Base = declarative_base(cls=Base)

class Quote(Base):
    author = Column(String(200))
    text = Column(Text())
    tags = Column(String(400))

    def __repr__(self):
        return f'QUOTE {self.author} {self.text[:15]}'


class QuotesToDBPipeline:

    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqlite.db')
        Base.metadata.create_all(engine)
        self.session = Session(engine) 

    def process_item(self, item, spider):
        quote = Quote(
            text=item['text'],
            author=item['author'],
            tags=', '.join(item['tags']),
        )
        self.session.add(quote)
        self.session.commit()
        return item

    def close_spider(self, spider):
        self.session.close()
