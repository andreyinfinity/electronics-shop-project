class InstantiateCSVError(Exception):
    """Исключение при поврежденном файле"""
    def __init__(self, *args, **kwargs):
        self.message = f'Файл {args[0]} поврежден'

    def __str__(self):
        return self.message
