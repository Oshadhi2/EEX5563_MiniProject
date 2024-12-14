class QuickFit:
    def __init__(self):
        # Initialize size-specific memory block lists
        self.memory_blocks = {
            50: ["Block 1", "Block 2"],
            100: ["Block 3", "Block 4"],
            200: ["Block 5"],
        }

    def allocate(self, process_name, size):
        # Find the best-fit list for the requested size
        suitable_blocks = [block_size for block_size in self.memory_blocks if block_size >= size]
        suitable_blocks.sort()

        if not suitable_blocks:
            print(f"No suitable memory block available for Process {process_name} requiring {size} KB.")
            return False

        best_fit = suitable_blocks[0]
        if self.memory_blocks[best_fit]:
            allocated_block = self.memory_blocks[best_fit].pop(0)
            remaining_size = best_fit - size

            # Add the remaining size as a new block if applicable
            if remaining_size > 0:
                if remaining_size not in self.memory_blocks:
                    self.memory_blocks[remaining_size] = []
                self.memory_blocks[remaining_size].append(f"{allocated_block} (Remaining {remaining_size} KB)")

            print(f"Process {process_name} allocated to {allocated_block} ({best_fit} KB). Remaining {remaining_size} KB added to the {remaining_size} KB list.")
            return True
        else:
            print(f"No free block available in the {best_fit} KB list for Process {process_name}.")
            return False

    def deallocate(self, process_name, block_size, block_name):
        # Return the block to the appropriate size-specific list
        if block_size in self.memory_blocks:
            self.memory_blocks[block_size].append(block_name)
            print(f"Process {process_name} deallocated from {block_name} ({block_size} KB).")
        else:
            print(f"Invalid block size {block_size} for deallocation.")

    def display_memory_state(self):
        print("\nCurrent Memory State:")
        for size, blocks in self.memory_blocks.items():
            print(f"  {size} KB List: {blocks}")

# Example usage
quick_fit = QuickFit()
quick_fit.display_memory_state()

# Allocating processes
quick_fit.allocate("Process A", 10)
quick_fit.allocate("Process B", 100)
quick_fit.allocate("Process C", 200)
quick_fit.allocate("Process D", 80)
quick_fit.allocate("Process E", 500)

quick_fit.display_memory_state()

# Deallocating processes
quick_fit.deallocate("Process A", 50, "Block 1")
quick_fit.deallocate("Process B", 20, "Block 3")
quick_fit.display_memory_state()
