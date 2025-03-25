import random
import matplotlib.pyplot as plt

class MemoryBlock:
    def _init_(self, id, size):
        self.id = id
        self.size = size
        self.marked = False

class MemoryManager:
    def _init_(self, total_memory):
        self.total_memory = total_memory
        self.memory = []
        self.free_memory = total_memory
        self.memory_usage = []

    def allocate(self, size):
        if size <= self.free_memory:
            block = MemoryBlock(len(self.memory), size)
            self.memory.append(block)
            self.free_memory -= size
            print(f"Allocated Block {block.id}, Size: {size}")
        else:
            print("Memory Full! Running Garbage Collection...")
            self.run_garbage_collector()

    def free(self):
        if self.memory:
            block = random.choice(self.memory)
            print(f"Freed Block {block.id}, Size: {block.size}")
            self.memory.remove(block)
            self.free_memory += block.size

    def mark_and_sweep(self):
        print("Running Mark and Sweep...")
        for block in self.memory:
            block.marked = random.choice([True, False])
        self.memory = [block for block in self.memory if block.marked]
        self.free_memory = self.total_memory - sum(block.size for block in self.memory)

    def run_garbage_collector(self):
        self.mark_and_sweep()

    def visualize_memory(self):
        used_memory = self.total_memory - self.free_memory
        self.memory_usage.append(used_memory)
        plt.plot(self.memory_usage, label='Memory Usage')
        plt.xlabel('Time Steps')
        plt.ylabel('Memory Used')
        plt.legend()
        plt.pause(0.1)


def main():
    memory_manager = MemoryManager(total_memory=1000)

    plt.ion()
    plt.figure()

    for _ in range(30):
        action = random.choice(['allocate', 'free'])
        if action == 'allocate':
            memory_manager.allocate(random.randint(50, 200))
        elif action == 'free':
            memory_manager.free()
        memory_manager.visualize_memory()

    plt.ioff()
    plt.show()

main()