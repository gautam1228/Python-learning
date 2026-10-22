file = open("sample.txt", "w")

try:
    file.write("Hello there !")
except Exception as e:
    print(f"Error while writing to file:", e)
finally:
    file.close()  # important to close the file
