import cv2 as cv
import torch
import numpy as np
import matplotlib.pyplot as plt


midas = torch.hub.load('intel-isl/MiDaS', 'MiDaS')
midas.to('cpu')
midas.eval()

transfroms = torch.hub.load('intel-isl/MiDaS','transforms')
transform =transfroms.small_transform

capture = cv.VideoCapture(0)
while True:
    isTrue,frame = capture.read()

    img = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    imgbatch = transform(img).to ('cpu')

    with torch.no_grad():
        prediction = midas(imgbatch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size= img.shape[:2],
            mode = 'bicubic',
            align_corners=True
        ).squeeze()

        output = prediction.cpu().numpy()
        print(output)



    plt.imshow(output,cmap='viridis')
    cv.imshow('live',frame)
    plt.pause(0.00001)




    if cv.waitKey(10)& 0xFF == ord('q'):
        break
capture.release()
cv.destroyAllWindows()
plt.show()
