from sqlalchemy import Column, Integer, String, create_engine, insert
from sqlalchemy.orm import Session, declarative_base, declared_attr
import requests
from bs4 import BeautifulSoup

PEP_URL = 'https://peps.python.org/'


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Pep(Base):
    type_status = Column(String(2))
    number = Column(Integer, unique=True)
    title = Column(String(200))
    authors = Column(String(200))

    def __repr__(self):
        return f'PEP {self.number} {self.title}'


engine = create_engine('sqlite:///sqlite-peps.db')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
session = Session(engine)

response = requests.get(PEP_URL)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, features='lxml')

section = soup.find('section', attrs={'id': 'numerical-index'})
tbody = section.find('tbody')
pep_rows = tbody.find_all('tr')

for row in pep_rows:
    tds = row.find_all('td')
    td_val = list(map(lambda td: td.text, tds))
    type_status, number, title, authors = td_val

    session.execute(
        insert(Pep).values(
            type_status=type_status,
            number=number,
            title=title,
            authors=authors,)
    )

session.commit()
