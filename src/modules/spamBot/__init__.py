import json
import win32api
import win32gui
import win32con
from abc import ABC, abstractmethod


class Bot:
    @abstractmethod
    def __find_tibia_window(self) -> None:
        pass

    @abstractmethod
    def start_send_message(self) -> None:
        pass


class SpamBot(Bot):
    def __init__(self, message_to_send: str, time_beetween_message: int, speed: int = 2) -> None:
        self.message = message_to_send
        self.time = time_beetween_message
        self.speed = speed
        self.__tibia_window = win32gui.FindWindowEx(None, None, None, self.__find_tibia_window())

    def __find_tibia_window(self) -> None:
        def list_of_windows(hwnd, table):
            if win32gui.IsWindowVisible(hwnd):
                table.append(win32gui.GetWindowText(hwnd))

        opened_windows = []
        win32gui.EnumWindows(list_of_windows, opened_windows)

        for window in opened_windows:
            if ('Tibia' in window) or ('OTClient' in window):
                return window

    def start_send_message(self) -> None:
        

