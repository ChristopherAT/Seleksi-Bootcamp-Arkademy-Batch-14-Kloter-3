import re
def printer(teks,*argv):
    # Ambil {a} {b} {c} dari teks dengan regex:
    list_posisi = re.findall(r'\{([0-9]+)\}',teks)
    teks = re.match(r'^(.*?)\{',teks).group(1)
    for pos in list_posisi:
        teks+=argv[int(pos)] + ' '
    return teks

