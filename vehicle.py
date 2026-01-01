
from collections import deque

class Vehicle:
    """Clase simple para representar un vehículo detectado."""
    def __init__(self, id, initial_centroid, bbox=None, maxlen=5):
        self.id = id
        self.path = deque([initial_centroid], maxlen=maxlen)
        self.bbox = bbox

    def update(self, centroid, bbox=None):
        self.path.append(centroid)
        if bbox is not None:
            self.bbox = bbox

    def last_centroid(self):
        return self.path[-1]

    def prev_centroid(self):
        return self.path[-2] if len(self.path) >= 2 else None