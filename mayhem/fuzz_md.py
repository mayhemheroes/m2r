#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports():
    from m2r import convert, parse_from_file

def TestOneInput(data):
        fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
        md = fdp.ConsumeRemainingString()
        convert(md)


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
