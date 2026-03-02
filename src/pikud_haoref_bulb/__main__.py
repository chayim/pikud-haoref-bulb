import asyncio
from typing import Any

import click
from loguru import logger
from pikud_haoref_bulb.notify import Notify
from pikud_haoref_bulb.requester import Requester
from pikud_haoref_bulb.types import PikudEntry


async def _poll_loop(requester: Requester, zone: str, delay: int) -> None:
    while True:
        await requester.get_current(zone=zone)
        await asyncio.sleep(delay)


async def _status_loop(status: list[Any], notify: Notify) -> None:
    while True:
        if status:
            latest = status[-1]
            notify.notify(latest)
        else:
            notify.notify(PikudEntry.no_alerts())
        await asyncio.sleep(1)


async def _async_main(zone: str, delay: int, bulbs: str) -> None:
    logger.info("starting pikud_haoref_bulb")
    status: list[Any] = []
    requester = Requester(status)
    notify = Notify(bulbs.split(","))
    await asyncio.gather(
        _poll_loop(requester, zone, delay),
        _status_loop(status, notify),
    )


@click.command()
@click.option("--city", envvar="PIKUD_HAOREF_ZONE", required=True, help="pikud haoref zone to monitor")
@click.option(
    "--delay", envvar="POLLING_SECONDS", default=90, type=int, help="polling interval (seconds) for pikud haoref api"
)
@click.option("--bulbs", envvar="BULB_IPS", type=str, required=True, help="comma separated list of yeelight bulb IPs")
def main(city: str, delay: int, bulbs: str) -> None:
    asyncio.run(_async_main(city, delay, bulbs))


if __name__ == "__main__":
    main()
