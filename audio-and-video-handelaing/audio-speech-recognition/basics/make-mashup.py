from pydub import AudioSegment

audio = AudioSegment.from_wav("audio/onetofive.wav")
# audio = AudioSegment.from_mp3("mashup.mp3")

# boost volume by 6dB
audio = audio + 6

# repeat the clip twice
audio = audio * 2

# 2 sec fade in
audio = audio.fade_in(2000)

audio.export("audio/mashup.mp3", format="mp3")
