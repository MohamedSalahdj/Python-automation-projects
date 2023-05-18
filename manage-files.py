import os,shutil
source_path = input("Enter Absolute path of folder that you wants manage files it:  ")

os.chdir(source_path)

print(os.getcwd())
for filename in os.listdir(source_path):
    if filename.endswith(('.docx','.doc')):
        if not os.path.exists('word'):
            os.mkdir('word')
        shutil.move(filename, 'word')

    elif filename.endswith(('.pdf',)):
        if not os.path.exists('pdf'):
            os.mkdir('pdf')
        shutil.move(filename, 'pdf')

    elif filename.endswith(('.pptx','.ppt')):
        if not os.path.exists('power-point'):
            os.mkdir('power-point')
        shutil.move(filename, 'power-point')

    elif filename.endswith(('xlsx','.csv')):
        if not os.path.exists('Excel'):
            os.mkdir('Excel')
        shutil.move(filename, 'Excel')

    elif filename.endswith(('.zip','.rar')):
        if not os.path.exists('Archive'):
            os.mkdir('Archive')
        shutil.move(filename, 'Archive')

    elif filename.endswith(('.exe')):
        if not os.path.exists('Programs'):
            os.mkdir('Programs')
        shutil.move(filename, 'Programs')
    
    elif filename.endswith(('.png','jpg','.jpeg','.svg','gif')):
        if not os.path.exists('Images'):
            os.mkdir('Images')
        shutil.move(filename, 'Images')
    
    elif filename.endswith(('.mp4','.mov','.wmv','.avi','.mkv')):
        if not os.path.exists('Video'):
            os.mkdir('Video')
        shutil.move(filename, 'Video')

    elif not os.path.isdir(source_path+'/'+filename):
        if not os.path.exists('Others'): 
            os.mkdir('Others')
        shutil.move(filename,'Others')
