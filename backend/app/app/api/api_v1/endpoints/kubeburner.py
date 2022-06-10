from typing import Union

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select, col

from app.api.deps import get_session
from app.models.model import KubeBurner


router = APIRouter()


@router.get('/', response_model = list[KubeBurner])
def root(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    uuid: Union[list[str], None] = Query(default=None)
):
    if uuid:
        print(uuid)
        kubeburners = session.exec(
        select(KubeBurner).where(col(KubeBurner.uuid).in_(uuid))).all()
    else:
        kubeburners = session.exec(
            select(KubeBurner).offset(offset).limit(limit)
        ).all()
    return kubeburners


@router.get('/{uuid}', response_model=list[KubeBurner])
def read_kubeburner(
    *,
    session: Session = Depends(get_session),
    uuid: str
):
    kubeburner = session.exec(
        select(KubeBurner).where(KubeBurner.uuid == uuid)
    ).all()
    return kubeburner


