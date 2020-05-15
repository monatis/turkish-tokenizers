import sentencepiece as spm

max_tokens = 1 ## thousands

spm.SentencePieceTrainer.Train('--input=tr_dedup.txt --model_prefix=tr_dedup_{}k --vocab_size={}'.format(max_tokens, max_tokens * 1000))
tokenizer = spm.SentencePieceProcessor()
tokenizer.load('tr_dedup_{}k.model'.format(max_tokens))
input = "İzmir'in dağlarında çiçekler açar, altın güneş orada sırmalar saçar."
pieces = tokenizer.EncodeAsPieces(input)
ids = tokenizer.encode_as_ids(input)
decoded_input = tokenizer.DecodeIds(ids)

print(input)
print(pieces)
print(ids)
print(decoded_input)