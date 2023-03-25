def extract_place(filename):
    first = filename.find("_") #px 10
    partial = filename[first+1:]
    second = partial.find("_") #px 4
    return partial[:second]

print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))
print(extract_place("2018-01-03_Oahu_21/51/57.jpg"))
print(extract_place("2018-01_Scottland_11/51/27.jpg"))#
