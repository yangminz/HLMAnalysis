f = open('报告.html', 'r').read()

flag = True
l, r = [], []
nf = ''

for i in range(len(f)):
    if f[i] == '$':
        if flag == True:
            nf += '<script type="math/tex">'
        else:
            nf += '</script>'
        flag = not flag
    else:
        nf += f[i]

wf = open('报告.html', 'w')
wf.write(nf)
