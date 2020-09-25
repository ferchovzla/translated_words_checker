from enchant.checker import SpellChecker
import enchant
import re

class LanguageDetector():
    
    def __init__(self, language):
      self.language = language
      self.not_translated = set()
      self.reserved_words = ["VPN", "GOOSE VPN", "NederlandsEnglishEspañolPolskiDeutschFrançaisMagyarItaliano", "VPNProveedores", "costosoSin", "ExpressVPNNordVPNIPVanishPIACactus", "IPVanish", "España?", "ExpressVPN", "ExpressVPN★★★★★ ★★★★★", "ProtonVPN", "ExpressVPN★★★★★", "CactusVPN", "GratuitosNavegación", "Trust.Zone", "NordVPN★★★★★", "VPNExpressVPNNordVPNIPVanishPIACactus", "PIA", "RUSVPN", "NordVPN", "ArenaVision", "★★★★★ ★★★★★", "Surfshark", "Magyar", "Cyberghost", "★★★★★", "★", "Netflix", "DirectTV", "Blog", "Polski", "Español", "Français", "Deutsch", "Nederlands", "English", "NederlandsEnglishEspañolPolskiDeutschFrançaisMagyarItaliano","Italiano"]
      self.bad_chars = ["*", "?", "!", "¿", "¡", ","]
      self.words_checked = set()

    def is_in_setlanguage(self, quote):

       if len(quote) == 0: return True

       words = quote.split()

       if len(words) > 8:
          return True

       d = enchant.Dict(self.language)
       
       if len(words) > 5:
          return True
       
       for i in words:
          #print("Check --->"+i)
          #forbiddenwords = re.compile('VPN|Netflix|Directv|IP') 
          
          rx = re.compile('\W+')
          word = rx.sub('', i).strip()

          if len(word) == 0: break 

          self.words_checked.add(word)

          if not d.check(word):
             if word not in self.not_translated and word not in self.reserved_words:
                self.not_translated.add(quote) #return False
                break

          
       return True  
