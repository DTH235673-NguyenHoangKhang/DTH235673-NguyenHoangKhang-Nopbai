#Cau8
import os

def get_filename(path):
    for i in range(len(path)-1, 0, -1):
        if path[i] == '\\' or path[i] == '/':
            return path[i+1:]

def get_songname(path):
    for i in range(len(path)-1, 0, -1):
        if path[i] == '.':
            for j in range(i-1, 0, -1):
                if path[j] == '\\' or path[j] == '/':
                    return path[j+1:i]
# Ví dụ sử dụng
path = r"d:\music\muabui.mp3"
print(get_filename(path))   # muabui.mp3
print(get_songname(path))   # muabui
