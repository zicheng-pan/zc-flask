class ExecFunc:
    def __init__(self, func, func_type, **options):
        self.func = func  # operation method
        self.func_type = func_type  # route 、view 、static
        self.options = options  # arguments
