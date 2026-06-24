import torch
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "LCO-Embedding/LCO-Embedding-Omni-3B",
    model_kwargs={
        "torch_dtype": torch.bfloat16,
        "attn_implementation": "flash_attention_2",  
    },
)

def main():
    pass

if __name__ == "__main__":
    main()