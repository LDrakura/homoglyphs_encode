import sys


class encoder(object):

  homoglyphs = {

       'a': ['а'],
       'b': [],
       'c': ['ϲ', 'с'],
       'd': ['ԁ'],
       'e': ['е'],
       'f': [],
       'g': ['ɡ'],
       'h': ['һ'],
       'i': ['Ꭵ', 'і'],
       'j': ['ј', 'ϳ'],
       'k': ['ĸ'],
       'l': ['ⅼ', 'ӏ'],
       'm': ['ⅿ'],
       'n': [],
       'o': ['о', 'ο'],
       'p': ['р'],
       'q': [],
       'r': ['г'],
       's': ['ѕ'],
       't': [],
       'u': ['υ'],
       'v': ['ⅴ', 'ѵ', 'ν'],
       'w': ['ѡ'],
       'x': ['х'],
       'y': ['у','γ'],
       'z': [],
       'A': ['Α'],
       'B': ['Β'],
       'C': [],
       'D': ['Ɗ'],
       'E': ['Ε'],
       'F': [],
       'G': [],
       'H': ['Η'],
       'I': ['Ι'],
       'J': [],
       'K': ['Κ'],
       'L': ['Ŀ','Ľ'],
       'M': ['Μ'],
       'N': ['Ν'],
       'O': ['Ο'],
       'P': ['Ρ'],
       'Q': [],
       'R': ['Ɍ'],
       'S': [],
       'T': ['Τ'],
       'U': [],
       'V': [],
       'W': [],
       'X': [],
       'Y': ['Ƴ', 'Υ'],
       'Z': ['Ζ'],
   }

  '''
  Execute the program.
  '''

  def execute(self, target):

    idns = {}
    oldidns = {}

    idns = self.replace_homoglyphs({target:0})
    while not set(oldidns.keys()) == set(idns.keys()):
      oldidns = idns
      idns = self.replace_homoglyphs(idns)

    idns.pop(target)
    for idn,count in idns.items():
      print(idn,count)
      #print(idn,count)

  def replace_homoglyphs(self, old):
    new = old.copy()
    for d,c in old.items():
      for i in range(0,len(d)):
        for character in self.homoglyphs:
          if d[i] == character:
            for glyph in self.homoglyphs[character]:
              icopy = u''
              icopy = (d[:i] + glyph + d[i+1:])
              new[icopy] = c+1
              
    return new

if __name__=='__main__':
    target = sys.argv[1]
    program = encoder()
    program.execute(target)
