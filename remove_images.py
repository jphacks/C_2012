import os
import glob

# imageかつformat外のファイルの一括削除
def remove_images():
    file_list = glob.glob('images/*')

    for file in file_list:
        os.remove(file)

if __name__ == '__main__':
    remove_images()
