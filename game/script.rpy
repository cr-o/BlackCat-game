﻿define m = Character("Munchie")

label start:
    scene bg exterior_blue
    show munchie_idle at slight_left
    m "This is the beginning of my adventure."
    m "I see there is already a puzzle for me to solve!"
    $setup_puzzle()
    hide munchie_idle
    call screen reassemble_puzzle
    return