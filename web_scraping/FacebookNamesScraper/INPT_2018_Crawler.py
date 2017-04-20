import re


def creat_data_base(html_file):
    file = open(html_file,"r")
    s = file.read()
    regX = r'<div class="fsl fwb fcb">.*?</div>'
    for elem in re.findall(regX, s):
        print(re.findall(r'<a.*>(.*)</a>',elem)[0])
page = "INPT Promo 2018.html"

creat_data_base(page)


## python scripting
