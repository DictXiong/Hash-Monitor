import hashlib,zlib,time

def get_file_hash(hash_obj, path, block_size = 4 * 2**20):
    with open(path, "rb") as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hash_obj.update(data)
    return hash_obj.hexdigest()

hash_objs = [hashlib.sha1(), hashlib.sha3_256()]

large_file = r"E:\Media\纪录片\柴静雾霾调查：穹顶之下.2015.HD720P.X264.AAC.Mandarin.CHS.Mp4Ba.mp4"

for i in hash_objs:
    start = time.time()
    print(i.name, ": ", get_file_hash(i, large_file))
    print(f"time: {time.time()-start}\n ---")