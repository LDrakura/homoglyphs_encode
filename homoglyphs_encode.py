import sys


class encoder(object):

  homoglyphs = {

      'a': ['а'],
       'b': ['ᖯ'],
       'c': ['ϲ', 'с'],
       'd': ['ԁ', '𝖽'],
       'e': ['е'],
       'f': ['𝖿', '𝗳'],
       'g': ['ɡ', 'ց'],
       'h': ['һ'],
       'i': ['і'],
       'j': ['ј', 'ϳ'],
       'k': ['ĸ', 'ꮶ'],
       'l': ['ⅼ'],
       'm': ['ⅿ','𝗆'],
       'n': ['ո'],
       'o': ['о', 'ο'],
       'p': ['р'],
       'q': ['𝗊'],
       'r': ['г'],
       's': ['ѕ'],
       't': ['𝚝'],
       'u': ['𝗎', 'ս'],
       'v': ['ⅴ', 'ѵ', 'ᴠ'],
       'w': ['𝗐'],
       'x': ['х', 'ⅹ'],
       'y': ['у', 'ꭹ'],
       'z': [],
       'A': ['Α'],
       'B': ['Β'],
       'C': ['ꓚ'],
       'D': ['Ⅾ', '𝙳'],
       'E': ['Ε'],
       'F': ['ꓝ'],
       'G': ['𝖦'],
       'H': ['Η'],
       'I': ['Ι'],
       'J': ['Ꭻ'],
       'K': ['Κ'],
       'L': ['Ⳑ', 'ꓡ'],
       'M': ['Μ'],
       'N': ['Ν'],
       'O': ['Ο'],
       'P': ['Ρ'],
       'Q': [],
       'R': ['R', 'Ꭱ'],
       'S': ['𝗦', 'Ѕ'],
       'T': ['Τ', 'Ꭲ'],
       'U': ['∪', '𝖴'],
       'V': ['ⴸ'],
       'W': [],
       'X': ['Ⲭ'],
       'Y': ['Ƴ', 'Υ', '𐊲'],
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
