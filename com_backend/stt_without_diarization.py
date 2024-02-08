import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
import warnings
import torchaudio

mp3_file_path = "D:\Study\github\STT_Interview_Feedback_system\com_backend\podcast.mp3"

def load_audio_file(file_path):
    waveform, sample_rate = torchaudio.load(file_path)
    # If the audio has multiple channels, select the first channel
    if waveform.shape[0] > 1:
        waveform = waveform[0]  # Select the first channel
    
    return {"raw": waveform.numpy(), "sampling_rate": sample_rate}

device = "cuda:0" if torch.cuda.is_available() else "cpu"
print(device)
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
model_id = "openai/whisper-large-v3"
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)
processor = AutoProcessor.from_pretrained(model_id)
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)

sample = load_audio_file(mp3_file_path)
result = pipe(sample)
print("\n")
print(result["text"])
