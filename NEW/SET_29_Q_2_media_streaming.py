class CodecNotSupportedError(Exception):
    pass


class VideoPlayer:
    def play_video(self, format):
        pass


class MobilePlayer(VideoPlayer):
    def play_video(self, format):
        if format == ".mkv":
            raise CodecNotSupportedError
        print("Playing in 1080p")


class TVPlayer(VideoPlayer):
    def play_video(self, format):
        print("Playing in 4K")


try:
    p = MobilePlayer()
    p.play_video(".mkv")

except CodecNotSupportedError:
    print("Format not supported on mobile")