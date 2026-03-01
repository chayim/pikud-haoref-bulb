import httpx
from loguru import logger

from shaboref.types import PikudEntry


class Requester:
    def __init__(self, status: list) -> None:
        self._status = status

    _baseurl_ = "https://alerts-history.oref.org.il/Shared/Ajax/GetAlarmsHistory.aspx"

    _headers_ = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:147.0) Gecko/20100101 Firefox/147.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "X-Requested-With": "XMLHttpRequest",
        "DNT": "1",
        "Sec-GPC": "1",
    }

    async def get_current(self, city: str, lang: str = "he", mode: int = 1, timeout: float = 60.0):

        p = {"lang": lang, "mode": mode, "city_0": city}
        try:
            with httpx.Client(
                headers=self._headers_,
                timeout=timeout,
                http2=True,
            ) as client:
                response = client.get(self._baseurl_, params=p)
                logger.info(response.json())
                response.raise_for_status()

                self._status = response.json()
                return self._status
        except (httpx.HTTPError, httpx.StreamError) as exc:
            logger.warning(f"Request failed: {exc}")
            entry = PikudEntry.no_internet()
            self._status.clear()
            self._status.append(entry)
            return self._status
