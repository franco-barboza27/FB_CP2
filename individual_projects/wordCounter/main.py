# FB 1st word counter

# import the source files

# introduce the user to the program (edits docs, saves word count, saves most recent time editted)

# ask them what the file exact file path is to the document they want to do things with
    # or if they'd rather terminate the program

# ask if they want to
    # 1. Update document info
    # 2. View document
    # 3. Add content to document
    # 4. Exit this menu (choose a different file)

    # if updating a document

        # Ask if they're sure they want to, which would replace the old document
            # if not go back to menu, otherwise move on

        # ask what they want to replace it with
            # use the document handler UPDATE function
            # use the document handler WORD COUNT function
            # use the timekeeper to get the current date and time

            # from the CSV manipulator file, use the CSV finder to check if the file path exists inside
                # if it does, create a database of the document paths, word counts, and edits
                    # replace the old (< and ^ done in the csv.py file, expanded on more)
                # if it doesn't
                    # append it normally to the CSV

    # viewing the document
        # dochandler DOC PRINTER function

    # adding to the document
        # dochandler DOC ADDER function

    # go back to the beginning of the main loop