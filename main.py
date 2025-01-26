import pyautogui as pag
import time


def goPrevPage():
    pag.moveTo(15, 535, duration = 0.1)
    pag.click()


def goNextPage():
    pag.moveTo(1495, 535, duration = 0.1)
    pag.click()


def goToPage(n):
    if type(n) is int and n > 0:
        # pag.moveTo(130, 72, duration = 0.1)
        pag.click(120, 60, duration=0.2)
        # pag.moveTo(530, 125, duration = 0.1)
        pag.click(515, 110, duration=0.2)
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
    lPageTopLeft = (85, 87)
    lPageBottomRight = (755, 981)

    takeScreenshot(lPageTopLeft, lPageBottomRight, name)


def getRPage(name):
    rPageTopLeft = (755, 87)
    rPageBottomRight = (1426, 981)

    takeScreenshot(rPageTopLeft, rPageBottomRight, name)


def getPages(first, number):
    goToPage(first)
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
    
    getPages(192, 4)

    pag.moveTo(0, 0)