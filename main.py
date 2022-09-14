
import cv2 
import os 
import shutil
import torch
from Save_result import Tool


filepath = r'C:\Users\GÜNERARDAIŞIK\Desktop\labeler\images'
destination = r'C:\Users\GÜNERARDAIŞIK\Desktop\labeler\dest'

model = torch.hub.load(r'C:\yolov5', 'custom', path=r'C:\Users\GÜNERARDAIŞIK\Desktop\labeler\model\KAAN.pt', source='local')

for filename in os.listdir(filepath):
    if "." not in filename:
        continue
    ending = filename.split(".")[-1]
    if ending not in ["jpg", "gif", "png","jfif","JPG", 'txt']:
        continue
    img = cv2.imread('images/'+filename)
    filename=filename.split('.jpg')[0]

    img1, img2 = Tool.divide(img)
    cv2.imwrite(destination+'\\'+ filename +'1.jpg', img1)
    cv2.imwrite(destination+'\\'+ filename +'2.jpg', img2)
    results1 = model(img1)
    results2 = model(img2)
    results1.display(render=True)
    results2.display(render=True)
    # Save_result.get_values(results)
    lines = Tool.get_values(results=results1)
    lines2 = Tool.get_values(results=results2)
    

    Tool.save_txt(lines,destination+'\\'+filename+'1.txt')
    Tool.save_txt(lines2,destination+'\\'+filename+'2.txt')

    cv2.imshow('img1', results1.imgs[0])
    cv2.imshow('img2', results2.imgs[0])

    
    cv2.waitKey(0)
    
