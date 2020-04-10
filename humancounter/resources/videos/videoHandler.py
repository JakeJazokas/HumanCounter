from humancounter.utils.filehandler import fetch_file_path

bnn_video = 'bnn.mkv'
pedestrians_video = 'pedestrians.avi'

def pedestrians():
    return fetch_file_path(__file__, pedestrians_video)