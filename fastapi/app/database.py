from sqlmodel import SQLModel

sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(url=sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)