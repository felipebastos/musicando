Clock.bpm = 120

# Dicionário das peças
# bg-hihat
b0 >> play('a')

# dist kick
b0 >> play('A')

# conga
b0 >> play('c')

# wood
b0 >> play('d')

# alt snare
b0 >> play('D')

# snap
b0 >> play('h')

# clap
b0 >> play('H')

# Jungle snare
b0 >> play('i')

# Rock snare
b0 >> play('I')

# tom
b0 >> play('m')

b0 >> play('M')

# Closed hat
b0 >> play('n')

# Open hat
b0 >> play('N')

# Snare drum
b0 >> play('o')

# Tamborine
b0 >> play('S')

# Alt rimshot
b0 >> play('t')

# Metal cowbell
b0 >> play('T')

# soft snare
b0 >> play('u')

# Low bass
b0 >> play('v')

# Heavy
b0 >> play('V')

# Kick drum
b0 >> play('x')

b0 >> play('X')

# Triangle
b0 >> play('&')

# clap
b0 >> play('*')

# bb kick
b0 >> play('$')

# hihat open
b0 >> play('=')

# Hihat closed
b0 >> play('-')

# Ride cymbal
b0 >> play('~')

# Estudo de batidas

Clock.bpm = 140

# Straight 8th Note Groove
b0 >> play('-------', dur=1/2)
b1 >> play('X o X o ', dur=b0.dur)

# Four on the floor
b0 >> play('V ')

# 16th note beat
b0 >> play('---- ---')
b1 >> play('X   o   ')

# Disco beat
b0 >> play('~~~~~~~~')
b1 >> play('X X X X ')
b2 >> play('  o   o ')

# Bossa Nova
b0 >> play('----------------')
b1 >> play('n  n  n   n  n  ')
b2 >> play('x  xx  xx  xx  x')

# Basic swing
b0 >> play('------', dur=PDur(4,6))
b1 >> play(' :  : ', dur=b0.dur)

# Train beat
b0 >> play('oooo', dur=1/2)
b1 >> play('X   ', dur=b0.dur)

# Motown
b0 >> play('--------', dur=1/2)
b1 >> play('o o o o ', dur=b0.dur)
b2 >> play('v    v v', dur=b0.dur)

# Half Time Shuffle
Clock.bpm = 80
b0 >> play('[- -][- -][- -][- -]')
b1 >> play('[   ][   ][ o ][   ]')
b2 >> play('[x  ][   ][   ][   ]')

# Samba
Clock.bpm = 180
b0 >> play('uuuuuuuuuuuuuuuu', dur=PDur(4,16))
b1 >> play('x  xx  xx  xx  x', dur=b0.dur)
b2 >> play('  -   -   -   - ', dur=b0.dur)

# Reggae One Drop
Clock.bpm = 65
b0 >> play('----', dur=PDur(4,4))
b1 >> play('  n ', dur=b0.dur)
b2 >> play('  x ', dur=b0.dur)

# Soca
Clock.bpm = 100
b0 >> play('-- ---- --', dur=[1/2,1/4,1/4,1/2,1/2,1/2,1/4,1/4,1/2,1/2])
b1 >> play('  o o  o o', dur=b0.dur)
b2 >> play('v  v v  v ', dur=b0.dur)

# Heavy rock
Clock.bpm = 120
b0 >> play('---- - ----', dur=[1/2,1/2,1/2,1/4,1/4,1/4,1/4,1/4,1/4,1/2,1/2])
b1 >> play('x o o o xo ', dur=b0.dur)

# Shuffle Groove
b0 >> play('~ ~~ ~', dur=PDur(2,4))
b1 >> play('X  o  ', dur=b0.dur)
