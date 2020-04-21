# Create the accession map used by test/mock/sitecustomize.py

import ihm.reference

codes = [ 'P52891', 'P46673', 'P35729', 'P36161', 'P49687', 'P53011', 'Q04491']

def pp(s):
    indent = 8
    width = 66
    def get_lines(s):
        for i in range(0, len(s), width):
            yield ' ' * indent + "'" + s[i:i+width] + "'"
    return '\n'.join(l for l in get_lines(s))

for code in codes:
    u = ihm.reference.UniProtSequence.from_accession(code)
    print("    '%s': {'db_code':'%s', 'sequence':\n%s},"
          % (code, u.db_code, pp(u.sequence)))
