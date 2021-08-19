class ChordSimulation:

    def __init__(self, m, peers):
        self.peers = sorted(peers)
        self.m = m
        self.all_finger_tables = {}

    def create_finger_table(self, node):
        p1 = pow(2, self.m)
        value = {}
        dummy = {}
        for i in range(self.m):
            p0 = pow(2, i)
            res = (node + p0) % p1
            new_res = None
            if res > self.peers[-1]:
                new_res = self.peers[0]
            else:
                for j, peer in enumerate(self.peers):
                    if peer > res:
                        new_res = peer
                        break
            value[i] = new_res
            dummy[i] = res

        return value

    def create(self):

        for peer in self.peers:
            value = self.create_finger_table(peer)
            self.all_finger_tables[peer] = value
        print("done")

if __name__ == '__main__':
    peers = [1, 12, 123, 234, 345, 456, 501]
    m = 9
    so = ChordSimulation(m, peers)
    so.create()

    peers2 = [32, 45, 99, 199, 132, 234]
    m = 8
    so = ChordSimulation(m, peers2)
    so.create()
