import pandas as pd


class Save_result():
    def make_txt(self, classId, x1, x2, y1, y2, width, height):
        cx = (x1 + x2)/ 2
        cy = (y1 + y2)/ 2
        cx = cx / width
        cy = cy / height
        xlen = (x2 - x1) / width
        ylen = (y2 - y1) / height

        return f'{classId} {cx} {cy} {xlen} {ylen}'
    
    def divide(self, img):
        height=  img.shape[0]
        print(height)
        img1 = img[0:int(height/2),:]
        img2 =  img[int(height/2):,:]
        return (img1, img2)
    

    def get_values(self,results):
        values=[]
        height, width = results.imgs[0].shape[:2]
        print(height, width)
        df=results.pandas().xyxy[0]
        df=pd.DataFrame(df)
        for detect in range(len(df.iloc[:]['name'])):
            classId = str(df.iloc[:]['class'][detect])
            x1=int(df.iloc[:]['xmin'][detect])
            x2=int(df.iloc[:]['xmax'][detect])
            y1=int(df.iloc[:]['ymin'][detect])
            y2=int(df.iloc[:]['ymax'][detect])
            values.append(self.make_txt(classId, x1, x2, y1, y2, width, height ))
        return values

    def save_txt(self, lines, path):
        
        with open(path, 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')

Tool = Save_result()
    
        
    

    