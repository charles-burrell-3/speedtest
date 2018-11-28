import dateutil
import pandas as pd

from configs import filename
from speedtest_objects import SpeedTestRows


#@app.route('/results')
def get_aggregated_results():
    def prepare_report(input_data_frame):
        def get_data(metric, data_frame):
            lowered = metric.lower()
            return [metric, data_frame[lowered].min(), data_frame[lowered].max(), data_frame[lowered].mean()]

        output_df_columns = headers
        ping_data = get_data('Ping', input_data_frame)
        upload_data = get_data('Upload', input_data_frame)
        download_data = get_data('Download', input_data_frame)
        return pd.DataFrame(columns=output_df_columns, dtype=float, data=[ping_data, upload_data, download_data])

    headers = ['Metric', 'Min', 'Max', 'Mean']
    output_data_frame = pd.read_csv(filename)
    speedtest_rows = SpeedTestRows(output_data_frame)
    time_of_test = output_data_frame['time'].max()
    formatted_date_time_of_test = dateutil.parser.parse(time_of_test).strftime('%H:%M %A, %d %B %Y')
    # return render_template('metrics.html', 'headers' = headers, 'metrics' = speedtest_rows, 'title' = 'Report for %s' % formatted_date_time_of_test)


def get_results_table():
    headers = ['Time', 'Ping', 'Upload', 'Download']
    output_data_frame = pd.read_csv(filename)
    speedtest_rows = SpeedTestRows(output_data_frame)
    # return render_template('data.html', 'headers' = headers, 'rows' = speedtest_rows, 'title' = 'Data Dump')