# Ex01_COLOR_CONVERSIONS_OF-IMAGE
## AIM
To write a python program using OpenCV to do the following image manipulations.

i) Read, display, and write an image.

ii) Access the rows and columns in an image.

iii) Cut and paste a small portion of the image.

iv)To perform the color conversion between RGB, BGR, HSV, and YCbCr color models.


## SOFTWARE REQUIRED:
Anaconda - Python 3.7
## ALGORITHM:

- **STEP 1:** Choose an image and save it as a filename.jpg ,<br><br>
- **STEP 2:** Use imread(filename, flags) to read the file.<br><br>
- **STEP 3:** Use imshow(window_name, image) to display the image.<br><br>
- **STEP 4:** Use imwrite(filename, image) to write the image.<br><br>
- **STEP 5:** End the program and close the output image windows.<br><br>
- **STEP 6:** Convert BGR and RGB to HSV and GRAY<br><br>
- **STEP 7:** Convert HSV to RGB and BGR<br><br>
- **STEP 8:** Convert RGB and BGR to YCrCb<br><br>
- **STEP 9:** Split and Merge RGB Image<br><br>
- **STEP 10:** Split and merge HSV Image<br><br>

## PROGRAM:

**Developed By:** JANARTHANAN V K <br>
**Register Number:** 212222230051

<table>
  <tr>
    <td width=50%>

### i) Read and display the image
```Python
import cv2
image=cv2.imread('japan.jpg')
image=cv2.resize(image,(1290,720))
cv2.imshow('Janarthanan V K',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
``` 
  </td>
  <td>

### OUTPUT:

![Screenshot 2024-02-15 203203](https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/88f86204-cb22-4b72-94a5-af6a0aaff513)


 
  </td>
  </tr>

   <tr>
    <td width=50%>

### ii) Write the image
```Python
    import cv2
    image=cv2.imread('japan.jpg')
    cv2.imwrite('d.jpg',image)
```
  </td>
  <td>

### OUTPUT:
![Screenshot 2024-02-15 204036](https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/9e2f28bf-b688-471a-97b5-849ffea08705)


  </td>
  </tr>
  <tr>
    <td width=50%>

### iii) Shape of the Image
```Python
    import cv2
    image=cv2.imread('japan.jpg',1)
    print(image.shape)
```
  </td>
  <td>

### OUTPUT:

![Screenshot 2024-02-15 205108](https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/d2318219-e727-4bf8-9c21-59bc74ae2478)

  </td>
  </tr>
  <tr>
    <td>
      
### iv) Access rows and columns
```Python
    import random
    import cv2
    image=cv2.imread('japan.jpg',1)
    image=cv2.resize(image,(400,400))
    for i in range (150,200):
      for j in range(image.shape[1]):
          image[i][j]=[random.randint(0,255),
                       random.randint(0,255),
                       random.randint(0,255)] 
    cv2.imshow('part image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
  </td>
  <td width="50%">

### OUTPUT:

![Screenshot 2024-02-15 205437](https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/80aeca6f-9881-427a-9c19-3027d101cc0a)

  </td>
  </tr>
  <tr>
    <td width=50%>
      
### v) Cut and paste portion of image

 ```Python
    import cv2
    image=cv2.imread('japan.jpg',1)
    image=cv2.resize(image,(400,400))
    tag =image[130:200,110:190]
    image[110:180,120:200] = tag
    cv2.imshow('partimage1',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
  </td>
  <td>

### OUTPUT:
![Screenshot 2024-02-15 210648](https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/40ec4acf-1799-4e8e-a95a-132775b8573f)

  </td>
  </tr>
</table>

### vi) BGR and RGB to HSV and GRAY

```python
import cv2
img = cv2.imread('space1.jpg',1)
img = cv2.resize(img,(720,720))
cv2.imshow('Original Image',img)

hsv1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv1)

hsv2 = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv2)

gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',gray1)

gray2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
### OUTPUT:

<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/64d99c6e-8d82-4245-87dc-6c5dd9392374" width=350 height=350>
<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/f49590eb-8ab2-40ec-a5cb-b8fb4fc99b9d" width=350 height=350>
<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/f7800fa9-8396-4cf5-b5df-fedf8e129141" width=350 height=350>
<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/063dfd7b-ccee-49a6-8a79-e30930440fd9" width=350 height=350>
<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/895e84b1-9980-4291-baa1-c033331ba70f" width=350 height=350>

### vii) HSV to RGB and BGR
```python
import cv2
image = cv2.imread('japan.jpg')
image = cv2.resize(image,(720,720))
rgb_image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
cv2.imshow('HSV Image', image)
cv2.imshow('RGB Image', rgb_image)
cv2.imshow('BGR Image', bgr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### OUTPUT:

<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/dbb2eb9e-9064-47ec-8916-85353833882a" height=350 width="350">
<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/8a87870b-89e5-40bf-a359-5b02a91c058e" height=350 width="350">
<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/e7e8159d-64f0-4e73-b392-a11b7bfab276" height=350 width="350">

### viii) RGB and BGR to YCrCb
```python
import cv2
image = cv2.imread('japan.jpg')
image = cv2.resize(image,(720,720))
ycrcb_image = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
cv2.imshow('YCrCb Image', ycrcb_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### OUTPUT:
<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/da573c17-ac31-464d-bec3-eb50412faf1a" height=350 width="350">

### ix) Split and merge RGB Image
```python
import cv2
image = cv2.imread('japan.jpg')
image=cv2.resize(image,(720,720))
blue, green, red = cv2.split(image)
merged_image = cv2.merge([blue, green, red])
cv2.imshow('Original Image', image)
cv2.imshow('Merged Image', merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### OUTPUT:

<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/cef3bddb-3734-4177-a9cd-ccb40a9c2b46" height=350 width="350">

### x) Split and merge HSV Image
```python
import cv2
image = cv2.imread('japan.jpg')
image = cv2.resize(image,(720,720))
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(hsv_image)
merged_hsv_image = cv2.merge([hue, saturation, value])
merged_bgr_image = cv2.cvtColor(merged_hsv_image, cv2.COLOR_HSV2RGB)
cv2.imshow('Original Image', image)
cv2.imshow('Merged BGR Image', merged_bgr_image)
cv2.imshow('Original2 Image', merged_hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### OUTPUT:

<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/c87f8785-357e-48a6-8f5c-f13f416695c4" height=350 width="350">
<img src="https://github.com/Janarthanan2/DIP_EX01_COLOR_CONVERSIONS_OF-IMAGE/assets/119393515/f8168b4d-6767-4ec2-b43d-1fb446a0cb3a" height=350 width="350">



## RESULT:
Thus the images are read, displayed, and written ,and color conversion was performed between RGB, HSV and YCbCr color models successfully using the python program.



