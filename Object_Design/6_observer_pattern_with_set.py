class Subcriber(object):
    def __init__(self, name):
        self.name=name

    def update(self,message):
        print("{0}, {1}".format(self.name, message))


class Publisher(object):
    def __init__(self):
        self.subscribers=set()

    def register(self,who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self,message):
        for subscriber in self.subscribers:
            subscriber.update(message)

if __name__ == "__main__":
    pub = Publisher()

    astin = Subcriber("아스틴")
    james = Subcriber("제임스")
    jeff = Subcriber("제프")

    pub.register(astin)
    pub.register(james)
    pub.register(jeff)

    pub.dispatch("점심시간입니다.")
    pub.unregister(jeff)
    pub.dispatch("퇴근시간입니다.")

    