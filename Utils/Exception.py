"""Utils file for implementation a exception methods"""


"""Att: 2021-09-25"""


class Error_in_execution_time(Exception):
    type_error = 'default'
    description_error = ''
    switch = {'default': 'Generic error!',
              'runtime': 'Dated error in runtime process!',
              'spider_exists': 'spider already exists in the current directory',
              'thread_Spider': 'Spider creation error'}

    def __init__(self, type_error) -> object:
        self.type_error = type_error
        self.description_error = self.switch.get(type_error)

    def __str__(self):
        return f'{self.type_error} -> {self.description_error }'