# Define opcode and machine code mapping table
opcode_table = {
    "MOV": "8B",
    "ADD": "03",
    "SUB": "2B",
    "MUL": "0F AF",
    # Other instructions...
}

# Assembler class
class Assembler:
    def __init__(self):
        self.symbol_table = {}
        self.error_report = []

    def assemble(self, assembly_code, output_file_name):
        # Clear symbol table and error report
        self.symbol_table.clear()
        self.error_report.clear()

        # Parse assembly code and build symbol table
        self.build_symbol_table(assembly_code)

        # Assemble instructions
        machine_code = self.assemble_instructions(assembly_code)

        # Optimize instructions
        self.optimize(machine_code)

        # Write output file
        self.write_output_file(output_file_name, machine_code)

        # Print error report
        self.print_error_report()

    def build_symbol_table(self, assembly_code):
        current_address = 0
        lines = assembly_code.split("\n")
        for line in lines:
            if line.strip() and not line.strip().startswith(";"):
                parts = line.split()
                if parts[0].endswith(":"):
                    label = parts[0].rstrip(":")
                    if label in self.symbol_table:
                        self.error_report.append(f"Duplicated label: {label}")
                    else:
                        self.symbol_table[label] = current_address
                else:
                    current_address += 1

    def assemble_instructions(self, assembly_code):
        machine_code = []
        lines = assembly_code.split("\n")
        for line in lines:
            if line.strip() and not line.strip().startswith(";"):
                parts = line.split()
                if parts[0].endswith(":"):
                    continue

                instruction = parts[0].upper()
                operands = parts[1:]

                if instruction in opcode_table:
                    opcode = opcode_table[instruction]
                    machine_code.append(bytes.fromhex(opcode))

                    for operand in operands:
                        if operand in self.symbol_table:
                            address = self.symbol_table[operand]
                            machine_code.append(address.to_bytes(4, "big"))
                        else:
                            try:
                                value = int(operand)
                                machine_code.append(value.to_bytes(4, "big"))
                            except ValueError:
                                self.error_report.append(f"Invalid operand: {operand}")
                else:
                    self.error_report.append(f"Invalid instruction: {instruction}")

        return b"".join(machine_code)

    def optimize(self, machine_code):
        # Perform instruction optimization here
        pass

    def write_output_file(self, output_file_name, machine_code):
        with open(output_file_name, "wb") as file:
            file.write(machine_code)

    def print_error_report(self):
        for error in self.error_report:
            print(error)


# Create an instance of the Assembler class
assembler = Assembler()

# Read assembly code from file
with open("input.asm", "r") as file:
    assembly_code = file.read()

# Assemble and output the result
output_file_name = "output.bin"
assembler.assemble(assembly_code, output_file_name)

# Output the contents of the resulting machine code file
with open(output_file_name, "rb") as file:
    machine_code = file.read()

print("Machine code:")
for i in range(0, len(machine_code), 4):
    instruction_bytes = machine_code[i:i+4]
    print(" ".join(f"{byte:02X}" for byte in instruction_bytes))

output_file = "output.txt"

with open(output_file, "w") as file:
    for i in range(0, len(machine_code), 4):
        instruction_bytes = machine_code[i: i+4]
        line = " ".join(f"{byte:02X}" for byte in instruction_bytes)
        file.write(line + "\n")

print("Machine code has been written to", output_file)