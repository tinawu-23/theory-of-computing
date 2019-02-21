def isValidCSV(text):
    state = "NewLine"
    alphnumchar = [".","'"]
    for char in text:
        if char == '\n':
            if state == "NewLine" or state == "NonQuoted" or state == "Comma" or state == "InQuote":
                state = "NewLine"
            elif state == "Quote":
                state = "Quote"
            else:
                return False
        elif char == '"':
            if state == "NewLine" or state == "Comma" or state == "InQuote":
                state = "Quote"
            elif state == "Quote":
                state = "InQuote"
            else:
                return False
        elif char == ',':
            if state == "InQuote" or state == "NewLine" or state == "Comma" or state == "NonQuoted":
                state = "Comma"
            elif state == "Quote":
                state = "Quote"
            else:
                return False
        elif char in alphnumchar or char.isalnum() or char.isspace():
            if state == "NewLine" or state == "NonQuoted" or state == "Comma":
                state = "NonQuoted"
            elif state == "Quote":
                state = "Quote"
            else:
                return False
        else:
            return False
        print(state)

    return (state == "NewLine" or state == "NonQuoted" or state == "InQuote")


text = ' '
print(isValidCSV(text))
