#import argparse
import sys
import re

if len(sys.argv) != 2:
    #raise(Error, "Requires exactly 1 arg: a .sql file whose keywords are to be capitalized.")
    print("Requires exactly 1 arg: a .sql file whose keywords are to be capitalized.")
else:
    filename = sys.argv[1]
    print(f"filename = {filename}")
    with open(filename) as f:
        content_str = f.read()
    print(f"content_str =\n{content_str}")
    capitalized_str = re.sub( \
        r"(^| )select ",
    )
