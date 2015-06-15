def filter_insignificant(chunk, tag_suffixes=['DT', 'CC', 'PRP','MD','VB', 'VBN','TO','RB','PRPS']):
  good = []
  
  for word, tag in chunk:
    ok = True
    
    for suffix in tag_suffixes:
      if tag.endswith(suffix):
        ok = False
        break
    
    if ok:
      good.append((word, tag))
  
  return good



plural_verb_forms = {
  ('is', 'VBZ'): ('are', 'VBP'),
  ('was', 'VBD'): ('were', 'VBD')
}

singular_verb_forms = {
  ('are', 'VBP'): ('is', 'VBZ'),
  ('were', 'VBD'): ('was', 'VBD')
}



def first_chunk_index(chunk, pred, start=0, step=1):
  l = len(chunk)
  end = l if step > 0 else -1
  
  for i in range(start, end, step):
    if pred(chunk[i]):
      return i
  
  return None

def correct_verbs(chunk):
  vbidx = first_chunk_index(chunk, lambda (word, tag): tag.startswith('VB'))
  # if no verb found, do nothing
  if vbidx is None:
    return chunk
  
  verb, vbtag = chunk[vbidx]
  nnpred = lambda (word, tag): tag.startswith('NN')
  # find nearest noun to the right of verb
  nnidx = first_chunk_index(chunk, nnpred, start=vbidx+1)
  # if no noun found to right, look to the left
  if nnidx is None:
    nnidx = first_chunk_index(chunk, nnpred, start=vbidx-1, step=-1)
  # if no noun found, do nothing
  if nnidx is None:
    return chunk
  
  noun, nntag = chunk[nnidx]
  # get correct verb form and insert into chunk
  if nntag.endswith('S'):
    chunk[vbidx] = plural_verb_forms.get((verb, vbtag), (verb, vbtag))
  else:
    chunk[vbidx] = singular_verb_forms.get((verb, vbtag), (verb, vbtag))
  
  return chunk  


def swap_verb_phrase(chunk):
  # find location of verb
  vbpred = lambda (word, tag): tag != 'VBG' and tag.startswith('VB') and len(tag) > 2
  vbidx = first_chunk_index(chunk, vbpred)
  
  if vbidx is None:
    return chunk
  
  return chunk[vbidx+1:] + chunk[:vbidx]  


def swap_noun_cardinal(chunk):
  cdidx = first_chunk_index(chunk, lambda (word, tag): tag == 'CD')
  # cdidx must be > 0 and there must be a noun immediately before it
  if not cdidx or not chunk[cdidx-1][1].startswith('NN'):
    return chunk

  noun, nntag = chunk[cdidx-1]
  chunk[cdidx-1] = chunk[cdidx]
  chunk[cdidx] = noun, nntag
  return chunk



def swap_infinitive_phrase(chunk):
  inpred = lambda (word, tag): tag == 'IN' and word != 'like'
  inidx = first_chunk_index(chunk, inpred)
  
  if inidx is None:
    return chunk
  
  nnpred = lambda (word, tag): tag.startswith('NN')
  nnidx = first_chunk_index(chunk, nnpred, start=inidx, step=-1) or 0
  
  return chunk[:nnidx] + chunk[inidx+1:] + chunk[nnidx:inidx]  


def singularize_plural_noun(chunk):
  nnspred = lambda (word, tag): tag == 'NNS'
  nnsidx = first_chunk_index(chunk, nnspred)
  
  if nnsidx is not None and nnsidx+1 < len(chunk) and chunk[nnsidx+1][1][:2] == 'NN':
    noun, nnstag = chunk[nnsidx]
    chunk[nnsidx] = (noun.rstrip('s'), nnstag.rstrip('S'))
  
  return chunk