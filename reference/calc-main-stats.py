
DATA = '''0.3
363 x 1210
top: 245
rest: 965

0.4
472 x 1180
top: 285
rest: 895

0.5
575 x 1150
top: 341
rest: 809

0.6
672 x 1120
top: 407
rest: 713

0.7
763 x 1090
top: 260
rest: 830

0.8
848 x 1060
top: 286
rest: 774

0.9
927 x 1030
top: 312
rest: 718

1.0
1000 x 1000
top: 339
rest: 661

1.1
1067 x 970
top: 361
rest: 609

1.2
1128 x 940
top: 382
rest: 558

1.3
1183 x 910
top: 399
rest: 511

1.4
1232 x 880
top: 416
rest: 464

1.5
1275 x 850
top: 432
rest: 418

1.6
1312 x 820
top: 444
rest: 376

1.7
1343 x 790
top: 453
rest: 337

1.8
1368 x 760
top: 463
rest: 297

1.9
1387 x 730
top: 469
rest: 261

2
1400 x 700
top: 474
rest: 226

2.1
1407 x 670
top: 476
rest: 224'''

headers = 'asp', 'width', 'height', 'top', 'space', 'top h%', 'spa h%', 'top w%', 'spa w%'
print('\t'.join(headers))

for entry in DATA.split('\n\n'):
    aspect, wh, t, r = entry.split('\n')
    width, height = wh.split(' x ')
    _, top = t.split(' ')
    _, space = r.split(' ')

    aspect = float(aspect)
    width = int(width)
    height = int(height)
    top = int(top)
    space = int(space)

    top_h_per = top / height
    space_h_per = space / height

    top_w_per = top / width
    space_w_per = space / width

    print(
        f'{aspect:1.1f}\t{width:4d}\t{height:4d}\t{top:3d}\t{space:3d}\t'
        f'{top_h_per:0.2f}\t{space_h_per:0.2f}\t{top_w_per:0.2f}\t{space_w_per:0.2f}\t'
    )
