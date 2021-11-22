'''Aqua - Composição de som ambiente.
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
'''

Root.default = 'A'
Scale.default = 'minor'
Clock.bpm = 95

b0 >> play(' X')
b1 >> play('x-o-')
b2 >> play('[VV] ')
x1 >> play('** (* )')
p1 >> bass(var([0,5,6,2], 4), dur=PDur(3,8))
p2 >> ambi(p1.pitch, amp=0.6)
p3 >> keys(p1.pitch) + [(0,2,4), (0,2,6), (0,2,5), (0,2,4)]

