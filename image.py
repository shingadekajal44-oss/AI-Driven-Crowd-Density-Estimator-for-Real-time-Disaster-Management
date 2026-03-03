# import random
# import os
# from PIL import Image,ImageFilter,ImageDraw
# import numpy as np
# import h5py
# from PIL import ImageStat
# import cv2

# def load_data(img_path,train = True):
#     gt_path = img_path.replace('.jpg','.h5').replace('images','ground_truth')
#     img = Image.open(img_path).convert('RGB')
#     gt_file = h5py.File(gt_path)
#     target = np.asarray(gt_file['density'])
#     if train:
#         crop_size = (img.size[0]/2,img.size[1]/2)
#         if random.randint(0,9)<= -1:
            
            
#             dx = int(random.randint(0,1)*img.size[0]*1./2)
#             dy = int(random.randint(0,1)*img.size[1]*1./2)
#         else:
#             dx = int(random.random()*img.size[0]*1./2)
#             dy = int(random.random()*img.size[1]*1./2)
        
        
        
#         img = img.crop((dx,dy,crop_size[0]+dx,crop_size[1]+dy))
#         target = target[dy:crop_size[1]+dy,dx:crop_size[0]+dx]
    
    
    
    
#     target = cv2.resize(target,(target.shape[1]/8,target.shape[0]/8),interpolation = cv2.INTER_CUBIC)*64
    
    
#     return img,target




# import random
# import cv2
# import numpy as np
# from PIL import Image
# import h5py

# def load_data(img_path, train=True):

#     gt_path = img_path.replace(".jpg", ".h5").replace("images", "ground_truth")
#     img = Image.open(img_path).convert("RGB")
#     gt = h5py.File(gt_path)
#     target = np.asarray(gt["density"])

#     if train:
#         crop_w = img.size[0] // 2
#         crop_h = img.size[1] // 2

#         dx = int(random.random() * (img.size[0] - crop_w))
#         dy = int(random.random() * (img.size[1] - crop_h))

#         img = img.crop((dx, dy, dx + crop_w, dy + crop_h))
#         target = target[dy:dy + crop_h, dx:dx + crop_w]

#     target = cv2.resize(target, (target.shape[1] // 8, target.shape[0] // 8),
#                         interpolation=cv2.INTER_CUBIC) * 64

#     return img, target




import random
import cv2
import numpy as np
from PIL import Image
import h5py
import os

def load_data(img_path, train=True, expected_downscale=8, debug=False):
    """
    expected_downscale: the factor by which model output is smaller than original image (default 8 for CSRNet)
    """

    gt_path = img_path.replace(".jpg", ".h5").replace("images", "ground_truth")
    img = Image.open(img_path).convert("RGB")

    if not os.path.exists(gt_path):
        raise FileNotFoundError(f"Ground-truth .h5 not found for {img_path}. Expected at {gt_path}")

    with h5py.File(gt_path, 'r') as gt:
        # common key: 'density' (adjust if your key is different)
        if 'density' in gt:
            target = np.asarray(gt['density'])
        else:
            # list keys to help debug
            raise KeyError(f"No 'density' key in {gt_path}. Keys: {list(gt.keys())}")

    if train:
        crop_w = img.size[0] // 2
        crop_h = img.size[1] // 2

        if img.size[0] - crop_w <= 0 or img.size[1] - crop_h <= 0:
            dx = 0; dy = 0
        else:
            dx = int(random.random() * (img.size[0] - crop_w))
            dy = int(random.random() * (img.size[1] - crop_h))

        img = img.crop((dx, dy, dx + crop_w, dy + crop_h))
        target = target[dy:dy + crop_h, dx:dx + crop_w]

    # ---- Downsample target to model output size ----
    new_w = target.shape[1] // expected_downscale
    new_h = target.shape[0] // expected_downscale

    if new_w <= 0 or new_h <= 0:
        raise ValueError("Target too small to downsample by expected_downscale")

    # Resize and preserve sum: multiply by area scaling (orig_area / new_area)
    area_scale = (target.shape[0] * target.shape[1]) / (new_h * new_w)  # should equal expected_downscale**2

    resized = cv2.resize(target, (new_w, new_h), interpolation=cv2.INTER_CUBIC)

    # Decide whether to apply area_scale or not:
    # If the density in .h5 is already at reduced resolution, area_scale should be 1.0
    # We will check a quick condition: if resized.sum() is close to original sum/area_scale, then skip multiply.
    eps = 1e-6
    orig_sum = target.sum()
    resized_sum = resized.sum()

    # If original sum is almost equal to resized_sum * area_scale => then target was full-resolution
    if abs(orig_sum - resized_sum * area_scale) / (orig_sum + eps) < 1e-3:
        # we need to multiply resized by area_scale to preserve count
        final_target = resized * area_scale
    else:
        # likely the .h5 already stores downsampled density (common). Don't multiply.
        final_target = resized

    if debug:
        print(f"[DEBUG] {os.path.basename(img_path)}: orig_sum={orig_sum:.4f}, resized_sum={resized_sum:.4f}, area_scale={area_scale:.4f}, final_sum={final_target.sum():.4f}")

    return img, final_target
