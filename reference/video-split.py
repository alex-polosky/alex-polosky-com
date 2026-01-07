

OUT = 'out'
IN0 = 'Cleveland Musicians Fundraiser 2023_100,000 Years.mp4'
D0 = '''0:15-0:22
0:44-0:49
4:10-4:34'''
IN1 = "Cleveland Musicians Fundraiser 2023_C'mon And Love Me.mp4"
D1 = '''0:07-0:15
0:20-0:30
0:35-0:41
1:03-1:08
1:24-1:29
1:38-1:48
2:08-2:13
2:32-2:35'''

i = 0
for in_, d in ((IN0, D0), (IN1, D1)):
    for x in d.split('\n'):
        s, e = x.split('-')
        sm, ss = [int(y) for y in s.split(':')]
        em, es = [int(y) for y in e.split(':')]
        seconds = (em*60 + es) - (sm*60 + ss)
        lm = seconds // 60
        ls = seconds % 60
        # Assume no hour long clips
        length = f'00:{lm:02d}:{ls:02d}'
        start = f'00:{sm:02d}:{ss:02d}'
        print(''.join(f'''
ffmpeg -ss {start} -i "{in_}" -t {length}
  -vf "scale=1280:-2"
  -c:v libx264 -crf 28 -preset slow
  -movflags +faststart
  -an
  "{OUT}/{i}.mp4"
'''.split('\n')))
        i += 1
