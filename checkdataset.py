import xml.etree.ElementTree as ET
import os
root="G:dataet\\Annotation"
total_xml=os.listdir(root)
list_xml_path=[]
for i in total_xml:
	list_xml_path.append(os.path.join(root,i))
# print(list_xml_path)
name_list=[]
for path in list_xml_path:
	tree=ET.parse(path)
	wh=tree.find("size")
	w,h=float(wh.find("width").text),float(wh.find("height").text)
	for obj in tree.findall("object"):
		_box=obj.find("bndbox")
		name=obj.find("name").text
		if name not in name_list:
			name_list.append(name)
		x1=float(_box.find("xmin").text)
		y1=float(_box.find("ymin").text)
		x2=float(_box.find("xmax").text)
		y2=float(_box.find("ymax").text)
		# if x1>=x2 or y1>=y2:
		# 	print(path)
		if x1==0 or y1==0 or x2==0 or y2==0:
			print(path)
		# if x1>w or x2>w or y1>h or y2>h:
		# 	print(x1,x2,y1,y2,w,h)
		# 	print(path)
print(name_list)