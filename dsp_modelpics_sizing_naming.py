
import os
import PIL
from PIL import Image

# Address of the folder in which your original pictures are saved
originals_directory = r'C:\Users\...'

# Create a folder for small size pictures
os.mkdir(os.path.dirname(originals_directory)+'\dsp_model')

# Create a folder for large size pictures
os.mkdir(os.path.dirname(originals_directory)+'\dsp_modelview')

# Access the folder in which original pictures are saved
os.chdir(originals_directory)

# Create a white background respecting small picture dimensions
background = Image.new('RGB', (250,225), (255,255,255))

# Target width and weight to fit into the background
basewidth = 240
baseheight = 215

# Open every image of my original directory
for file in os.listdir():
    
    # Create a copy of the background
    background_copy = background.copy()
    # Open image
    img = Image.open(file)
    # Create a copy of the image
    imgcopy = img.copy()
    # Store the size of the image
    imgcopy_size = imgcopy.size
    
    # If the image is wider than high
    if imgcopy_size[0] > imgcopy_size[1]:
        
        # Calculate the required coefficient of reduction to reach target width
        wpercent = (basewidth / float(imgcopy_size[0]))
        # Reduce height using the coefficient of reduction
        hsize = int((float(imgcopy_size[1]) * float(wpercent)))
        
        # If height is still higher than target height after reduction
        if hsize > baseheight :
            
            # Calculate the required coefficient of reduction to reach target height
            hpercent = (baseheight / float(img.size[1]))
            # Reduce width using the coefficient of reduction
            wsize = int((float(img.size[0]) * float(hpercent)))
            # Resize the image
            imgcopy = imgcopy.resize((wsize, baseheight), PIL.Image.ANTIALIAS)         
            
        # If height is lower or equal to target height
        else :
            
            # Resize the image
            imgcopy = imgcopy.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        
        # Paste the image on the center of the background
        background_copy.paste(imgcopy, box=(int(float((background.size[0] - imgcopy.size[0])/2)), int(float((background.size[1] - imgcopy.size[1])/2))))
        
        # Rename the image and save it in the required directory
        background_copy.save(os.path.dirname(originals_directory) + '\dsp_model\dsp_model_' + file)
    
    # If the image is higher than wide    
    else :
    
        # Calculate the required coefficient of reduction to reach target height
        hpercent = (baseheight / float(imgcopy.size[1]))
        # Reduce width using the coefficient of reduction
        wsize = int((float(imgcopy.size[0]) * float(hpercent)))
        
        # If width is still higher than target width after reduction
        if wsize > basewidth :
            
            # Calculate the required coefficient of reduction to reach target width
            wpercent = (basewidth / float(img.size[0]))
            # Reduce height using the coefficient of reduction
            hsize = int((float(img.size[1]) * float(wpercent)))
            # Resize the image
            imgcopy = imgcopy.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        
        # If width is lower or equal to target width
        else :
            
            # Resize the image
            imgcopy = imgcopy.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
        
        # Paste the image on the center of the background
        background_copy.paste(imgcopy, box=(int(float((background.size[0] - imgcopy.size[0])/2)), int(float((background.size[1] - imgcopy.size[1])/2))))
        
        # Rename the image and save it in the required directory
        background_copy.save(os.path.dirname(originals_directory) + '\dsp_model\dsp_model_' + file)

# Create a white background respecting large picture dimensions
background = Image.new('RGB', (375,450), (255,255,255))

# Target width and weight to fit into the background
basewidth = 350
baseheight = 425

# Open every image of my original directory
for file in os.listdir():

    # Create a copy of the background
    background_copy = background.copy()
    # Open image
    img = Image.open(file)
    # Create a copy of the image
    imgcopy = img.copy()
    # Store the size of the image
    imgcopy_size = imgcopy.size
    
    # If the image is wider than high
    if imgcopy_size[0] > imgcopy_size[1]:
        
        # Calculate the required coefficient of reduction to reach target width
        wpercent = (basewidth / float(imgcopy_size[0]))
        # Reduce height using the coefficient of reduction
        hsize = int((float(imgcopy_size[1]) * float(wpercent)))
        
        # If height is still higher than target height after reduction
        if hsize > baseheight :
            
            # Calculate the required coefficient of reduction to reach target height
            hpercent = (baseheight / float(img.size[1]))
            # Reduce width using the coefficient of reduction
            wsize = int((float(img.size[0]) * float(hpercent)))
            # Resize the image
            imgcopy = imgcopy.resize((wsize, baseheight), PIL.Image.ANTIALIAS)         

        # If height is lower or equal to target height
        else :
            
            # Resize the image
            imgcopy = imgcopy.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        
        # Paste the image on the center of the background
        background_copy.paste(imgcopy, box=(int(float((background.size[0] - imgcopy.size[0])/2)), int(float((background.size[1] - imgcopy.size[1])/2))))
        
        # Rename the image and save it in the required directory
        background_copy.save(os.path.dirname(originals_directory) + '\dsp_modelview\dsp_modelview_' + file)
    
    # If the image is higher than wide     
    else :
    
        # Calculate the required coefficient of reduction to reach target height
        hpercent = (baseheight / float(imgcopy.size[1]))
        # Reduce width using the coefficient of reduction
        wsize = int((float(imgcopy.size[0]) * float(hpercent)))
        
        # If width is still higher than target width after reduction
        if wsize > basewidth :
            
            # Calculate the required coefficient of reduction to reach target width
            wpercent = (basewidth / float(img.size[0]))
            # Reduce height using the coefficient of reduction
            hsize = int((float(img.size[1]) * float(wpercent)))
            # Resize the image
            imgcopy = imgcopy.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        
        # If width is lower or equal to target width
        else :
            
            # Resize the image
            imgcopy = imgcopy.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
        
        # Paste the image on the center of the background
        background_copy.paste(imgcopy, box=(int(float((background.size[0] - imgcopy.size[0])/2)), int(float((background.size[1] - imgcopy.size[1])/2))))
        
        # Rename the image and save it in the required directory
        background_copy.save(os.path.dirname(originals_directory) + '\dsp_modelview\dsp_modelview_' + file)


        
