from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "postgresql://test_user:test_password_123@localhost/verteilte_systeme_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
