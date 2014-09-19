_base_translations =  {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15,
            'G': 16,
            'H': 17,
            'I': 18,
            'J': 19,
            'K': 20,
            'L': 21,
            'M': 22,
            'N': 23,
            'O': 24,
            'P': 25,
            'Q': 26,
            'R': 27,
            'S': 28,
            'T': 29,
            'U': 30,
            'V': 31,
            'W': 32,
            'X': 33,
            'Y': 34,
            'Z': 35,
            'a': 10,
            'b': 11,
            'c': 12,
            'd': 13,
            'e': 14,
            'f': 15,
            'g': 16,
            'h': 17,
            'i': 18,
            'j': 19,
            'k': 20,
            'l': 21,
            'm': 22,
            'n': 23,
            'o': 24,
            'p': 25,
            'q': 26,
            'r': 27,
            's': 28,
            't': 29,
            'u': 30,
            'v': 31,
            'w': 32,
            'x': 33,
            'y': 34,
            'z': 35,
            '_': 39, 
            '-': 42}

class LCDDisplay(object):
  """ Mixin to provide LCD display """

  def display_chars(self, char1=None, char2=None):
    if char1 in _base_translations:
      self._send_midi((176, 34, _base_translations[char1]))
    if char2 in _base_translations:
      self._send_midi((176, 35, _base_translations[char2]))

  def display_num(self, number):
    number = str(number)
    if len(number) == 2:
      self._send_midi((176, 34, _base_translations[number[0]]))
      self._send_midi((176, 35, _base_translations[number[1]]))
    else:
      self._send_midi((176, 34, 0))
      self._send_midi((176, 35, _base_translations[number[0]]))
