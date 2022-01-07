from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db = SQLAlchemy()
Session = sessionmaker()
Base = declarative_base()

# ---------------------- Application Initiation ----------------------
def create_app(test: bool = False):
    app = Flask(__name__, instance_relative_config=False)
    if test:
        app.config.from_object("config.TestConfig")
        test_db = Path(app.config['SQLALCHEMY_DATABASE_URI'])
        if test_db.exists():
            test_db.unlink()
        app.config['SQLALCHEMY_DATABASE_URI']
    else:
        app.config.from_object("config.LocalConfig")
    
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    Session.configure(bind=engine)

    with app.app_context():
        # Import routes
        from application.api import Item
        # Create database tables for our data models
        Base.metadata.create_all(engine)
        return app
