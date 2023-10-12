"""Defines Disjoint Set class"""


class DisjointSet:
    """Disjoint set class"""
    RANK = 0
    SIZE = 1
    def __init__(self, size=10):
        self.head = list(range(size))
        self.rank = [int(1)]*size
        self.size = [int(1)]*size

    def get_head(self, pos: int):
        """Returns the given position's set head

        Args:
            pos (int): Position to get the set head of

        Returns:
            int: Head of the given position
        """
        old_head = pos
        new_head = self.head[old_head]
        temp = old_head
        while old_head != new_head:
            old_head = temp
            temp = new_head
            new_head = self.head[old_head]
        return new_head

    def join(self, pos1, pos2, join_type=None):
        '''Join given sets based on the given type of join function.
           Defaults to join by rank.'''
        head1 = self.get_head(pos1)
        head2 = self.get_head(pos2)
        if join_type == self.RANK:
            cond = self.rank[head1] >= self.rank[head2]
        elif join_type == self.SIZE:
            cond = self.size[head2] >= self.size[head1]
        else:
            print("No given type of disjoint set join operation, defaulting to \
                  join by rank.")
            cond = self.rank[head1] >= self.rank[head2]

        if cond:
            self.head[head2] = head1
            self.size[head1] += self.size[head2]
            if self.rank[head1] < (self.rank[head2]+1):
                self.rank[head1] = self.rank[head2] + 1
        else:
            self.head[head1] = head2
            self.size[head2] += self.size[head1]
            if self.rank[head2] < (self.rank[head1]+1):
                self.rank[head2] = self.rank[head1] + 1

    def join_by_rank(self, pos1, pos2):
        '''Join given sets based on their head's rank.'''
        head1 = self.get_head(pos1)
        head2 = self.get_head(pos2)
        if self.rank[pos1] >= self.rank[pos2]:
            self.head[head2] = head1
            self.size[head1] += self.size[head2]
            if self.rank[head1] < (self.rank[head2]+1):
                self.rank[head1] += self.rank[head2] + 1
        else:
            self.head[head1] = head2
            self.size[head2] += self.size[head1]
            if self.rank[head2] < (self.rank[head1]+1):
                self.rank[head2] += self.rank[head1] + 1

    def join_by_size(self, pos1, pos2):
        '''Join given sets based on their head's size.'''
        head1 = self.get_head(pos1)
        head2 = self.get_head(pos2)
        if self.size[head1] >= self.size[head2]:
            self.head[head2] = head1
            self.size[head1] += self.size[head2]
            if self.rank[head1] < (self.rank[head2]+1):
                self.rank[head1] = self.rank[head2] + 1
        else:
            self.head[head1] = head2
            self.size[head2] += self.size[head1]
            if self.rank[head2] < (self.rank[head1]+1):
                self.rank[head2] = self.rank[head1] + 1

    def print_info(self, string=""):
        '''Prints out the head, rank and size data for the disjoint set,
        with an option to choose what to print before the information.'''
        print(string, end="")
        print(f"head: {self.head}")
        print(f"rank: {self.rank}")
        print(f"size: {self.size}")

if __name__ == '__main__':
    #Test types: 
    # Normal
    # Same number
    # Same set
    # Out-of-bounds
    # Negative numbers
    pass
