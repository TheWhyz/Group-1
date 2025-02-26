import sys

class AssemblerInterpreter:
    OPCODES = {
        "const": 0, "get": 1, "put": 2, "ld": 3, "st": 4, "add": 5, "sub": 6, 
        "mul": 7, "div": 8, "cmp": 9, "jpos": 10, "jz": 11, "j": 12, "jl": 13, 
        "jle": 14, "jg": 15, "jge": 16, "halt": 17
    }

    def __init__(self):
        self.stack = [0] * 1000
        self.labels = {}
        self.program = []
        self.reg = 0
        self.ip = 0  # Instruction Pointer

    def parse_file(self, filename):
        """Reads and parses the assembly file."""
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("ERROR: File not found!")
            sys.exit(1)

        count = 0
        for line in lines:
            line = line.strip()
            if not line or line.startswith(";"):  # Ignore empty lines and comments
                continue

            parts = line.split()
            if parts[0] not in self.OPCODES:
                self.labels[parts[0]] = count
                parts = parts[1:]  # Remove label
            
            self.program.append(parts)
            count += 1

    def assemble(self):
        """Converts parsed instructions into machine code."""
        count = 0
        for instr in self.program:
            if not instr:
                continue
            opcode = self.OPCODES.get(instr[0], -1)
            if opcode == -1:
                print(f"ERROR: Unknown opcode {instr[0]}")
                sys.exit(1)

            address = 0
            if len(instr) > 1:
                operand = instr[1]
                if operand.isdigit():
                    address = int(operand)
                elif operand in self.labels:
                    address = self.labels[operand]
                else:
                    print(f"ERROR: Undefined label {operand}")
                    sys.exit(1)

            self.stack[count] = opcode * 1000 + address
            count += 1

    def execute(self):
        """Executes the assembled machine code."""
        instructions = {
            1: self.get, 2: self.put, 3: self.ld, 4: self.st, 5: self.add,
            6: self.sub, 7: self.mul, 8: self.div, 9: self.cmp, 10: self.jpos,
            11: self.jz, 12: self.j, 13: self.jl, 14: self.jle, 15: self.jg,
            16: self.jge, 17: self.halt
        }

        while self.ip >= 0:
            code = self.stack[self.ip] // 1000
            address = self.stack[self.ip] % 1000

            if code in instructions:
                instructions[code](address)
            else:
                print(f"ERROR: Invalid opcode {code}")
                break

        print("** Program terminated **")

    # Instruction Handlers
    def get(self, _):
        try:
            self.reg = int(input("Enter value: "))
        except ValueError:
            print("ERROR: Invalid input")
        self.ip += 1

    def put(self, _):
        print("Output:", self.reg)
        self.ip += 1

    def ld(self, address):
        self.reg = self.stack[address]
        self.ip += 1

    def st(self, address):
        self.stack[address] = self.reg
        self.ip += 1

    def add(self, address):
        self.reg += self.stack[address]
        self.ip += 1

    def sub(self, address):
        self.reg -= self.stack[address]
        self.ip += 1

    def mul(self, address):
        self.reg *= self.stack[address]
        self.ip += 1

    def div(self, address):
        if self.stack[address] == 0:
            print("ERROR: Division by zero")
            sys.exit(1)
        self.reg //= self.stack[address]
        self.ip += 1

    def cmp(self, address):
        self.reg -= self.stack[address]
        self.ip += 1

    def jpos(self, address):
        self.ip = address if self.reg > 0 else self.ip + 1

    def jz(self, address):
        self.ip = address if self.reg == 0 else self.ip + 1

    def j(self, address):
        self.ip = address

    def jl(self, address):
        self.ip = address if self.reg < 0 else self.ip + 1

    def jle(self, address):
        self.ip = address if self.reg <= 0 else self.ip + 1

    def jg(self, address):
        self.ip = address if self.reg > 0 else self.ip + 1

    def jge(self, address):
        self.ip = address if self.reg >= 0 else self.ip + 1

    def halt(self, _):
        self.ip = -1

# Entry Point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: No input file provided!")
        sys.exit(1)

    assembler = AssemblerInterpreter()
    assembler.parse_file(sys.argv[1])
    assembler.assemble()
    assembler.execute()
