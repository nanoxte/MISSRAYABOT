from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from .config import Config

Base = declarative_base()

class StreamHistory(Base):
    __tablename__ = 'stream_history'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    quality = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Database:
    def __init__(self):
        self.engine = create_engine(Config.DB_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def add_stream(self, title, url, quality):
        session = self.Session()
        try:
            stream = StreamHistory(
                title=title,
                url=url,
                quality=quality
            )
            session.add(stream)
            session.commit()
        finally:
            session.close()
