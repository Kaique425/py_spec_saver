import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine(
    'mysql+mysqldb://kaique:KSunimed197@localhost/pc_spec', echo=True)

sessionmaker()

connection = engine.connect(

)
