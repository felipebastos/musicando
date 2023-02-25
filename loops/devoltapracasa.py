"""De Volta pra Casa - Experimentos com FoxDot
    Copyright (C) 2021  Felipe Bastos Nunes

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from FoxDot import (
    Root,
    Scale,
    Clock,
    Player,
    P,
    PDur,
    Group,
    bass,
    play,
    Go,
    var,
    linvar,
    sinepad,
    razz,
)

Root.default = "D"
Scale.default = "minor"
Clock.bpm = 130

# Batida disco :-)
d0 = Player("d0")
d0 >> play("~~~~~~~~")
d1 = Player("d1")
d1 >> play("V V V V ")
d2 = Player("d2")
d2 >> play("  o   o ")
Group(d0, d1, d2).dur = PDur(4, 8)
Group(d0, d1, d2).amp = 0.4
# Palminhas, porque quem tá animado bate palma até mentalmente
c0 = Player("c0")
c0 >> play("* { [**]} * * ", amp=0.7)
# Baixo
line = P[3, 2, 4, 0]
b0 = Player("bass")
b0 >> bass(var(line, 8), dur=PDur(3, 8), oct=4, amp=0.6)
# Gotas circulando :-) pra dar uma sensação de sorrir ao ir pra casa
s0 = Player("sinepad")
s0 >> sinepad(line, amp=0.3, pan=linvar([-1, 0, 1, 0])).every(4, "stutter") + (
    0,
    2,
    6,
)
# Sirenes distantes
line2 = P[3, 7]
s1 = Player("razz")
s1 >> razz(line2, amp=0.05, pan=linvar([-1, 0, 1]))

Go()
