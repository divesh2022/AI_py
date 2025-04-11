#  Write a program to implement Tower of Hanoi.

def tower_of_hanoi(n, source, target, auxiliary):
    steps = 0
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return 1
    steps = tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    steps = steps + 1
    steps = steps + tower_of_hanoi(n - 1, auxiliary, target, source)
    return steps

# Example usage for testing
if __name__ == "__main__":
    n = 3
    total_steps = tower_of_hanoi(n, 'A', 'C', 'B')
    print(f"Total steps: {total_steps}")
