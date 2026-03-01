import asyncio
from typing import Any

import click
from loguru import logger

from shaboref.notify import Notify
from shaboref.requester import Requester


async def _poll_loop(requester: Requester, zone: str, delay: int) -> None:
    while True:
        await requester.get_current(zone=zone)
        await asyncio.sleep(delay)


async def _status_loop(status: list[Any], notify: Notify) -> None:
    while True:
        if status:
            latest = status[-1]
            notify.notify(latest)
        await asyncio.sleep(1)


async def _async_main(zone: str, delay: int) -> None:
    logger.info("starting shaboref")
    status: list[Any] = []
    requester = Requester(status)
    notify = Notify()
    await asyncio.gather(
        _poll_loop(requester, zone, delay),
        _status_loop(status, notify),
    )


@click.command()
@click.option("--city", envvar="PIKUD_HAOREF_ZONE", required=True, help="pikud haoref zone to monitor")
@click.option("--delay", envvar="POLLING_SECONDS", default=60, type=int, help="polling interval (seconds) for pikud haoref api")
def main(city: str, delay: int) -> None:
    asyncio.run(_async_main(city, delay))


if __name__ == "__main__":
    main()
