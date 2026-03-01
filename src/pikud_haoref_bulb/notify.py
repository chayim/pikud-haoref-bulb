from __future__ import annotations

from pikud_haoref_bulb.types import PikudEntry, PikudState
from yeelight import Bulb


class Notify:
    _last_state = PikudEntry
    _bulbs: list[str] = []

    def __init__(self, bulbs: list[str]):
        self.bulbs = bulbs

    def notify(self, status: PikudEntry) -> None:
        if self._last_state.rid == status.rid:
            return

        match self._last_state.category:
            case PikudState.LEAVE_THE_MAMAD:
                self.green()
            case PikudState.EARLY_WARNING:
                self.yellow()
            case PikudState.ROCKETS:
                self.red()
            case PikudState.NO_INTERNET:
                self.blue()
            case _:
                self.white()
        self._last_state = status

    def _colourize(self, rgb_code: tuple, times: int = 10) -> None:
        for _b in self.bulbs:
            c = 0
            b = Bulb(_b)
            while c < times:
                b.turn_on()
                b.set_brightness(100)
                b.set_rgb(rgb_code)
                b.turn_off()
                c += 1
            b.turn_off()

    def red(self, times: int = 10) -> None:
        self._colourize((255, 0, 0), times)

    def yellow(self, times: int = 10) -> None:
        self._colourize((255, 255, 0), times)

    def green(self, times: int = 10) -> None:
        self._colourize((0, 255, 0), times)

    def blue(self, times: int = 10) -> None:
        self._colourize((0, 0, 255), times)

    def white(self, times: int = 10) -> None:
        self._colourize((255, 255, 255), times)
