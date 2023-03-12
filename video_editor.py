import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import youtube_dl
import win32gui
import mpv


class MyWidget(QWidget):
   def __init__(self,title=""):
      super().__init__()
      self.other_widgets = []
      self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
      self.setWindowTitle(title)
   
   def moveEvent(self, event):
      super().moveEvent(event)

class mpv_player():
   def __init__(self,fname):
      self.player=mpv.MPV(
         wid=str(PID),
         input_default_bindings=True,
         input_vo_keyboard=True,
         osc=True,
         #ytdl=use_youtube_dl
         ytdl=False
      )
      self.player.play(fname)
      self.player.loop=True
      self.player.volume=35

if __name__ == '__main__':
   app = QApplication(sys.argv)

   # create four instances of MyWidget
   widget1 = MyWidget("left")
   widget2 = MyWidget("video")
   widget3 = MyWidget("timeline")
   widget4 = MyWidget("right")
   widget1.other_widgets=[widget1, widget2, widget3]
   widget2.other_widgets=[widget1, widget2, widget3]
   widget3.other_widgets=[widget1, widget2, widget3]
   widget4.other_widgets=[widget1, widget2, widget3]
   widget1.setStyleSheet('background-color: #444;')
   widget2.setStyleSheet('background-color: #333;')
   widget3.setStyleSheet('background-color: #222;')
   widget4.setStyleSheet('background-color: #444;')
   
   
   url = r"D:\videos\yoink\undergrown\first_undergrown_lets_play_2022-11-29_11-44-03.mp4"
   
   # ydl = youtube_dl.YoutubeDL()
   # info_dict = ydl.extract_info(url, download=False)
   # url=info_dict['url']
   
   # set the geometry of the windows
   x=0
   y=0
   width=1920-x
   height=1080-y
   
   widget1.setGeometry(x, y, int(width/3), height)
   widget2.setGeometry(x+int(width/3), y, int(width/3), int(height/2))
   widget3.setGeometry(x+int(width/3), y+int(height/2), int(width/3), int(height/2))
   widget4.setGeometry(x+(int(width/3)*2), y, int(width/3), height)

   # show the windows
   widget1.show()
   widget2.show()
   widget3.show()
   widget4.show()
   
   PID=win32gui.FindWindowEx(None,None,None,'video')
   print(PID)
   mpv_player(url)

   sys.exit(app.exec())
