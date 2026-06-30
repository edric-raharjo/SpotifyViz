import faiss
import numpy as np
import pydub
import torch
from sentence_transformers import SentenceTransformer
from transformers import BitsAndBytesConfig

quantization_setting = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

model = SentenceTransformer(
    "LCO-Embedding/LCO-Embedding-Omni-3B",
    model_kwargs={
        "torch_dtype": torch.bfloat16,
        "attn_implementation": "flash_attention_2",
        "quantization_config": quantization_setting,
    },
)


def chop_audio_to_10s(audio_path) -> list:
    chopped_audios_filenames = []

    audio_format = pydub.AudioSegment.from_mp3(audio_path)

    slice_count = np.ceil(len(audio_format) / 10000)

    for i in range(0, int(slice_count)):
        start_idx = 10000 * i
        end_idx = 10000 * (i + 1)
        file_path = audio_path.replace(".mp3", f"_{i}.mp3")
        audio_format[start_idx, end_idx].export(file_path, format="mp3")
        chopped_audios_filenames.append(file_path)

    return chopped_audios_filenames


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def generate_vectors(audio_tracks: list, faiss_index_path: str):

    faiss_vdb = faiss.IndexFlatIP(d=2048)

    for audio_path in audio_tracks:
        if not audio_path.endswith(".mp3"):
            raise ValueError("Must be .mp3 file")
        else:
            chopped_audios = chop_audio_to_10s(audio_path)

        encoded_audio = model.encode(
            chopped_audios, batch_size=1
        )  # How do I batch? Or I can't? Anyway, that isn't important, I only have 8GB VRAM

        faiss_vdb.add(encoded_audio.astype("float32"))

    # Save to FAISS after done iterating
    faiss.write_index(faiss_vdb, faiss_index_path)


if __name__ == "__main__":
    main()
