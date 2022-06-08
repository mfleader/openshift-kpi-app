from typing import List

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select

from app.api.deps import get_session
from app.models.model import KubeBurner


router = APIRouter()


@router.get('/',
    response_model = List[KubeBurner]
    )
def root(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100)
):
    kubeburners = session.exec(
            select(KubeBurner).offset(offset).limit(limit)).all()

    return kubeburners