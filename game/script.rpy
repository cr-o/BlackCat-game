define m = Character("Munchie")
default grid_width = 3
default grid_height = 3
define puzzle_field_size = 650
define puzzle_field_offset = 30
define puzzle_piece_size = 450
define grip_size = 75
define active_area_size = puzzle_piece_size - (grip_size * 2)

label start:
    scene bg exterior_blue
    show munchie_idle at slight_left
    m "This is the beginning of my adventure."
    m "I see there is already a puzzle for me to solve!"
    # $setup_puzzle()
    hide munchie_idle
    
    centered "{nw}"

    $ grid_width = 3
    $ grid_height = 3
    $ chosen_img = "puzzle_solved.png"
    
    # and call puzzle label
    call puzzle
    # call screen reassemble_puzzle
    call reassemble_complete
    return