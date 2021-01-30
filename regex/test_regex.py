import pytest
import re
from input_text import *


s1 = "20191129-09-30-35-824223_lane1_ko2_orig.jpg"
s2 = "20191129-09.jpg-30-35-824223_lane1_ko2_orig.jpg"
s3 = "20191129-09-32-01-280280_lane1_ko2_orig.tson"


regex = "(\d{8})-(\d{2})"
m = re.match(regex, s1)  
print(m.group(1))
print(m.group(2))


m = re.match(r"(?P<date>\w+) (?P<h>\w+)", s1)

