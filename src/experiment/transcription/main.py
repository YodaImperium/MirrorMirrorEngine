from models import transcribe_audio
audio_file_path = "C:/Users/asus/Documents/GitHub/MirrorMirrorEngine/src/experiment/transcription/test.mp3"
transcribe_audio(audio_file_path, None, "whisper_base", None, "EN", 1)