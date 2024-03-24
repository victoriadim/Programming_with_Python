def start_playing(obj):
    return obj.play()


class MixinPlay:
    def play(self):
        return f"from mixin playing"


class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))


guitar = Guitar()
print(start_playing(guitar))