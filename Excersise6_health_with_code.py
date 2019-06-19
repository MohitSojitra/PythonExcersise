from pygame import *

# pygame.mixer.init();
# pygame.mixer.Souns
mixer.init()
mixer.music.load("file/s.mp3")
mixer.music.play()
while mixer.music.get_busy():
    time.clock().tick(10)