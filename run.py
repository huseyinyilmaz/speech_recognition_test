import datetime
from os import path

import speech_recognition as sr

start = datetime.datetime.now()
# file_name = '263-seo-for-python-developers.mp3'
file_name = 'input.wav'
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), file_name)
# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    result = r.recognize_sphinx(audio)
    print("Sphinx thinks you said " + result)
    with open('result.txt', 'w') as f:
        f.write(result)

except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

end = datetime.datetime.now()
duration = end - start
print('duration = ', duration)
