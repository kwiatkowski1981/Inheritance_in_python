class Airplane:
    def __init__(self, model, engines=2):
        self.model = model
        self.engines = engines

    def engine_on(self, engine):
        pass

    @classmethod
    def get_ready(cls, model):
        sample_plane = cls(model, 3)
        sample_plane.engine_on(0)
        sample_plane.engine_on(1)
        sample_plane.engine_on(2)
        return sample_plane
