from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_URL =  "postgresql://review@localhost/review"


engine = create_engine(
    "postgresql://review@localhost/review",
    connect_args={
        "check_same_thred": False
    }
        
)

session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)