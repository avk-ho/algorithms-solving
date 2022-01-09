# https://www.algoexpert.io/questions/Generate%20Document

# First solution
def generateDocument(characters, document):
    can_generate = True
    document_list = list(document)
    characters_list = list(characters)
    for chr in document_list:
        current_character = chr
        current_character_doc_count = document_list.count(current_character)
        current_character_chr_count = characters_list.count(current_character)
        can_generate = current_character in characters and current_character_chr_count >= current_character_doc_count
        if not can_generate:
            return can_generate
        for i in range(current_character_doc_count):
            document_list.remove(current_character)

    return can_generate