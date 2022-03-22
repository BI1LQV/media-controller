import time
import controller
lastAction = -1
lastExecTime = 0
indexToActionMap = [
    controller.volumeUp,
    controller.volumeDown,
    controller.rewind,
    controller.fastforward,
    controller.playOrPause,
    controller.screenShot
]


def actionExecute(i):
    indexToActionMap[i]()
