import sys

def remove_common_links(file1,file2,file3):
    with open(file1) as f:
        lines1 = f.readlines()
    with open(file2) as f:
        lines2 = f.readlines()
    lines1 = [line.strip() for line in lines1]
    lines2 = [line.strip() for line in lines2]
    lines1 = set(lines1)
    lines2 = set(lines2)
    lines = lines1 - lines2
    with open(file3, "w") as f:
        for line in lines:
            f.write(line + "")
            f.write("\n")
def seperate_with_keywords(file):
    keyword = ["movies", "tv"]
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = set(lines)
    for i in keyword:
        lines = [line for line in lines if i in line]
        name =  i + '.txt'
        with open(name, "w") as f:
            for line in lines:
                f.write(line + "")
                f.write("\n")

# seperate_with_keywords(sys.argv[1])
remove_common_links(sys.argv[1],sys.argv[2],sys.argv[3])
