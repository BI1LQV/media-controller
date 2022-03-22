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
    def exec():
        indexToActionMap[i]()
        print(i, 'exec')
        global lastAction
        global lastExecTime
        lastAction = i
        lastExecTime = time.time()
    if i in [0, 1, 2, 3]:  # 为持续性动作
        if lastAction != i:  # 不同动作 直接执行
            exec()
        elif time.time()-lastExecTime > 0.5:  # 相同动作 间隔500毫秒执行
            exec()
    else:  # 为一次性动作
        if lastAction != i:  # 必须为不同动作才能执行
            exec()
