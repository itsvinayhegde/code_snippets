import os 
import random 
import shutil

f1_image_paths = os.listdir('/home/vinay/person/DB/VOCdata/JPEGImages')
image_paths = []
for img_path in f1_image_paths:
    image_paths.append(img_path)
random.shuffle(image_paths)

try: 
	shutil.rmtree('/home/vinay/person/DB/images/train2007', ignore_error=False, onerror=None)
except Exception as e:
	print(e)
      
try: 
	shutil.rmtree('/home/vinay/person/DB/images/test2007', ignore_error=False, onerror=None)
except Exception as e:
	print(e)
      
try: 
	shutil.rmtree('/home/vinay/person/DB/images/val2007', ignore_error=False, onerror=None)
except Exception as e:
	print(e)
	
try: 
    shutil.rmtree('/home/vinay/person/DB/labels/train2007', ignore_error=False, onerror=None)
except Exception as e:
    print(e)
	
try: 
    shutil.rmtree('/home/vinay/person/DB/labels/test2007', ignore_error=False, onerror=None)
except Exception as e:
    print(e)

try: 
    shutil.rmtree('/home/vinay/person/DB/labels/val2007', ignore_error=False, onerror=None)
except Exception as e:
    print(e)
	
train_images = []
test_images = []
val_images = []

for i, image_path in enumerate(image_paths):
	if i <= int(len(image_paths) * 0.70):
		os.symlink(f"/home/vinay/person/DB/VOCdata/JPEGImages/{image_path}", f"/home/vinay/person/DB/images/train2007/{image_path}")
		xml_name = image_path.split('.')[0]
		train_images.append(f'/home/vinay/person/DB/images/train2007/{image_path}')
		shutil.copy(f"/home/vinay/person/DB/VOCdata/labels/{xml_name + '.txt'}",f"/home/vinay/person/DB/images/train2007")
		shutil.copy(f"/home/vinay/person/DB/VOCdata/labels/{xml_name + '.txt'}",f"/home/vinay/person/DB/labels/train2007")
	elif i > int(len(image_paths) * 0.70) and i < int(len(image_paths) * 0.85):
		os.symlink(f"/home/vinay/person/DB/VOCdata/JPEGImages/{image_path}", f"/home/vinay/person/DB/images/test2007/{image_path}")
		xml_name = image_path.split('.')[0]
		test_images.append(f"/home/vinay/person/DB/images/test2007/{image_path}")
		shutil.copy(f"/home/vinay/person/DB/VOCdata/labels/{xml_name + '.txt'}",f"/home/vinay/person/DB/images/test2007")
		shutil.copy(f"/home/vinay/person/DB/VOCdata/labels/{xml_name + '.txt'}",f"/home/vinay/person/DB/labels/test2007")
	else:
		os.symlink(f'/home/vinay/person/DB/VOCdata/JPEGImages/{image_path}', f'/home/vinay/person/DB/images/val2007/{image_path}')
		xml_name = image_path.split('.')[0]
		train_images.append(f'/home/vinay/person/DB/images/val2007/{image_path}')
		shutil.copy(f"/home/vinay/person/DB/VOCdata/labels/{xml_name + '.txt'}",f"/home/vinay/person/DB/images/val2007")
		shutil.copy(f"/home/vinay/person/DB/VOCdata/labels/{xml_name + '.txt'}",f"/home/vinay/person/DB/labels/tval2007")


with open(r'/home/vinay/person/DB/images/train2007.txt', 'w') as fp:
	fp.write('\n'.join(test_images))
	
with open(r'/home/vinay/person/DB/images/test2007.txt', 'w') as fp:
	fp.write('\n'.join(test_images))
	
with open(r'/home/vinay/person/DB/images/val2007.txt', 'w') as fp:
	fp.write('\n'.join(test_images))

