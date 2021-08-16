def bucketize(sentence, bucket_limit):
    bucket = ['']
    i = 0
    for word in sentence.split():
        if len(bucket[i] + ' ') + len(word) <= bucket_limit:
            bucket[i] += ' ' + word
        elif len(word) <= bucket_limit:
            bucket.append(word)
            i += 1
    return bucket if bucket[0] != '' else []
        
print(bucketize("she sells sea shells by the sea", 10))
print(bucketize("the mouse jumped over the cheese", 7))
print(bucketize("fairy dust coated the air", 20))
print(bucketize("a b c d e", 2))