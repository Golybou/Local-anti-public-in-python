import os

class EndOfStream(Exception):
    pass

def batch_read_and_process(file_obj, batch_size=1000):
    while True:
        batch = set()
        while len(batch) < batch_size:
            line = file_obj.readline().strip()
            if not line:
                raise EndOfStream
            batch.add(line)
        yield batch

def main():
    base_dir = r'Your Folbider'
    s_file_path = os.path.join(base_dir, 'the name of the file with the lines that are the main ones.txt')
    profiles_file_path = os.path.join(base_dir, 'the name of the file with the lines that are secondary.txt')
    output_file_path = os.path.join(base_dir, 'the name of the source file with strings.txt')

    with open(s_file_path, "r") as s_file, \
            open(profiles_file_path, "r") as profiles_file, \
            open(output_file_path, "w") as output:

        s = set(line.strip() for line in s_file)

        try:
            batch_reader = batch_read_and_process(profiles_file)
            while True:
                profiles_batch = next(batch_reader)

                unique_profiles_batch = profiles_batch - s

                for profile in unique_profiles_batch:
                    output.write(f"{profile}\n")

        except EndOfStream:
            pass

if __name__ == "__main__":
    main()
