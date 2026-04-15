class CodecNotSupportedError(Exception):
    pass


class MobilePlayer:
    def play_video(self, file):
        try:
            if file == ".mkv":
                raise CodecNotSupportedError
            print("MobilePlayer: Playing in 1080p")
        except CodecNotSupportedError:
            print("MobilePlayer: Codec not supported")


class TVPlayer:
    def play_video(self, file):
        print("TVPlayer: Playing in 4K")


players = [(MobilePlayer(), ".mp4"), (MobilePlayer(), ".mkv"), (TVPlayer(), ".mkv")]

for player, file in players:
    player.play_video(file)