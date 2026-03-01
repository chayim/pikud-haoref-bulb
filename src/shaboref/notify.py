from __future__ import annotations

from shaboref.types import PikudEntry, PikudState


class Notify:
    _last_state = PikudEntry

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
                self.orange()
            case _:
                self.white()
        self._last_state = status

    def _colourize(self, hex_code: str, seconds: int = 10) -> None:
        # TODO: implement colourize logic
        pass

    def red(self, seconds: int = 10) -> None:
        self._colourize("#FF0000", seconds)

    def yellow(self, seconds: int = 10) -> None:
        self._colourize("#FFFF00", seconds)

    def green(self, seconds: int = 10) -> None:
        self._colourize("#00FF00", seconds)

    def orange(self, seconds: int = 10) -> None:
        self._colourize("#FFA500", seconds)

    def white(self, seconds: int = 10) -> None:
        self._colourize("#FFFFFF", seconds)
