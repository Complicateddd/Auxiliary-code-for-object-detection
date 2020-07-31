import os
import shutil
file=open("/media/ubuntu/新加卷/xiangmu/dataset/ImageSets/Main/test.txt",'r')
list_=[]
for line in file.readlines():
	list_.append(line.strip()+'.jpg')
	print(line)
print(list_)
img=os.listdir("/media/ubuntu/新加卷/xiangmu/dataset/JPEGImages")
print(len(img))
for i in img:
	if i in list_:
		shutil.copy(os.path.join("/media/ubuntu/新加卷/xiangmu/dataset/JPEGImages",i),
			os.path.join("/media/ubuntu/新加卷/xiangmu/sample",i))
file.close()