import re
import glob

# Pokédex descriptions
for file in glob.glob('./src/data/pokemon/species_info/*.h'):
    with open(file, "r") as f:
        txt = f.read()
    for x in re.findall("(COMPOUND_STRING\((.|\n)*?\),)", txt):
        txt = txt.replace(x[0], re.sub("COMPOUND_STRING\(\n *", "COMPOUND_STRING(", re.sub('\"( |\n)*?\"', "", x[0]).replace("\\n", " ")))
    if "shared_dex_text" in file:
        for x in re.findall("(_\((.|\n)+?\);)", txt):
            txt = txt.replace(x[0], re.sub("_\(\n *", "_(", re.sub('\"( |\n)*?\"', "", x[0]).replace("\\n", " ")))
    with open(file, "w") as f:
        f.write(txt)
