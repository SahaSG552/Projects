class Video:
    def create(self, name):
        self.name = name
    
    def play(self):
        print("воспроизведение видео")

class YouTube:
    videos = []
    
    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)
    
    @classmethod
    def play(cls, video_indx):
        return Video.play(cls.videos[video_indx])

yt = YouTube()
yt.add_video("Pidor.avi")
yt.add_video("Anus.3gp")
yt.play(1)
# yt.play(1)