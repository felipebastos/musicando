Root.default = "B"
Scale.default = 'locrian'
Clock.bpm = 112


# Bossa nova :-)
mao1 = '----------------'
mao2 = ''
pe1 = 't  t  t   t  t  '
pe2 = 'xxxxxxxx'

p0 >> play(mao1, dur=1/2)
p1 >> play(pe1, dur=p0.dur)
p2 >> play(pe2, dur=[1.5,1/2, 1.5, 1/2, 1.5, 1/2, 1.5, 1/2])
Group(p0,p1,p2).amp = 1

line1 = P[0,6,2,2,6,5]
b0 >> bass(var(line1, 8), oct=3).every(1, 'offadd', 4)

v0 >> keys(var(line1, 8)) + [(0,2,6),(0,2,4,8),(0,2,6),(0,2,4,6,8,10),(0,2,4),(0,2,6)]

