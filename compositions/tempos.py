Root.default = 'G'
Scale.default = 'minor'
Clock.bpm = 120
p0 >> play('V-V-V-V(x~)V~V~V~V(x-)')

line1 = P[0,3,6,4]
b0 >> jbass(var(line1,3), dur=s0.dur, oct=4)
s0 >> zap(var(line1,3), oct=6, dur=[1/2,1/4,1/2]).every(5, 'stutter') + [(0,2,4),(0,2,5),(0,2,4)]

s1 >> 


print(SynthDefs)
