from stl_backend.config.configuration import Settings
import whisperx
import gc
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torchaudio


class STTModel:
    def __init__(self):
        self.HF_TOKEN = Settings.HF_TOKEN
        self.__device = "cuda"
        self.__batch_size = 16
        self.__compute_type = "float16"
    
    def __load_model(self, audio_file):
        audio = whisperx.load_audio(audio_file)
        model = whisperx.load_model("large-v2", self.__device, compute_type=self.__compute_type)
        result = model.transcribe(audio, batch_size=self.__batch_size)
        print("Before alignment:", result["segments"])
        print(result["segments"]) # before alignment
        return result, result["segments"], audio
    
    def __align(self,result, segments, audio):
        model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=self.__device)
        result = whisperx.align(segments, model_a, metadata, audio, self.__device, return_char_alignments=False)
        print(result)
        return result
    
    def __diarize(self, audio):
        diarize_model = whisperx.DiarizationPipeline(use_auth_token=self.HF_TOKEN, device=self.__device)
        diarize_segments = diarize_model(audio, min_speakers=2, max_speakers=2)
        print(diarize_segments)
        print("Unique speakers:", diarize_segments.speaker.unique())
        return diarize_segments
    
    def __assign_word_speakers(self, diarize_segments, result):
        result = whisperx.assign_word_speakers(diarize_segments, result)
        print(diarize_segments)
        print(result["segments"])
        return result
    
    def __save_result(self, result):
        with open("result.txt", "w") as f:
            for result in result["segments"]:
                f.write(result["speaker"] + " " + str(result["start"]) + " " + result["text"] + "\n")
        print("Result saved to result.txt")
    
    def main(self, audio_file):
        result, segments, audio = self.__load_model(audio_file)
        result = self.__align(result, segments, audio)
        diarize_segments = self.__diarize(audio)
        result = self.__assign_word_speakers(diarize_segments, result)
        self.__save_result(result)
        
class STTModelWithoutDia:
    def __init__(self):
        self.MODEL_ID = Settings.MODEL_ID
        self.__device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.__torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    
    def __load_model(self):
        self.__model = AutoModelForSpeechSeq2Seq.from_pretrained(self.MODEL_ID, torch_dtype=self.__torch_dtype, 
                                                                 low_cpu_mem_usage=True, use_safetensors=True)
        return self.__model
    
    def __load_audio_file(self, file_path):
        waveform, sample_rate = torchaudio.load(file_path)
        # If the audio has multiple channels, select the first channel
        if waveform.shape[0] > 1:
            waveform = waveform[0]
        return {"raw": waveform.numpy(), "sampling_rate": sample_rate}
    
    def __transcribe(self, sample):
        model = self.__load_model()
        model.to(self.__device)
        processor = AutoProcessor.from_pretrained(self.MODEL_ID)
        pipe = pipeline("automatic-speech-recognition", model=model, tokenizer=processor.tokenizer,
                        feature_extractor=processor.feature_extractor, max_new_tokens=128, chunk_length_s=30,
                        batch_size=16, return_timestamps=True, torch_dtype=self.__torch_dtype, device=self.__device)
        sample = self.__load_audio_file(sample)
        result = pipe(sample)
        return result["text"]
    
    def main(self, audio_file):
        result = self.__transcribe(audio_file)
        return result
        
    
    
    
    
        
        
if __name__ == "__main__":
    # model = STTModel()
    # model.main(r"D:\Study\github\STT_Interview_Feedback_system\audio.wav")
    model = STTModelWithoutDia()
    result = model.main(r"D:\Study\github\STT_Interview_Feedback_system\com_backend\podcast.mp3")
        
    
    
    

        
        
        
