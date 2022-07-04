from cpp11_std_unique_ptr import *

k1 = makeKlassUniquePtr("first")
k2 = makeKlassUniquePtr("second")
if Klass.getTotal_count() != 2:
    raise "number of objects should be 2"

del k1
if Klass.getTotal_count() != 1:
    raise "number of objects should be 1"

if k2.getLabel() != "second":
    raise "wrong object label"

del k2
if Klass.getTotal_count() != 0:
    raise "no objects should be left"