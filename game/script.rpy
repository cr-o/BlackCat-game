##### directly lifted from here https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=16151#p294340

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
    show munchie_napping at slight_low
    m "{i}z z z . . .{/i}"
    m "{i}. . .{/i}"
    hide munchie_napping
    show munchie_idle at slight_left
    m "Ah, it’s still night, why did I wake up?"
    m "I was having such a blissful sleep."
    hide munchie_idle
    "A gentle breeze wafts through the open window beside her, carrying with it the soft rustling of leaves, and the scent of something pleasant but…strange."
    "Her whiskers twitch in anticipation at once."
    show munchie_idle at slight_left
    m "That smells lovely…like dewy grass and something earthy…?"
    hide munchie_idle
    "Feeling the sleep rub from her eyes, Munchie began to contemplate seriously"
    show munchie_idle at slight_left
    m "Tonight feels like a good time to venture out…"
    hide munchie_idle
    "Though feeling snug in her bed, her mind wanders to the world beyond her cozy bed."
    "She didn’t want to admit that the stories Sarah and James – her caretakers – told her every evening were beginning to get into her head."
    show munchie_idle at slight_left
    m "{i}Sigh{/i}"
    m "I guess my mother was right after all…"
    m "That one day, I’d long for the adventure that ran deep in our family blood."
    hide munchie_idle
    "With a subtle flick of her tail, she leaps on all fours, yawning with her paw outstretched."
    show munchie_walking at slight_left
    m "I guess I’m just as rambunctious as my siblings after all…"
    hide munchie_walking
    "She takes a long look at the windowsill before she springs over to it."
    show munchie_walking at slight_left
    m "Sarah and James must still be in their beds sleeping…"
    hide munchie_walking
    "Then, with one final leap – and a wistful look at her bed – she steps outside."



    centered "{nw}"

    $ grid_width = 3
    $ grid_height = 3
    $ chosen_img = "puzzle_solved.png"
    
    # and call puzzle label
    call puzzle
    # call screen reassemble_puzzle
    scene bg exterior_orange with dissolve
    call reassemble_complete
    return