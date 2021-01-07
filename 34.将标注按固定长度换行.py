def FindLabel(field):
    w=4
    n = len(field) // w
    showlabel = ''
    i = 0
    while i <= n + 1:
        showlabel = showlabel + [名称][i*w:(i+1)*w] + "\n"
        i += 1
    return showlabel