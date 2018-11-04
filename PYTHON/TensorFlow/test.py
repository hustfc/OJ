f = open("mini_classes.txt","r")
# And for reading use
classes = f.readlines()
f.close()
classes = [c.replace('\n','').replace(' ','_') for c in classes]
classes = classes[0:3]
print(classes)
# import urllib.request
# def download():
#     base = 'https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/'
#     for c in classes:
#         cls_url = c.replace('_', '%20')
#         path = base + cls_url + '.npy'
#         print(path)
#         urllib.request.urlretrieve(path, 'data/' + c + '.npy')
# download()

