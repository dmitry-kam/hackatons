import sys
import string

def translator(line):
    line = line.strip()
    inCharSet = "АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
    outCharSet = "ПпОоНнМмЛлКкЙйИиЗзЖжЕеДдГгВвБбАаЯяЮюЭэЬьЫыЪъЩщШшЧчЦцХхФфУуТтСсРр"
    LitorrheaDict = str.maketrans(inCharSet, outCharSet)
    #reverseLitorrheaDict = str.maketrans(outCharSet, inCharSet)
    #beginLine, endLine = string[:len(line)//2], string[len(line)//2:]
    return line.translate(LitorrheaDict)

for line in sys.stdin:
   #print(line.strip())
   print(translator(line))