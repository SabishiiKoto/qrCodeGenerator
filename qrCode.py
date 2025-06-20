import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer, \
    VerticalBarsDrawer, HorizontalBarsDrawer
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SolidFillColorMask, SquareGradiantColorMask, \
    HorizontalGradiantColorMask, VerticalGradiantColorMask

def rgbAsking():
    redRGB = int(input("Enter the RED number in RGB: "))
    greenRGB = int(input("Enter the GREEN number in RGB: "))
    blueRGB = int(input("Enter the BLUE number in RGB: "))
    tuple = (redRGB,greenRGB,blueRGB)
    return tuple
    


color = 'black'
background_color = 'white'
qrVersion = 1
boxSize = 5
borderSize = 5
colorBool = False
sizeBool = False
styleBool = False
maskBool = False
styleInput = ""
maskInput = ""

print("QR CODE GENERATOR")
website_link = input("Input link: ")
file_name = input("Input filename: ")
if (".png" not in file_name):
    file_name = file_name + ".png"
    
customize = input("Do you want to customize the QR Code (Enter to skip): ").rstrip()
if (customize != ""):
    menu = '''CUSTOMIZE QR CODE
    1. Color (Disable 3 & 4)
    2. Size
    3. QR Code Style (version 7.4+/Disable 1 & 4)
    4. Color Mask (version 7.4+/Disable 1 & 3)
    5. Quit
    '''
    print(menu)
    customize_choice = input("Enter choice: ")
    while(customize_choice != "5"):
        if (customize_choice == "1"):
            color = input("Color of the qr code: ").lower()
            background_color = input("Color of the background: ").lower()
            colorBool = True
            maskBool = False
            styleBool = False
            
        elif (customize_choice == "2"):
            sizeBool = True
            qrVersion = int(input("Enter a number for version (1 to 40): "))
            boxSize = int(input("Enter a number for box size: "))
            borderSize = int(input("Enter a number for border (4+): "))
            while (boxSize < 4 or qrVersion < 1 or qrVersion > 40):
                qrVersion = int(input("Enter a number for version (1 to 40): "))
                boxSize = int(input("Enter a number for box size: "))
                borderSize = int(input("Enter a number for border (4+): "))
                
        elif (customize_choice == "3"):
            styleBool = True
            maskBool = False
            colorBool = False
            if (qrVersion < 7.4):
                qrVersion = 7.4
            styleMenu = """QR Code Style
            1. Square/Normal
            2. Gapped Square
            3. Circle
            4. Rounded
            5. Vertical Bars
            6. Horizontal Bars
            """
            print(styleMenu)
            styleInput = input("Enter a choice number: ")
            while (styleInput < "1" or styleInput > "6"):
                print(styleMenu)
                styleInput = input("Enter a choice number: ")
                
        elif (customize_choice == "4"):
            maskBool = True
            styleBool = False
            colorBool = False
            if (qrVersion < 7.4):
                qrVersion = 7.4
                
            maskMenu = """QR Code Color Mask Type
            1. Solid Fill
            2. Radical Gradiant
            3. Square Gradiant
            4. Horizontal Gradiant
            5. Vertical Gradiant
            """
            print(maskMenu)
            
            maskInput = input("Enter a choice number: ")
            while (maskInput < "1" or maskInput > "5"):
                print(maskMenu)
                maskInput = input("Enter a choice number: ")
                
            
        print(menu)
        customize_choice = input("Enter choice: ")
    
try:
    qr = qrcode.QRCode(version = qrVersion, box_size = boxSize, border = borderSize)
    # version: is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix).
    # Set to <None> and use the <fit> parameter when making the code to determine this automatically.
    # box_size: controls how many pixels each "box" of the QR code is.
    # border: controls how many boxes thick the border should be ( the default is 4, which is the minimum according to the specs).
    qr.add_data(website_link)
    qr.make()
    image = qr.make_image(fill_color=color, back_color=background_color)
    
    if (styleBool):
        if (styleInput == "1"):
            image = qr.make_image(image_factory=StyledPilImage, module_drawer=SquareModuleDrawer())
            
        elif (styleInput == "2"):
            image = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
            
        elif (styleInput == "3"):
            image = qr.make_image(image_factory=StyledPilImage, module_drawer=CircleModuleDrawer())
            
        elif (styleInput == "4"):
            image = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
            
        elif (styleInput == "5"):
            image = qr.make_image(image_factory=StyledPilImage, module_drawer=VerticalBarsDrawer())
            
        elif (styleInput == "6"):
            image = qr.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer())
    
    elif (maskBool):
        if (maskInput == "1"):
            print("FRONT COLOR")
            front_color = rgbAsking()
            print("BACKGROUND COLOR")
            background_color = rgbAsking()
            image = qr.make_image(image_factory=StyledPilImage, color_mask=SolidFillColorMask(background_color,front_color))
            
        elif (maskInput == "2"):
            print("CENTER COLOR")
            center_color = rgbAsking()
            print("EDGE COLOR")
            edge_color = rgbAsking()
            print("BACKGROUND COLOR")
            background_color = rgbAsking()
            image = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask(background_color,center_color,edge_color))
            
        elif (maskInput == "3"):
            print("CENTER COLOR")
            center_color = rgbAsking()
            print("EDGE COLOR")
            edge_color = rgbAsking()
            print("BACKGROUND COLOR")
            background_color = rgbAsking()
            image = qr.make_image(image_factory=StyledPilImage, color_mask=SquareGradiantColorMask(background_color, center_color,edge_color))
            
        elif (maskInput == "4"):
            print("LEFT COLOR")
            left_color = rgbAsking()
            print("RIGHT COLOR")
            right_color = rgbAsking()
            print("BACKGROUND COLOR")
            background_color = rgbAsking()
            image = qr.make_image(image_factory=StyledPilImage, color_mask=HorizontalGradiantColorMask(background_color,left_color,right_color))
            
        elif (maskInput == "5"):
            print("TOP COLOR")
            top_color = rgbAsking()
            print("BOTTOM COLOR")
            bottom_color = rgbAsking()
            print("BACKGROUND COLOR")
            background_color = rgbAsking()
            image = qr.make_image(image_factory=StyledPilImage, color_mask=VerticalGradiantColorMask(background_color,top_color,bottom_color))
            
    image.save(file_name)
except IOError:
    print("Error while generating!")