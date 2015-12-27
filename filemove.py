import os


start_dir = "/Users/kimbusung/Downloads"
dest_dir = "/Users/kimbusung/Downloads/Modern Family S07/"

moved_list = []

for entry in os.scandir(start_dir):
    if entry.is_dir():
        for inner_entry in os.scandir(entry.path):
            if inner_entry.name.startswith("Modern"):
                moved_list.append(list((inner_entry.name, inner_entry.path)))

for entry in  moved_list:
    os.rename(entry[1], dest_dir+entry[0])



