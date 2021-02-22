def FindLabel([HBHD], [HFPQMC]):
    label = str([HBHD])+str([HFPQMC])
    w = 7  # 设置每一行的字符长度
    n = len(label) // w
    showlabel = ''
    i = 0
    while i <= n:
        showlabel = showlabel + label[i*w:(i+1)*w] + "\n"
        i += 1
    return showlabel
