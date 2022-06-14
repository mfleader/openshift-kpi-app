from webbrowser import get
import sqlmodel as sqm

from app.models.model import KubeBurner
import app.services.rdbms as rdbms
import simdata


def create_table_data(ngn):
    sqm.SQLModel.metadata.create_all(ngn)
    with sqm.Session(ngn) as session:
        for d in simdata.data:
            session.add(KubeBurner(**d))
        session.commit()


def main():
    sqm.SQLModel.metadata.create_all(rdbms.engine)
    with sqm.Session(rdbms.engine) as session:
        for d in simdata.data:
            session.add(KubeBurner(**d))
            session.commit()


if __name__ == '__main__':
    main()