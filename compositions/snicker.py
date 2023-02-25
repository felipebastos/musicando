"""Snicker - Composição de som ambiente.
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
    bass,
    play,
    Go,
    snick,
    var,
    blip,
)

Root.default = "E"
Scale.default = "major"
Clock.bpm = 120
p0 = Player("p0")
p0 >> play("X-o[---]", amp=0.4)
line1 = P[0, 0, 2, 4]
b0 = Player("bass")
b0 >> bass(var(line1, 3), dur=[1 / 2, 1 / 4, 1 / 4, 1 / 2], oct=4, amp=0.6)
s = Player("snick")
s0 >> snick(b0.pitch, dur=b0.dur, amp=0.4).every(5, "stutter").every(7, "stutter") + (
    0,
    2,
    4,
)
s1 = Player("blip")
s1 >> blip(b0.pitch + P[(2, 4), (2, 5), (2, 6), (2, 4)], dur=b0.dur, oct=3, amp=0.3)

Go()
