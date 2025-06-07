def remove_proper_noun(input_path, output_path):
    with open(input_path, encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            word = line.strip()
            if word and not word[0].isupper():
                outfile.write(word + "\n")

remove_proper_noun("fr_beta.txt", "fr.txt")