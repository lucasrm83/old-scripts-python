import sl4a

droid = sl4a.Android()
message = droid.dialogGetInput('TTS', 'O que você gostaria de falar?').result
droid.ttsSpeak(message)
