import os


def copy_file(command: str) -> None:
    command = command.split(" ")
    if len(command) == 3:
        source, target = command[1], command[2]
        if os.path.exists(source):
            if command[0] == "cp":
                if source != target:
                    with (open(source, "r") as file_in,
                          open(target, "a") as file_out):
                        for line in file_in:
                            file_out.write(line)
