class CorruptAudioFileError(Exception):
    pass


class BassBoost:
    def apply_effect(self, ok):
        try:
            if not ok:
                raise CorruptAudioFileError
            print("Bass Boost applied")
        except CorruptAudioFileError:
            print("Error: Corrupt audio file")


class NoiseReduction:
    def apply_effect(self, ok):
        try:
            if not ok:
                raise CorruptAudioFileError
            print("Noise reduced")
        except CorruptAudioFileError:
            print("Error: Corrupt audio file")


effects = [(BassBoost(), True), (NoiseReduction(), True), (BassBoost(), False)]

for effect, status in effects:
    effect.apply_effect(status)