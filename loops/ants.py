"""Ants - Composição de som ambiente.
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

Root.default = "E"
Scale.default = "minorPentatonic"
Clock.bpm = 112

b0 >> play("[VV]-o-")
b1 >> play("[**]* (* )")

line = P[0, 2, 4, 3]
i0 >> bass(var(line, 4), dur=PDur(3, 8))
i1 >> arpy(i0.pitch) + [(0, 2, 4), (0, 2, 6), (0, 2, 4), (0, 2, 4)]

solo = P[0, 2, 3, 4, 5, 6]
s0 >> viola(solo[0:6], dur=var([1 / 4, 1]))
