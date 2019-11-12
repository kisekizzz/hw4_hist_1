import cv2 as cv
import numpy as np
LEVEL = 256

def equalize_hist(imgS):
    imgInfo = imgS.shape
    imgHight = imgInfo[0];
    imgWide = imgInfo[1];
    PixelTotal = imgHight * imgWide;
    PixelLevelStatist = [0 for i in range(LEVEL)]
    cdf = [0 for i in range(LEVEL)]
    PixelNewLevel = [0 for i in range(LEVEL)]
    print("统计中...")
    for i in range(PixelTotal):
        PixelLevelStatist[imgS[i % imgHight][i // imgHight]] += 1

    print("计算概率中...")
    for i in range(LEVEL):
        if i != 0:
            cdf[i] = cdf[i - 1] + PixelLevelStatist[i] / PixelTotal;
        else:
            cdf[i] = PixelLevelStatist[i] / PixelTotal;

        print("生成新灰度级中...")
    for i in range(LEVEL):
        LevelTemp = int((LEVEL - 1) * cdf[i] + 0.5)
        PixelNewLevel[i] = LevelTemp

    imgNew = np.zeros(imgHight,imgWide, dtype = np.uint8)

    print("图片重新生成中...")
    for i in range(imgHight):
        for j in range(imgWide):
            imgNew[i][j] = PixelNewLevel[imgS[i][j]]

    return imgNew


if __name__ == '__main__':
    imgS = cv.imread("88.png")
    imgNew = equalize_hist(imgS)
    cv.imshow(imgS)
    cv.imshow(imgNew)
    cv.waitKey(0)


