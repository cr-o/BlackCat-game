define m = Character("Munchie")

label start:
    scene bg exterior_blue
    m "This is the beginning of my adventure."
    m "I see there is already a puzzle for me to solve!"
    $setup_puzzle()
    call screen reassemble_puzzle
    return