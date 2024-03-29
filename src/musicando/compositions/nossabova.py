"""Nossa Bova - Composição de som ambiente.
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
    sinepad,
    Go,
)

Root.default = "F"
Scale.default = "minor"
Clock.bpm = 112

line1 = P[0, 0, 2, 6, 4, 3, 0, 3, 5, 4, 5, 6, 5]

b0 = Player("bass")

b0 >> bass(
    line1,
    dur=[
        1,
        1 / 2,
        1 / 2,
        1 / 2,
        1,
        1,
        1 / 2,
        1 / 2,
        1,
        1 / 2,
        1 / 4,
        1 / 2,
        1 / 4,
    ],
    oct=4,
    amp=0.6,
)

s0 = Player("sinepad")

s0 >> sinepad(b0.pitch, dur=b0.dur, amp=0.4).every(3, "offadd", -2).every(
    5, "stutter"
).every(7, "stutter") + (0, 2, 4)


def linha_de_percursao(time=0):
    """Percursão que varia no tempo."""
    mao1 = ""
    pe1 = ""
    pe2 = ""
    if time < 5:
        mao1 = "----------------"
        pe1 = "t  t  t   t  t  "
        pe2 = "xxxxxxxx"
    elif time < 10:
        mao1 = "---~-------~-~-"
        pe1 = "t o  t   o  [ttt]  o"
        pe2 = "xxxxxxxx"
    else:
        Clock.future(1, linha_de_percursao, args=(0,))
        return
    p0 = Player("p0")
    p0 >> play(mao1, dur=PDur(4, 9))
    p1 = Player("p1")
    p1 >> play(pe1, dur=p0.dur)
    p2 = Player("p2")
    p2 >> play(pe2, dur=[1.5, 1 / 2, 1.5, 1 / 2, 1.5, 1 / 2, 1.5, 1 / 2])

    Group(p0, p1, p2).amp = 1
    Clock.future(1, linha_de_percursao, args=(time + 1,))


linha_de_percursao()

Go()
