import imageio
from pygifsicle import optimize
from skimage.transform import resize
import os, sys

class TargetFormat(object):
    GIF = ".gif"
    MP4 = ".mp4"
    AVI = ".avi"

def convertFile(inputpath, targetFormat):
    """Reference: http://imageio.readthedocs.io/en/latest/examples.html#convert-a-movie"""
    outputpath = os.path.splitext(inputpath)[0] + targetFormat
    print("\r\n{0}\tto\t{1}".format(inputpath, outputpath), end = ", ")

    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']
    target_fps = 10
    write_freq = fps // target_fps
    writer = imageio.get_writer(outputpath, fps=target_fps)
    for i,im in enumerate(reader):
        if (i % write_freq == 0):
            #sys.stdout.write("\rframe {0}".format(i))
            #sys.stdout.flush()
            scale = im.shape[1] / 480
            imshape = (im.shape[0] / scale, im.shape[1] / scale)
            imshape = (int(imshape[0]), int(imshape[1]))
            writer.append_data((255 * resize(im, imshape)).astype('uint8'))
    #print("\r\nFinalizing...")
    print(i)
    writer.close()
    #print("Done.")

def optimize_gif(pth):
    print(pth)
    optimize(pth)

def to_mp4(pth):
    opth = '/'.join(['mp4'] + pth.split('/')[1:])
    opth = opth[:-3] + 'mp4'
    os.system("ffmpeg -i {} {}".format(pth, opth))
#convertFile("C:\\Users\\Yoda\\Desktop\\EwokPr0n.mp4", TargetFormat.GIF)
#import pdb; pdb.set_trace()
#convertFile("rma-foam-1.mp4", TargetFormat.GIF)
#optimize("rma-foam-1.gif")
#for root, dirs, files in os.walk("."):
for root, dirs, files in os.walk("gifs"):
    for fname in files:
        if fname.endswith(".gif"):
            fpth = os.path.join(root, fname)
            #convertFile(fpth, TargetFormat.GIF)
            to_mp4(fpth)
