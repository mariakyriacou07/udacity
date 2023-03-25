import random
import words

def silly_string(nouns,verbs,templates):
    template = random.choice(templates) #Choose a random template
    output = [] # We will append strings into this list for output
    index = 0 # Keep track of where in the template string we are
    
    while index < len(template):
          if template[index:index+8] == '{{noun}}':
             output.append(random.choice(nouns))
             index += 8
          elif template[index:index+8] == '{{verb}}':
             output.append(random.choice(verbs))
             index += 8
          else:
             output.append(template[index])
             index += 1
    return "".join(output)

print(silly_string(words.nouns, words.verbs,words.templates))
       


          

