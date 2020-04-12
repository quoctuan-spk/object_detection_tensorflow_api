# xoa cai cu luu cai moi lai

file1=open("demofile1.txt",'w')    # file = open("demofile.txt",'w',encoding='utf_8') - cho tieng viet co dau
file1.writelines("16146222; Tran Quoc Tuan")
file1.close()

# luu noi duoi
file2=open("demofile2.txt",'a')
file2.writelines("""
16146221; Nguyen Minh Tuan
16146222; Tran Duy Tuan
16146222; HaHa
""")
file2.close

f=open("hjhj.txt","w")
f.close
