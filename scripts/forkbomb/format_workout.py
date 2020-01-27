import base64
import json
import requests

url = 'https://formatworkout.forkbomb.ru'

mapper = [('avi', r'00000000: 52 49 46 46 A4 F9 0D 00  41 56 49 20 4C 49 53 54  RIFF....AVI LIST'),
          ('bmp', r"00000000: 42 4D 56 27 03 00 00 00  00 00 36 04 00 00 28 00  BMV'......6...(."),
          ('cab', r"00000000: 4D 53 43 46 00 00 00 00  27 34 09 00 00 00 00 00  MSCF....'4......"),
          ('cer', r'00000000: 30 82 03 10 30 82 01 F8  A0 03 02 01 02 02 10 1E  0...0...........'),
          ('class', r'00000000: CA FE BA BE 00 00 00 31  00 81 0A 00 22 00 38 09  .......1....".8.'),
          ('dat', r'00000000: 00 00 00 00 01 00 00 00  00 00 00 00 62 31 05 00  ............b1..'),
          ('dex', r'00000000: 64 65 78 0A 30 33 35 00  60 29 42 26 7C 54 B3 5F  dex.035.`)B&|T._'),
          ('doc', r'00000000: D0 CF 11 E0 A1 B1 1A E1  00 00 00 00 00 00 00 00  ................'),
          ('elf', r'00000000: 7F 45 4C 46 01 01 01 00  00 00 00 00 00 00 00 00  .ELF............'),
          ('evtx', r'00000000: 45 6C 66 46 69 6C 65 00  00 00 00 00 00 00 00 00  ElfFile.........'),
          ('exe', r'00000000: 4D 5A 90 00 03 00 00 00  04 00 00 00 FF FF 00 00  MZ..............'),
          ('gif', r'00000000: 47 49 46 38 39 61 20 03  01 01 F7 00 00 00 00 00  GIF89a .........'),
          ('inf', r'00000000: 5B 56 65 72 73 69 6F 6E  5D 0D 0A 53 69 67 6E 61  [Version].'),
          ('jpg', r'00000000: FF D8 FF E0 00 10 4A 46  49 46 00 01 01 01 00 60  ......JFIF.....`'),
          ('mbr', r'00000000: 33 C0 8E D0 BC 00 7C 8E  C0 8E D8 BE 00 7C BF 00  3.....|......|..'),
          ('mov', r'00000000: 00 00 00 20 66 74 79 70  71 74 20 20 20 05 03 00  ... ftypqt   ...'),
          ('mp3', r'00000000: FF FB 90 44 00 0F F0 00  00 69 00 00 00 08 00 00  ...D.....i......'),
          ('pcap', r'00000000: D4 C3 B2 A1 02 00 04 00  00 00 00 00 00 00 00 00  ................'),
          ('pdf', r'00000000: 25 50 44 46 2D 31 2E 35  0D 25 E2 E3 CF D3 0D 0A  %PDF-1.5.%......'),
          ('png', r'00000000: 89 50 4E 47 0D 0A 1A 0A  00 00 00 0D 49 48 44 52  .PNG........IHDR'),
          ('pwl', r'00000000: E3 82 85 96 03 00 00 00  02 00 01 00 00 00 00 00  ..........'),
          ('pyc', r'00000000: 03 F3 0D 0A 8D 5A 76 4E  63 00 00 00 00 00 00 00  .....ZvNc.......'),
          ('rar', r'00000000: 52 61 72 21 1A 07 00 CF  90 73 00 00 0D 00 00 00  Rar!.....s......'),
          ('rtf', r'00000000: 7B 5C 72 74 66 31 5C 61  64 65 66 6C 61 6E 67 31  {\rtf1\adeflang1'),
          ('swf', r'00000000: 43 57 53 07 E5 F7 10 00  78 9C EC BD 07 5C 53 4B  CWS.....x....\SK'),
          ('tif', r'00000000: 49 49 2A 00 20 4D 00 00  80 3F E0 4F F0 04 16 0D  II*. M...?.O....'),
          ('txt', r'00000000: 20 20 20 20 20 20 20 20  20 20 20 20 20 20 20 20                  '),
          ('txt', r'00000000: FE FF 00 61 00 37 00 35  00 36 00 65 00 37 00 34  ...a.7.5.6'),
          ('wav', r'00000000: 52 49 46 46 6A 7D 00 00  57 41 56 45 66 6D 74 20  RIFFj}..WAVEfmt'),
          ('wav.bz2', r'00000000: 42 5A 68 39 31 41 59 26  53 59 29 76 31 28 00 1C  BZh91AY&SY)v1(..'),
          ('wav.gz', r'00000000: 1F 8B 08 08 AC 44 52 53  04 00 77 61 76 2E 77 61  .....DRS..wav.wa'),
          ('zip', r'00000000: 50 4B 03 04 14 00 00 00  08 00 21 65 93 44 65 DA  PK........!e.De.'),
          ('zlib', r'00000000: 78 9C 6D 55 D1 6E 23 37  0C 7C CF 57 F0 ED 1C C0  x.mU.n#7.|.W....')]

s = requests.Session()
s.get(url)

for i in range(37):
    response = s.get(f"{url}/gettask")
    response = json.loads(response.text)
    task = base64.b64decode(response['task']).decode()
    print(response['level'], task[:70])

    for (extension, raw) in mapper:
        if raw in task:
            s.post(f"{url}/verify",
                   data=json.dumps({"ans": extension}),
                   headers={"Content-Type": "application/json"})
