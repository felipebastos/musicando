"""Tempos - Composição de som ambiente.
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
    jbass,
    play,
    Go,
    var,
    viola,
)

Root.default = "G"
Scale.default = "minor"
Clock.bpm = 120

p0 = Player("p0")
p0 >> play("V-V-V-V(x~)V~V~V~V(x-)", amp=0.4)

line1 = P[0, 3, 6, 4]
b0 = Player("jbass")
b0 >> jbass(var(line1, 3), dur=s0.dur, oct=4, amp=0.5)
s0 = Player("zap")
s0 >> zap(var(line1, 3), oct=6, dur=[1 / 2, 1 / 4, 1 / 2], amp=0.3).every(
    5, "stutter"
) + [(0, 2, 4), (0, 2, 5), (0, 2, 4)]

s1 = Player("viola")
s1 >> viola(var(line1, 3), dur=s0.dur, amp=0.4) + [
    (0, 2, 4),
    (0, 2, 3),
    (0, 2, 4),
]


# print(SynthDefs)

Go()
