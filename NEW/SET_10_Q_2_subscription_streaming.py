class ConcurrentStreamsExceededError(Exception):
    pass


class Subscription:
    def stream_video(self):
        pass


class BasicPlan(Subscription):
    def __init__(self):
        self.active_streams = 1

    def stream_video(self):
        if self.active_streams >= 2:
            raise ConcurrentStreamsExceededError
        print("Streaming in 720p")


class PremiumPlan(Subscription):
    def stream_video(self):
        print("Streaming in 4K")


try:
    user = BasicPlan()
    user.active_streams = 2
    user.stream_video()

except ConcurrentStreamsExceededError:
    print("Upgrade to Premium for more streams")