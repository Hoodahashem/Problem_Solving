def spin_words(sentence):
    rstr = ""
    compo = sentence.split(" ")
    i = 0
    while i < len(compo):
        if len(compo[i]) >= 5:
            rstr += compo[i][::-1]
            if len(compo) > 1 and i != len(compo) - 1:
                rstr += " "
            i += 1
        else:
            rstr += compo[i]
            if len(compo) > 1 and i != len(compo) - 1:
                rstr += " "
            i += 1
    return rstr

# Simple Test Case
print(spin_words("This sentence is a sentence")) # The Output Should Be => "This ecnetnes is a ecnetnes"
