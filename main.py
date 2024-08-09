from PIL import Image
import os

username = os.getlogin()

osu_path = "C:\\Users\\"+username+"\\AppData\\Local\\osu!\\Skins\\"
print("enter skin name")
skin_name = input()#"GRM KW2"

file_path = osu_path + skin_name +"\\"

do_2x = "" #if @2x do "@2x"
    
resamp_filter = Image.Resampling.BICUBIC

hc_overlay = Image.open(file_path+'hitcircleoverlay'+do_2x+'.png').convert("RGBA")
hc = Image.open(file_path+'hitcircle'+do_2x+'.png').convert("RGBA")

if do_2x == "":
    org_hc_width, org_hc_height = hc.size
    hc = hc.resize(size=[int(org_hc_width*1.25), int(org_hc_height*1.25)], resample=resamp_filter)
    
    org_hc_overlay_width, org_hc_overlay_height = hc_overlay.size
    hc_overlay = hc_overlay.resize(size=[int(org_hc_overlay_width*1.25), int(org_hc_overlay_height*1.25)], resample=resamp_filter)


org_hc_width, org_hc_height = hc.size
org_hc_overlay_width, org_hc_overlay_height = hc_overlay.size

if org_hc_width >= org_hc_overlay_width:
    width1 = org_hc_width
    height1 = org_hc_height

"""
full_hc = Image.new('RGBA', (width1, height1))
full_hc.paste(hc, (0,0))
full_hc.paste(hc_overlay, (100,0))

"""

full_hc = Image.alpha_composite(hc, hc_overlay)
#full_hc.save("kutasexe.png")

for i in range(10):
    num_path = file_path + "default-"+str(i)+do_2x+".png"
    image2 = Image.open(num_path)
    width2, height2 = image2.size
    new_image = Image.new('RGBA', (width1, height1))
    new_image.paste(image2, (width1//2-width2//2, height1//2-height2//2))
    new_image = Image.alpha_composite(full_hc, new_image)
    #new_image.paste(full_hc, (0, 0))
    new_image.save("default-"+str(i)+do_2x+".png")


