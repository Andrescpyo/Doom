import os

class UtilMaps:
    def __init__(self, path = "maps"):
        self.path = path
        self.maps = []

    def load_maps(self):
        list_files = os.listdir(self.path)
        #print(list_files)

        for f in list_files:
            temp = open(self.path + "/" + f, 'r').readlines()
            file_map = [list(map(lambda x: int(x), e)) for e in [line.split(" ")[1:-2] for line in temp]]

            self.maps.append(file_map)
           




if __name__ == "__main__":
    u = UtilMaps()
    u.load_maps()
    for l in u.maps:
        print(l)
        print()