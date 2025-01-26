import pyautogui as pag
import time


def goPrevPage():
    pag.moveTo(15, 1040, duration = 0.1)
    pag.click()


def goNextPage():
    pag.moveTo(3000, 1040, duration = 0.1)
    pag.click()


def goToPage(n):
    if type(n) is int and n > 0:
        pag.click(125, 90, duration=0.2)
        pag.click(515, 145, duration=0.2)
        pag.typewrite(str(n))
        pag.typewrite(['enter'])

    else:
        print(f'The page number "{n}" is inaccessible!')


def takeScreenshot(startCoords: tuple[int], endCoords: tuple[int], name):
    sX, sY = startCoords
    width, height = endCoords[0]-sX, endCoords[1]-sY

    screenshot = pag.screenshot(region=(sX, sY, width, height))

    screenshot.save(name)


def getLPage(name):
    lPageTopLeft = (128, 120)
    lPageBottomRight = (1512, 1963)

    takeScreenshot(lPageTopLeft, lPageBottomRight, name)


def getRPage(name):
    rPageTopLeft = (1512, 120)
    rPageBottomRight = (2896, 1963)

    takeScreenshot(rPageTopLeft, rPageBottomRight, name)


def getPages(first, number):
    # goToPage(first)
    indice = first
    while indice <= first+number:
        time.sleep(4)
        if indice % 2:
            getRPage(f'./pages/page{(3-len(str(indice)))*"0"+str(indice)}.png')
            goNextPage()
        else:
            getLPage(f'./pages/page{(3-len(str(indice)))*"0"+str(indice)}.png')
        indice += 1


if __name__ == "__main__":
    time.sleep(3)
    
    goToPage(50)
    time.sleep(5)
    getLPage(f'./pages/page050.png')

    pag.moveTo(0, 0)