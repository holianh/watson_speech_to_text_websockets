import os
from watson_speech_to_text_websockets import WSSpeechToTextV1

recordings = ["./recordings/{0}".format(x)
              for x
              in os.listdir('./recordings')]

username, password = os.getenv('STT_CREDENTIALS').split(':')

ws = WSSpeechToTextV1(username=username, password=password)
results = ws.recognize(file_name=recordings[0],
                       content_type="audio/wav",
                       keywords_threshold=0.6,
                       keywords=['officials'],
                       content_callback=lambda x: print(x))

print(results)

with open(recordings[1], 'rb') as audiofile:
    results = ws.recognize(file_object=audiofile,
                           content_type="audio/wav",
                           content_callback=lambda x: print(x))
    print(results)