from runpy import run_path
while True:
    f = input("Test file: ")
    if f == "exit":
        break
    if not f.endswith(".py"):
        f += ".py"
    run_path("tests\\" + f)
