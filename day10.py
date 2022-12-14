
example = """noop
addx 3
addx -5"""

example_parsed = example.split('\n')


class CPU:
    def __init__(self, monitoring_times: set[int]):
        self.X = 1
        self.clock = 1
        self.monitor = monitoring_times
        self.measurements = []
        self.pixels = []
        self.write()

    def write(self):
        if abs((self.clock % 40) - 1 - self.X) <= 1:
            self.pixels.append("#")
        else:
            self.pixels.append(".")
        if self.clock in self.monitor:
            self.measurements.append((self.clock, self.signal_strength))

    @property
    def signal_strength(self):
        return self.clock * self.X

    def __call__(self, instruction: str):
        if (instruction == 'noop'):
            self.clock += 1
            self.write()
        else:
            self.clock += 1
            self.write()
            self.clock += 1
            self.X += int(instruction.split()[1])
            self.write()

    def __repr__(self):
        return self.measurements.__repr__()

    def print_screen(self):
        for i, pixel in enumerate(self.pixels):
            if i % 40 == 0:
                print()
            print(pixel, end='')


video_system = CPU({20, 60, 100, 140, 180, 220})
with open("inputs/day10", "r") as f:
    for instruction in f:
        video_system(instruction.strip())

print(video_system)

print(
    f"The sum of the monitored signal strengths is: {sum(x[1] for x in video_system.measurements)}.")

video_system.print_screen()
