*This project has been created as part of the 42 curriculum by <pmarcos->.*

# Call Me Maybe

## Description

This project takes a sentence written in plain language and turns it into a
function call. If you ask it "What is the sum of 40 and 2?", it does not answer
42: it tells you which function should be called and with which arguments.

```json
{"prompt": "What is the sum of 40 and 2?", "name": "fn_add_numbers", "parameters": {"a": 40.0, "b": 2.0}}
```

Underneath it uses Qwen3-0.6B, a small model. If you just ask it for JSON, it
often gets it wrong. The fix is not to ask more nicely, it is to not let it go
wrong: at every step of the generation I work out which characters can come next
according to the function definitions, and I only let through the tokens that
fit. The model decides which function to call and which values to use; the
grammar only decides what counts as valid JSON.

## Installation

You need Python 3.10 or later, `uv`, and the `llm_sdk/` folder copied next to
`src/`.

```bash
uv sync
```

The first run downloads the model and takes a few minutes. After that it comes
from the cache.

`setup.sh` is optional and only useful on the campus machines: it moves the cache
and the environment to `/goinfre` so the download does not fill up the home
quota. The project works fine without it.

## Makefile targets

- `make install` — install the dependencies
- `make run` — run the program with the default paths
- `make debug` — run it under `pdb`
- `make lint` — run `flake8` and `mypy`
- `make clean` — remove `__pycache__`, `.mypy_cache` and the generated output

## How to use it

By default it reads from `data/input/` and writes to `data/output/`:

```bash
uv run python -m src
```

With your own paths:

```bash
uv run python -m src \
  --functions_definition data/input/functions_definition.json \
  --input data/input/function_calling_tests.json \
  --output data/output/function_calling_results.json
```

It also accepts `--model` if you want to try a different model.

The result is a JSON file with one entry per prompt:

```json
[
  {
    "prompt": "What is the sum of 2 and 3?",
    "name": "fn_add_numbers",
    "parameters": {"a": 2.0, "b": 3.0}
  }
]
```

If one prompt fails, the program does not stop. It reports the problem on stderr,
writes that entry with an empty name, and carries on with the rest.

## How it works

### The grammar

I build one template per function. For example, for
`fn_add_numbers(a: number, b: number)`:

```
'{"name": "fn_add_numbers", "parameters": {"a": '  <number>  ', "b": '  <number>  '}}'
```

The fixed pieces of text are matched character by character. The gaps for the
values are small automata, one per type. The number one knows the JSON grammar,
so it accepts `-1.5e10` but rejects `01` or `2.`. The string one keeps track of
the quotes, the backslash escapes and the four digits of a `\u` sequence.

The important part is that I do not work with one template, but with all of them
at once. I keep a set of positions, one per function, and I drop the ones that no
longer fit. By the time the model has written `{"name": "fn_g`, only the functions
that start that way are still alive. **The model picks the function with its own
probabilities**, I only cross out the ones that have become impossible.

### The generation loop

At each step one of two things happens.

**Either the next character is already decided.** After
`{"name": "fn_add_numbers"`, the text `, "parameters": {"a": ` is the only thing
that can follow. I write it straight out without asking the model anything. This
is what speeds the program up the most: most of a call is fixed structure and it
comes for free.

**Or there are several options.** Then I do ask for the logits, sort the
vocabulary from highest to lowest score and walk down it: I skip the tokens the
grammar does not accept here and keep the first one that fits. If another token
with a similar score (within a margin of 6) says the same thing but longer, I
prefer that one: writing `numbers` in one go instead of `n` saves several passes.

### Token healing

When I write forced text directly, the cut can land somewhere the tokenizer would
never have cut. If I re-encode the text as it is, the model gets a tokenization it
has never seen and its predictions get noticeably worse.

What I do is this: after writing forced text, I re-encode everything and look at
the last token. If that token sits in the middle of a word, I strip it off the end
and turn it into a condition: the next token has to start with those letters and
add something to them. That way the model decides those characters again with a
tokenization it recognises. If no token fits, I ask again without the trick.
Healing can never be the reason something fails.

### The final check

The grammar guarantees the JSON is well formed, but not that it makes sense. So
`parse_call` checks everything again: that the function exists, that exactly the
right arguments are there, and that each value has the declared type. I widen
integers to floats when the parameter is a `number`, which is the format the
subject asks for.

## Decisions I made

**The prompt is short on purpose.** Every prompt token is re-encoded on every
pass, and there is one pass per generated token, so if the prompt grows the whole
run pays for it. That is why I only include each function's signature. I add the
description only when two names share their first four letters, which is when the
model has to decide early and with little to go on.

**I close the thinking block before it starts.** Qwen3 writes a `<think>` section
before answering. If I leave it open it starts writing text that the grammar has
to reject, and those are wasted passes. I hand it the block already closed and
empty, so it starts exactly where the JSON starts.

**Nothing is hardcoded.** The grammar is built from
`functions_definition.json`. If you add a function to the file, the program
accepts it with no code change, which is exactly what the subject asks for when it
warns that the input files may change during the review.

**The decoder knows nothing about the SDK.** It only needs `encode` and `logits`,
declared as a `Protocol`. That is what lets me test it with a fake model, without
downloading any weights.

## Performance

`bench.py` measures the cost of each call. Run it from the root of the repo:

    uv run python bench.py

It prints one line per prompt with the number of forward passes, the time it
took, and the call that came out:

     12 fwd     3.4s  {"name": "fn_greet", "parameters": {"name": "shrek"}}

and then the totals: forward passes, total time, and average time per pass.

The number of passes is the interesting figure. A call is around 50 to 60
characters, but most of them are structure that the grammar fills in on its own
without asking the model, so the count stays far below that. The time per pass
depends entirely on the machine — it is CPU bound and single batch.

My results on <machine, number of threads>:

- **__** forward passes per call on average
- **__ s** per call
- **__ s** per forward pass

Note that `bench.py` measures cost, not correctness: it prints the generated call
but does not judge it. For accuracy I run the program normally and check
`data/output/function_calling_results.json` against the requests. On the provided
test file: **__ out of __** correct.

## Problems I ran into

**Tokens that cross two pieces of the template.** At first I matched character by
character and rejected any token that straddled a fixed piece and the next one,
which ruled out almost every useful token. I fixed it by letting a position that
has finished its piece carry on into the next one within the same character.

**Knowing when a number ends.** A number has no end marker: it ends when the next
character arrives. I had to make the automaton say which states it can finish in,
so I could combine its characters with those of the following piece. Otherwise
`16` could never be followed by `}}`.

**Quotes inside an argument.** If the request contains a quote, the token holding
it is not valid inside a JSON string. What I do is retry the same token with the
quote escaped, so the value survives instead of the generation breaking.

**The one that cost me the most: tokenization.** The JSON came out perfect but the
argument values were slightly wrong. It took me a while to see that the problem
was where the forced text was cut, which is what became the token healing. You can
only see it by looking at the logits step by step, which is what I wrote
`debug.py` for.

## Testing

`test_grammar.py` tests the part where the real difficulty is:

- that every template produces valid JSON according to its own definition;
- a list of strings that must be accepted (negatives, exponents, escaped quotes,
  several arguments) and another of strings that must be rejected (function that
  does not exist, leading zeros, wrong type, unescaped newline, one brace too
  many);
- the edge cases: tokens crossing pieces, numbers that close right on the
  delimiter, a function with no arguments;
- the whole decoder with a fake model and a fake vocabulary, so I can test the
  logic without loading the model.

`bench.py` counts passes and time. `debug.py` shows the prompt, how many tokens it
takes, and the most likely tokens at each point, with and without the grammar.

On top of that, `flake8` and `mypy` with `make lint`.

## Resources

- Willard and Louf, *Efficient Guided Generation for Large Language Models*
  (2023), where the idea of seeing the grammar as an automaton comes from.
- [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259), the JSON specification.
- [Qwen3 documentation](https://qwenlm.github.io/blog/qwen3/), for the chat
  template and the thinking block.
- The documentation of `outlines` and of GBNF in `llama.cpp`, read only to
  understand the problem. I do not use either of them.
- [The bytes_to_unicode concept](https://huggingface.co/learn/llm-course/es/chapter6/5).

### Use of AI

I used AI at three points in this project.

**To understand the problem.** Constrained decoding, and the idea of expressing a
JSON schema as a set of finite automata, were new to me. I used Claude to work
through how the technique is normally implemented before writing anything.

**On the core code.** The grammar (the templates, the value automata, the set of
cursors) and the decoder (the token search, the forced text, the token healing)
were written with AI assistance. I read through both, traced them against the
test cases in `test_grammar.py`, and can explain every design decision in them —
see the sections above.


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