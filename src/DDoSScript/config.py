class Config():
    def __init__(self):
        self.ATKIPv4 = '192.168.52.73'
        self.ATKPARAMETERS = [
            ('  ', 1e9, '--flood', 0),
            ('-0', 1e9, '--flood', 0),
            ('-1', 1e9, '--flood', 2),
            ('-2', 1e9, '--flood', 2),
        ]
        '''
        (mode, data, freq, processes)
        Recommand to use the total number of processes equal to the number of CPU cores.
        '''
