## turkish-tokenizers

This repo contains tokenizer models for Turkish language trained with `Sentence Piece` by `Google`. Available vocabulary sizes are 10k, 16k, 20k and 32k. The input text was cleaned and deduplicated Oscar corpus in Turkish. I will publish BPE tokenizers trained with the `tokenizers` package quite soon.

## TODO
- [ ] Rewrite a better `spm_train.py` configureable with command line arguments.
- [ ] Publish BPE tokenizers and `bpe_train.py`.
- [ ] Write a better `readme.md` to explain the purpose, motivation and how to use it.
