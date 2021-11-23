Root.default = "F"
Scale.default = 'minor'
Clock.bpm = 112
line1 = P[0,0,2,6,4,3,0,3,5,4,5,6,5]
b0 >> bass(line1, dur=[1,1/2,1/2,1/2,1,1,1/2,1/2,1,1/2,1/4,1/2,1/4], oct=4, amp=0.6)
s0 >> sinepad(b0.pitch, dur=b0.dur, amp=0.4).every(3, 'offadd', -2).every(5, 'stutter').every(7, 'stutter') + (0,2,4)
def linha_de_percursao(n=0):
    mao1 = ''
    mao2 = ''
    pe1 = ''
    pe2 = ''
    if n < 5:
        mao1 = '----------------'
        mao2 = ''
        pe1 = 't  t  t   t  t  '
        pe2 = 'xxxxxxxx'
    elif n < 10:
        mao1 = '---~-------~-~-'
        mao2 = ''
        pe1 = 't o  t   o  [ttt]  o'
        pe2 = 'xxxxxxxx'
    else:
        Clock.future(1, linha_de_percursao, args=(0,))
        return
    p0 >> play(mao1, dur=PDur(4,9))
    p1 >> play(pe1, dur=p0.dur)
    p2 >> play(pe2, dur=[1.5,1/2, 1.5, 1/2, 1.5, 1/2, 1.5, 1/2])
    Group(p0,p1,p2).amp = 1
    Clock.future(1, linha_de_percursao, args=(n+1,))
linha_de_percursao()
