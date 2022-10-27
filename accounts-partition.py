from json import dumps, loads
import os

####################
accFile = "acc.json"
accPerFile = 50
###############
os.system("cls" if os.name == "nt" else "clear")

assert os.path.exists(accFile), "%r file doesn't exist!" % accFile

with open(accFile, "r") as File:
    Original = loads(File.read())

def nameGenerator(name : str) -> object :
    filename = name[::-1][name[::-1].index(".") + 1 : ][::-1]
    extension = name[::-1][ : name[::-1].index(".") + 1][::-1]
    format = "new-%s{}%s" % (filename, extension)
    idx = 0
    while True :
        yield format.format(idx)
        idx += 1

nameGen = nameGenerator(accFile)
savedCount = 0

for idx in range(0, len(Original), accPerFile):
    with open(next(nameGen), "w") as File :
        File.write(dumps(
            Original[idx : idx + accPerFile],
            indent = 4
        ))
        print("- accounts in", f"{idx}~{idx + accPerFile - 1}", "saved!")
        savedCount += 1

nameGen.close()
print("\n-", savedCount, "files saved!")