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
    # 8^15 < register_a < 8^16

    _, b, c, program = preprocessing(data)
    div = []
    max_power = len(program)

    for i in range(8):
        computer = Computer(program=program, register_a=i, register_b=b, register_c=c)
        computer.run()
        if computer.output and [str(out) for out in computer.output] == program[-1:]:
            div.append(i)
    new_a = div.copy()

    for power in range(1, max_power):
        start = 8**power
        end = 8 ** (power + 1)
        div = []

        for i in range(start, end):
            if i // 8 in new_a:
                computer = Computer(program=program, register_a=i, register_b=b, register_c=c)
                computer.run()
                expected_output = program[-(power + 1) :]
                if computer.output and [str(out) for out in computer.output] == expected_output:
                    div.append(i)

        new_a = div.copy()
    return new_a[0]
