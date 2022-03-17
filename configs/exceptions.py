class StageWrongValueError(Exception):
    def __init__(self, stage_value: str):
        self.message = f'''Environment variable 'STAGE' has value='{stage_value}' which is not supported.''' \
                       '''Please set one of ['dev', 'prod']'''
        super().__init__(self.message)
