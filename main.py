import os
import sys
import shutil
import subprocess
import webbrowser
import zipfile

from PIL import Image
from utils.androidImageSize import androidIslemListesi
from utils.iOSImageSize import iOSIslemListesi, klasorPath
from utils.toZip import zipdir

imagePath = '/Users/avdisx/PycharmProjects/iconGenerator/iconImage/ic_launcher.png'
imge = Image.open(imagePath)

# for Android
for icon in androidIslemListesi:
    print("iconlar")
    print(icon)
    img = imge.resize(icon[0])

    klasor = icon[1]
    print("klasör")
    print(klasor)
    klasorAdi = icon[1]
    print("Klasör Adı:")
    print(klasorAdi)

    varMi = os.path.exists(icon[1])
    if varMi == True:
        print("Klasör Var")
        img.save(icon[1] + "/ic_launcher.png")
    else:
        print("Klasör Yok.")
        os.makedirs(klasorAdi)
        img.save(klasorAdi + "/ic_launcher.png")

# foriOS

for iconiOS in iOSIslemListesi:
    print("iconlar")
    print(iconiOS)
    # resmi uygun boyutlarda şekillendiriyorum
    imageiOs = imge.resize(iconiOS[0])

    pathVarMi = os.path.exists(iconiOS[2])
    if pathVarMi == False:
        os.makedirs(iconiOS[2])
    dosyaAdi = iconiOS[2] + "/" + iconiOS[1] + ".png"
    print("dosyaAdi: ")
    print(dosyaAdi)
    imageiOs.save(dosyaAdi)

# Content.json Kopyalama İşlemi

shutil.copy2("./iconImage/Contents.json", klasorPath)
print("Content.json Kopyalama Başarılı")

pathVarMi = os.path.exists("./temp/outputIcons/")

if pathVarMi == False:
    os.makedirs("./temp/outputIcons/")

zipf = zipfile.ZipFile(
    './temp/outputIcons/iconPackAVS.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('./temp/iconsAVS/', zipf)
print("iconPackAVS oluşturuldu.")
zipf.close()

url = './temp/outputIcons/iconPackAVS.zip'
if sys.platform == 'darwin':
    subprocess.Popen(['open', url])
else:
    webbrowser.open_new_tab(url)
