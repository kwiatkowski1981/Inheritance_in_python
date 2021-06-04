class Singleton:
    _INSTANCE = None

    @staticmethod
    def get_instance():
        if Singleton._INSTANCE is None:
            Singleton._INSTANCE = Singleton()
        return Singleton._INSTANCE


app = Singleton.get_instance()
print(app)
