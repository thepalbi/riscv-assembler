from riscv_assembler.convert import AssemblyConverter


def test_sw_encodes_s_type_immediate():
    cnv = AssemblyConverter(output_mode="a", nibble_mode=False)
    ir = int(cnv.convert("sw x1, 10(x2)")[0], 2)
    assert ir == 0x112523
    imm12 = ((ir >> 7) & 0x1F) | (((ir >> 25) & 0x7F) << 5)
    if imm12 & 0x800:
        imm12 -= 0x1000
    assert imm12 == 10
