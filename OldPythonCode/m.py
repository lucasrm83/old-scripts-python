import sl4a

droid = sl4a.Android()
message = droid.dialogGetMessage('TTS', 'What would you like to say?').result
droid.ttsSpeak(message)
