def new(num_buckets=256):
    """initialize a map with the given number of buckets. """
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])  # update aMap with 256 numer of buckets.
    return aMap


def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to
    an index for the aMap's buckets. *note len aMap is always 256"""
    print("in hash key # %s" % (hash(key) % len(aMap))),
    # print(len(aMap))
    return hash(key) % len(aMap)


def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]


def get_slot(aMap, key, default=None):
    """ return the index, key and value of a slot found in a bucket.
    returns -1 , key, and default (none if not set) when not found.
    """
    bucket = get_bucket(aMap, key)
    for i, kv in enumerate(bucket):
        k, v = kv
        print(" in get method k is: %s" %k)
        print(" in get method v is: %s" %v)
        if key == k:
            return i, k, v
    return -1, key, default


def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default"""
    i, k, v = get_slot(aMap, key, default=default)
    return v


def set(aMap, key, value):
    """sets the the key to the value, replacing any existing values."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not , append to create it
        bucket.append((key, value))


def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)

    for i in range(len(bucket)):  # was xrange??
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break


def list(aMap):
    """Prints out what's in the map"""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print(k, v)
