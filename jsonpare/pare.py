import sys

def pare(data, key, is_verbose=False, separator='.'):
    parts = key.split(separator)

    i = 0
    ptr = data
    for part in parts:
        if is_verbose is True:
            if i > 0:
                sys.stderr.write(' -> ')

            sys.stderr.write(part)

        try:
            if issubclass(ptr.__class__, list) is True:
                ptr = ptr[int(part)]
            else:
                ptr = ptr[part]
        except:
            if is_verbose is True:
                sys.stderr.write("\n")

            raise ValueError("Could not descend to child node: %s" % (part))

        i += 1

    if is_verbose is True:
        sys.stderr.write("\n")

    return ptr
