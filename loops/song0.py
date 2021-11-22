'''Song0 - Experimentos com FoxDot
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

Root.default = 'D'
Scale.default = 'minor'
s0 >> play('[VV]-o[----]')
sc >> play('[**]( *)')
s1 >> sawbass(
    var([0,2,5,4],4),
    )
s2 >> ambi(
    [0,2,5,4],
    oct=5,
    amp=0.3
    )

