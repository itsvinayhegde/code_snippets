import os

# mention bith input and output directories
input_dir = "/home/vinay/vinay/code/fold"
output_dir = "/home/vinay/vinay/code/fold_out"
os.makedirs(output_dir, exist_ok=True)

"""
key -> class id you want to replace
val -> class id you want replace with
for example, key[0] will be replaced by val[0].
"""
key = [5, 26, 8] 
val = [81, 54, 65] 

if len(key) != len(val):
    print("Aborting : Length of key and value list are not same")
    exit(0)

in_file_count = 0
out_file_count = 0

for file in sorted(os.listdir(input_dir)):
    filepath = os.path.join(input_dir,file)
    filename = os.path.basename(filepath)
    
    new_label_list = []

    with open(filepath, 'r') as f:
        in_file_count += 1
        label_contents = f.readlines()

    for line in label_contents:
        line = line.rstrip().split(' ')
        for a in range(len(key)):
            if int(line[0]) == key[a]:
                    line[0] = str(val[a])
        new_label = ' '.join(line)
        new_label_list.append(new_label)

    with open(os.path.join(output_dir,filename),'w') as fe:
        for item in new_label_list:
            fe.write("%s\n" % item)
        out_file_count += 1

print(f"files in input folder -> {in_file_count}")
print(f"files in output folder -> {out_file_count}")