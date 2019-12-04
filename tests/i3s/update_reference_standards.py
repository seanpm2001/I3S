import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..', '../', '../..'])

from pycparser import (
    parse_file,
    c_generator,
    i3s_processing
)

def update_reference_standards():
    generator = c_generator.CGenerator()

    f_reference_standards = open("i3s_reference_standards.c", "w")

    ast = parse_file("i3s.c")
    i3s_processing.convert_i3s_to_c(ast)
    i3s_processed = generator.visit(ast)

    f_reference_standards.write(i3s_processed + ast.suffix)
    f_reference_standards.close()

    # update with debug comments
    f_debug_reference_standards = open("i3s_debug_reference_standards.c", "w")

    ast = parse_file("i3s.c")
    i3s_processing.convert_i3s_to_c(ast, True)
    i3s_processed = generator.visit(ast)

    f_debug_reference_standards.write(i3s_processed + ast.suffix)
    f_debug_reference_standards.close()

#------------------------------------------------------------------------------
if __name__ == "__main__":
    update_reference_standards()
