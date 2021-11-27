Root.default = "E"
Scale.default = 'major'
Clock.bpm = 120
p0 >> play('X-o[---]', amp=0.4)
line1 = P[0,0,2,4]
b0 >> bass(var(line1,3), dur=[1/2,1/4,1/4,1/2], oct=4, amp=0.6)
s0 >> snick(b0.pitch, dur=b0.dur, amp=0.4).every(5, 'stutter').every(7, 'stutter') + (0,2,4)
s1 >> blip(b0.pitch + P[(2,4),(2,5),(2,6),(2,4)], dur=b0.dur, oct=3, amp=0.3)

