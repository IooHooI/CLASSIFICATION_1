import pandas as pd


class DataLoader:

    def __init__(self, data_paths, columns_path, classes_path):
        self._data_paths = data_paths
        with open(columns_path, 'r') as source:
            columns = source.readlines()
        with open(classes_path, 'r') as source:
            classes = source.readlines()
        classes = [class_.split(' ') for class_ in classes]
        self._classes_map = dict([(' '.join(class_[0:-1]), int(class_[-1])) for class_ in classes])
        self._columns = [column.replace('\n', '') for column in columns]

    def load(self):
        data_frames = [self._load_data(data_path) for data_path in self._data_paths]
        return pd.concat(data_frames)

    def _load_data(self, data_path):
        with open(data_path, 'r') as source:
            lines = source.readlines()
            data = [line.split(',') for line in lines]
            for observation in data:
                observation[-1] = observation[-1].split('.|')[0]
                self._cast_function(observation)
        data_frame = pd.DataFrame(data=data, columns=self._columns)
        return data_frame

    def _cast_function(self, observation):
        for i in range(len(observation)):
            if observation[i] == 'f':
                observation[i] = False
            elif observation[i] == 't':
                observation[i] = True
        if observation[0] != '?':
            observation[0] = int(observation[0])
        else:
            observation[0] = None
        if observation[1] == '?':
            observation[1] = None
        observation[-1] = self._classes_map[observation[-1]]
        self._to_float(observation, 17)
        self._to_float(observation, 19)
        self._to_float(observation, 21)
        self._to_float(observation, 23)
        self._to_float(observation, 25)
        self._to_float(observation, 27)

    def _to_float(self, observation, index):
        if observation[index - 1]:
            observation[index] = float(observation[index])
        else:
            observation[index] = None
