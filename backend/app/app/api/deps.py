from sqlmodel import Session

import app.services.rdbms as rdbms


def get_session():
    with Session(rdbms.engine) as session:
        yield session
