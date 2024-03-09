from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "postgresql://user:password@postgresserver/db"
# "postgresql://test_user:test_password_123@db/verteilte_systeme_db"
SQLALCHEMY_DATABASE_URL = "rqlite+pyrqlite://localhost:4001/"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, )
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
