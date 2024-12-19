from pydantic import BaseModel


class Computer(BaseModel):
    program: list[int]
    register_a: int
    register_b: int
    register_c: int
    instruction_pointer: int = 0
    output: list[int] | None = None

    def run(self):
        if self.instruction_pointer >= len(self.program):
            return
        # print(self)

        pointer = self.program[self.instruction_pointer]
        operand = self.program[self.instruction_pointer + 1]
        instruction = self.opcodes()[pointer]
        instruction(operand)

        self.instruction_pointer += 2

        return self.run()

    def opcodes(self):
        return {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def combo(self, operand):
        map_combo = {
            0: operand,
            1: operand,
            2: operand,
            3: operand,
            4: self.register_a,
            5: self.register_b,
            6: self.register_c,
            7: None,
        }

        return map_combo[operand]

    def adv(self, operand):
        self.register_a = self.register_a // 2 ** self.combo(operand)

    def bxl(self, operand):
        self.register_b = self.register_b ^ operand

    def bst(self, operand):
        self.register_b = self.combo(operand) % 8

    def jnz(self, operand):
        if self.register_a == 0:
            return operand
        else:
            self.instruction_pointer = operand - 2

    def bxc(self, operand):
        self.register_b = self.register_b ^ self.register_c

    def out(self, operand):
        if self.output is None:
            self.output = []

        self.output.append(self.combo(operand) % 8)

    def bdv(self, operand):
        self.register_b = self.register_a // 2 ** self.combo(operand)

    def cdv(self, operand):
        self.register_c = self.register_a // 2 ** self.combo(operand)


def preprocessing(data):
    a = data[0].split(" ")[-1]
    b = data[1].split(" ")[-1]
    c = data[2].split(" ")[-1]

    program = data[4].split(" ")[-1].split(",")

    return a, b, c, program


def part_1(data):
    # pass
    a, b, c, program = preprocessing(data)
    computer = Computer(program=program, register_a=a, register_b=b, register_c=c)
    computer.run()
    if computer.output:
        return ",".join([str(out) for out in computer.output])


def part_2(data):
    _, b, c, program = preprocessing(data)

    valid_values = {0}
    for i in range(len(program)):
        next_values = set()

        for value in valid_values:
            next_a = value * 8
            for j in range(next_a, next_a + 8):
                computer = Computer(program=program, register_a=j, register_b=b, register_c=c)
                computer.run()

                if computer.output and [str(out) for out in computer.output] == program[-(i + 1) :]:
                    next_values.add(j)

        valid_values = next_values
    return min(valid_values)
