import win32api
from win32con import KEYEVENTF_EXTENDEDKEY
from win32con import VK_MEDIA_PLAY_PAUSE as VK_MEDIA_PLAY_PAUSE  # 暂停播放
from win32con import VK_VOLUME_MUTE, VK_VOLUME_DOWN, VK_VOLUME_UP  # 音量控制
from win32con import VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK  # 上一首下一首
from win32con import VK_SNAPSHOT  # 截屏
from win32con import VK_UP, VK_DOWN
import requests


def playOrPause():
    '''
    暂停或播放
    '''
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)


def volumeMute():
    '''
    静音
    '''
    win32api.keybd_event(VK_VOLUME_MUTE, 0, KEYEVENTF_EXTENDEDKEY, 0)


def volumeUp():
    '''
    音量提升
    '''
    win32api.keybd_event(VK_VOLUME_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)


def volumeDown():
    '''
    音量下降
    '''
    win32api.keybd_event(VK_VOLUME_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)


def nextTrack():
    '''
    下一首
    '''
    win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)


def prevTrack():
    '''
    上一首
    '''
    win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)


def screenShot():
    '''
    截屏
    '''
    win32api.keybd_event(VK_SNAPSHOT, 0, KEYEVENTF_EXTENDEDKEY, 0)


def accelerate():
    '''
    加速
    '''
    requests.get("http://127.0.0.1:8090?action=accelerate")


def decelerate():
    '''
    减速
    '''
    requests.get("http://127.0.0.1:8090?action=decelerate")


def fastforward():
    '''
    快进
    '''
    requests.get("http://127.0.0.1:8090?action=fastforward")


def rewind():
    '''
    后退
    '''
    requests.get("http://127.0.0.1:8090?action=rewind")


def prePPT():
    win32api.keybd_event(VK_UP, 0, KEYEVENTF_EXTENDEDKEY, 0)


def nextPPT():
    win32api.keybd_event(VK_DOWN, 0, KEYEVENTF_EXTENDEDKEY, 0)
