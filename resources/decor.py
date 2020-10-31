# decorators for functions

def audio_record_thread(func):
    def inner(s):
        print("AudioCapture: Started Recording Audio")
        func(s)
        print("AudioCapture: Stopped Recording Audio")
        return
    return inner


def file_saving(func):
    def wrap(filename):
        print("Saving file...")
        func(filename)
        print("File saved")
        return
    return wrap
