//para ver vocab.json
uv run python -c "from llm_sdk import Small_LLM_Model; Small_LLM_Model('Qwen/Qwen3-0.6B'); print('ok')"

uv run python -c "
import json, glob
from src.vocabulary import Vocabulary
p = glob.glob('/goinfre/pmarcos-/hf_cache/hub/models--Qwen--Qwen3-0.6B/snapshots/*/vocab.json')[0]
raw = json.load(open(p, encoding='utf-8'))
v = Vocabulary(p, 151643)
inv = {i: t for t, i in raw.items()}
for i in [220, 198, 279, 1782, 0, 15]:
    print('%6d  json=%-12r real=%r' % (i, inv.get(i), v.text(i)))
"

//bibliografia:
https://huggingface.co/learn/llm-course/es/chapter6/5 - bpe (bytes_to_unicode)