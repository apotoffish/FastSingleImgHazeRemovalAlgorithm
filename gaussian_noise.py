import numpy as np

def gasuss_noise(image, mean=0, sigma=0.05):
    '''
        添加高斯噪声
        mean : 均值
        sigma : 标准差
    '''
    image = np.array(image / 255, dtype=float)
    noise = np.random.normal(mean, sigma, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)
    return out
