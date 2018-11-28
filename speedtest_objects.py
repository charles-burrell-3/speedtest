import dateutil


class SpeedTestRows:
    def __init__(self, dataframe):
        def get_data(metric):
            lowered = metric.lower()
            return SpeedTestMetric(metric, self.dataframe[lowered].min(), self.dataframe[lowered].max(),
                                   self.dataframe[lowered].mean())

        self.dataframe = dataframe
        self.rows = []
        self.ping_metrics = get_data('ping')
        self.upload_metrics = get_data('upload')
        self.download_metrics = get_data('download')

        for index in range(0, len(self.dataframe.index)):
            ping = self.dataframe['ping'][index]
            upload = self.dataframe['upload'][index]
            download = self.dataframe['download'][index]
            time = self.dataframe['time'][index]
            formatted_time = dateutil.parser.parse(time).strftime('%H:%M %A, %d %B %Y')
            self.rows.append(SpeedTestRow(formatted_time, ping, upload, download))

    def rows(self, index=0, page_size=25):
        start = index * page_size
        end = start + page_size
        return self.rows[start:end]


class SpeedTestMetric:
    def __init__(self, name, minimum, mean, maximum):
        self.name = name
        self.min = minimum
        self.mean = mean
        self.max = maximum


class SpeedTestRow:
    def __init__(self, time, ping, upload, download):
        self.time = time
        self.ping = ping
        self.upload = upload
        self.download = download

    def __str__(self):
        return 'Ping: %s Upload: %s Download: %s\n' % (self.ping, self.upload, self.download)
