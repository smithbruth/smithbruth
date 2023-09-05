def exercise1(InputText):
    words = InputText.split()
    TerribleCount = 0  #Initially set to 0
    OutputWords = []

    for word in words:    #This is the counting and replacement of the word ‘terrible’
        if word == "terrible":
            TerribleCount += 1
            if TerribleCount % 2 == 0:
                OutputWords.append("pathetic")
            else:
                OutputWords.append("marvellous")
        else:
            OutputWords.append(word)

    return " ".join(OutputWords), TerribleCount

def main():
    InputFilePath = "F:/file_to_read.txt"  #Specify file reading and output paths
    OutputFilePath = "F:/result.txt"

    try:           
        with open(InputFilePath, "r") as InputFile:    #Make readable
            InputText = InputFile.read()

        ModifiedText, TerribleCount = exercise1(InputText)

        with open(OutputFilePath, "w") as OutputFile:  #Make ‘writeable’
            OutputFile.write(ModifiedText)

        print(f"Total occurrences of 'terrible': {TerribleCount}") #consequence of the function
        print(f"Modified text written to {OutputFilePath}")

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    main()
