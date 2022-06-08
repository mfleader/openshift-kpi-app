import datetime
from datetime import timedelta
from datetime import tzinfo
import pytz

from fastapi import APIRouter


router = APIRouter()


class EST(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours = -5)

    def tzname(self, dt):
        return "EST"

    def dst(self, dt):
        return timedelta(0)


@router.get("/")
async def root():
    return {
        'corporation': 'Red Hat',
        'organization': 'OpenShift Performance and Scale',
        'time': datetime.datetime.now(pytz.timezone('US/Eastern'))
    }