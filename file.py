import glob

path = "/"

text_files = glob.glob(path + "/**/*.py", recursive = True)

print(text_files)