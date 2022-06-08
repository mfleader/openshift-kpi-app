import datetime
import pytz

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def root():
    return {
        'corporation': 'Red Hat',
        'organization': 'OpenShift Performance and Scale',
        'time': datetime.datetime.now(pytz.timezone('US/Eastern'))
    }