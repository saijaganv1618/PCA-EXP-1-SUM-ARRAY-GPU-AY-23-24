

# import cv2
# from google.colab.patches import cv2_imshow

# In[ ]:


#read and diplay image
#Type ur code here


# In[ ]:


#WRITE AN IMAGE
#Type ur code here

# Save the original image to a file
original_output_path = "image path"
#Type ur code here
cv2.imwrite(original_output_path, image)
print(f"Original image saved to: {original_output_path}")

# Read the saved image
#Type ur code here

# Display the saved image
#Type ur code here

# Save the saved image to a new file
#Type ur code here
cv2.imwrite(new_output_path, saved_image)
print(f"Saved image saved to: {new_output_path}")


# In[ ]:


#ACCESSING ROWS AND COLUMNS
#Type ur code here
# Get the shape of the image (rows, columns, channels)

print(f"Image Shape: Rows={rows}, Columns={columns}, Channels={channels}")

# Assign random values to pixels in the first row and first column
                                                                 # Random values for the first row
image[:, 0] = np.random.randint(0, 256, size=(rows, channels))  # Random values for the first column
#Type ur code here
# Display the modified image
#Type ur code here


# In[ ]:


#Cut and paste the image

#Type ur code here
# Display the original image

#Type ur code here
# Get the shape of the image (rows, columns, channels)
#Type ur code here

# Define the region to cut (example: top-left corner, width=100, height=100)
cut_region = image[0:100, 0:100]

# Paste the cut region back onto the image (example: paste at (200, 200))
image[] = cut_region
#Display the modified image
#Type ur code here


# In[ ]:


#######COLOR CONVERSION
##Convert BGR and RGB to HSV and GRAY
#Type ur code here
# Convert BGR to RGB
image_rgb = (image_bgr, cv2.COLOR_BGR2RGB)

# Convert BGR to HSV
image_hsv_bgr = cv2.cvtColor(image_bgr, )

# Convert RGB to HSV
#Type ur code here

# Convert BGR to Grayscale
#Type ur code here

# Convert RGB to Grayscale
#Type ur code here

# Display the original BGR image
#Type ur code here
# Display the HSV image (BGR and RGB converted)
#Type ur code here
# Display the Grayscale image (BGR and RGB converted)
print("BGR TO GRAY")
cv2_imshow(image_gray_bgr)
print("RGB TO GRAY")
cv2_imshow(image_gray_rgb)


# In[ ]:


##Convert HSV to RGB and BGR
#Type ur code here
# Convert BGR to HSV
#Type ur code here
# Convert HSV to RGB
#Type ur code here
# Convert HSV to BGR
image_bgr_hsv = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

# Display the original BGR image
#Type ur code here
cv2_imshow(image_bgr)

# Display the HSV image
#Type ur code here
cv2_imshow(image_hsv)

# Display the RGB image (HSV to RGB)
print("HSV TO RGB")
#Type ur code here

# Display the BGR image (HSV to BGR)

#Type ur code here


# In[ ]:


##Convert RGB and BGR to YCrCb
#Type ur code here

# Convert BGR to YCrCb
image_ycrcb_bgr = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YCrCb)

# Convert RGB to YCrCb
#Type ur code here
                                                                # Convert BGR to RGB
image_ycrcb_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)

# Display the original BGR image
#Type ur code here

# Display the YCrCb image (BGR to YCrCb)
#Type ur code here

# Display the YCrCb image (RGB to YCrCb)

#Type ur code here


# In[ ]:


#Split and Merge RGB Image


## Split the RGB channels
blue_channel, green_channel, red_channel = cv2.split(image_bgr)

# Display the original BGR image
#Type ur code here

# Display the individual RGB channels
print("BLUE CHANNEL")
cv2_imshow(blue_channel)
#Type ur code here

# Merge the RGB channels back together

#Type ur code here
# Display the merged image
#Type ur code here


# In[ ]:


##Split and merge HSV Image
#Type ur code here
# Convert BGR to HSV
#Type ur code here

# Split the HSV channels
#Type ur code here
# Display the original BGR image and the converted HSV image
print("ORIGINAL IMAGE")
cv2_imshow(image_bgr)
print("HSV IMAGE")
cv2_imshow(image_hsv)

# Display the individual HSV channels
#Type ur code here


# In[ ]:




