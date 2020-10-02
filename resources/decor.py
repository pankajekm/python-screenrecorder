#decorators for functions

def audio_record_thread(func):
    def inner(s):    
        print("Pyaudio: Started Recording Audio")
        func(s)
        print("Pyaudio: Stopped Recording Audio")
        return
    return inner