import csv
#Mở file
def mofile(_path,lsths):
    file = open("ds_hs.csv",'w') 
    file.write

#thêm hs
def themhs(lsths):
    while True:
        msv=int(input("Nhập mã sv: "))
        ths=str(input("Nhập tên hs: "))
        dt=int(input("Nhập điểm toán: "))
        dl=int(input("Nhập điểm lý: "))
        dh=int(input("Nhập điểm hóa: "))
        dtb=(dt+dl+dh)/3
        print("Điểm trung bình: ",dtb)
        if dtb>=9:
            print("Xếp loại: Xuất sắc")
            xl="Xuất sắc"
        elif dtb>=8:
            print("xếp loại: Giỏi")
            xl="Giỏi"
        elif dtb>=7:
            print("Xếp loại: Khá")
            xl="Khá"
        elif dtb>=5:
            print("Xếp loại: Trung bình")
            xl="Trung bình"
        elif dtb<5:
            print("Xếp loại: Yếu")
            xl="Yếu"
        lsths.append({'msv':msv,'ths':ths,'dt':dt,'dl':dl,'dh':dh,'dtb':dtb,'xl':xl})
        tt=input("Bạn có muốn tiếp tục? (1: c; 2: k): ")
        if tt!='1':
            break
    return
#in ds hs
def inhs(lsths):
    print('{:12}{:12}{:18}{:18}{:18}{:18}{:18}'.format('msv','ths','dt','dl','dh','dtb','xl'))
    for hs in lsths:
        print('{:12}{:12}{:18}{:18}{:20}{:18}{:18}'.format(hs['msv'],hs['ths'],hs['dt'],hs['dl'],hs['dh'],hs['dtb'],hs['xl']))
    return
#tìm hs
def timhs(lsths,f):
    for hs in lsths:
        if hs['msv']==f:
            return hs
    return
#xóa ds hs
def xoahs(lsths,masv):
    for i in range(len(lsths)):
        hs=lsths[i]
        if hs['msv']==masv:
            del(lsths[i])
            return 1
    return 0
#lưu ds hs
def luuhs(_path,lsths):
    try:
        f=open(_path,'w',newline='',encoding = 'utf-8')
        csv.writer(f).writerow(['msv','ths','dt','dl','dh','dtb','xl'])
        for hs in lsths:
            csv.writer(f).writerow([hs['msv'],hs['ths'],hs['dt'],hs['dl'],hs['dh'],hs['dtb'],hs['xl']])
        f.close()
        return 1
    except Exception as ex1:
        return 0

