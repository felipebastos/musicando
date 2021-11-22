Root.default = 'D'
Scale.default = 'minor'
Clock.bpm = 130

# Batida disco :-)
d0 >> play('~~~~~~~~')
d1 >> play('V V V V ')
d2 >> play('  o   o ')
Group(d0,d1,d2).dur = PDur(4,8)
Group(d0,d1,d2).amp = 0.4
# Palminhas, porque quem tá animado bate palma até mentalmente
c0 >> play('* { [**]} * * ', amp=0.7)
# Baixo
line = P[3,2,4,0]
b0 >> bass(var(line,8), dur=PDur(3,8), oct=4, amp=0.6)
# Gotas circulando :-) pra dar uma sensação de sorrir ao ir pra casa
s0 >> sinepad(
    line,
    amp=0.3,
    pan=linvar([-1,0,1,0])
    ).every(4, 'stutter') + (0,2,6)
# Sirenes distantes
line2 = P[3,7]
s1 >> razz(line2, amp=0.05, pan=linvar([-1,0,1]))

