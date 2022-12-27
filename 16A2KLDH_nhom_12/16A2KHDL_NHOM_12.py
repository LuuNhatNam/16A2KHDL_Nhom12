''' NHÓM 12:
1.Lưu Nhật Nam
2.Lê Tuấn Thành 
3.Đào Xuân Tâm
4.Nguyễn Thị Thanh Hằng
'''


import os,csv
import libs.xu_li_ds_hs
_path="files/ds_hs.csv"
lsths=[]


#Bắt đầu chương trình
print("CT QUẢN LÝ HỌC SINH")
while True:
    print('1: Mở file danh sách học sinh')
    print('2: Thêm thông tin học sinh mới')
    print('3: In danh sách học sinh đầy đủ')
    print('4: Lưu danh sách học sinh')
    print('5: Tìm học sinh trong danh sách')
    print('6: xóa danh sách học sinh')
    print('7: Sắp xếp học sinh,sv theo điểm tb có thứ tự giảm dần')
    
    cn=int(input('Chọn chức năng cần thực hiện: '))
    if cn==1:
        libs.xu_li_ds_hs.mofile(lsths)
    elif cn==2:
        libs.xu_li_ds_hs.themhs(lsths)
    elif cn==3:
        libs.xu_li_ds_hs.inhs(lsths)
    elif cn==4:
        libs.xu_li_ds_hs.luuhs(_path,lsths)
    elif cn==5:
        f=int(input('Nhập mã sv cần tra cứu: '))
        hs=libs.xu_li_ds_hs.timhs(lsths,f)
        if hs==None:
            print('không tìm thấy học sinh')
        else:
            print(hs)
    elif cn==6:
        masv=int(input('Nhập msv của sv cần xóa: '))
        kt=input('Bạn có chắc chắn muốn xóa sinh viên này ra khỏi danh sách? (c/C hay k/K): ')
        if kt=='c'or kt=='C':
            kq=libs.xu_li_ds_hs.xoahs(lsths,masv)
            if kq==1:
                print('Đã xóa hs có số mã sv: ',masv)
            else:
                print('Không tồn tại mã sinh viên này')
    elif cn==7:
        print("danh sách trước khi sắp xếp hs,sv theo dtb:",libs.xu_li_ds_hs.inhs(lsths))
        print("Danh sách hs,sv sau khi sắp xếp giảm dần theo dtb: \n")
        libs.xu_li_ds_hs.sapxephs(lsths)
        print('{:>12}{:>12}{:>16}{:>18}{:>18}{:>18}{:>25}'.format('msv','ths','dt','dl','dh','dtb','xl'))
        for hs in libs.xu_li_ds_hs.sapxephs(lsths):
            print('{:>12}{:>12}{:>16}{:>18}{:>18}{:>18}{:>25}'.format(hs['msv'],hs['ths'],hs['dt'],hs['dl'],hs['dh'],hs['dtb'],hs['xl']))
    else:
        break
    
    tieptuc=int(input("Bạn có muốn tiếp tục ct? (1:tt): "))
    if tieptuc!=1:
        break
    else:
        os.system('cls')
    input('Gõ 1 phím bất khì để tiếp tuc ct \n')
