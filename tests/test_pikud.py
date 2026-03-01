import json

from pikud_haoref_bulb.requester import Requester
from pikud_haoref_bulb.types import PikudEntry


def test_entry_datatype(samplefile):
    data = json.load(open(samplefile))
    entries = [PikudEntry.from_dict(d) for d in data]
    for e in entries:
        assert e.data.find("נתניה") != -1


async def test_fetch_and_format():
    status: list = []
    r = Requester(status)
    data = await r.get_current("נתניה - מזרח")
    entries = [PikudEntry.from_dict(d) for d in data]
    for e in entries:
        assert e.data.find("נתניה") != -1
