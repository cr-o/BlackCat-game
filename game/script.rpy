##### directly lifted from here https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=16151#p294340

define m = Character("Munchie")
define c = Character("Cat", color="#c492de")
define mrk = Character("Mr. Kitty", color="#c492de")

default grid_width = 3
default grid_height = 3
define puzzle_field_size = 650
define puzzle_field_offset = 30
define puzzle_piece_size = 450
define grip_size = 75
define active_area_size = puzzle_piece_size - (grip_size * 2)

label start:
    play music "dreamland_lullaby.wav"
    scene bg interior_one
    show munchie_napping at slight_low
    m "{i}z z z . . .{/i}"
    m "{i}. . .{/i}"
    hide munchie_napping
    show munchie_idle at slight_left
    m "Ah, it’s still night, why did I wake up?"
    m "I was having such a blissful sleep."
    hide munchie_idle
    "A gentle breeze wafts through the open window beside her, carrying with it the soft rustling of leaves, and the scent of something pleasant but...strange."
    "Her whiskers twitch in anticipation at once."
    show munchie_idle at slight_left
    m "That smells lovely...like dewy grass and something earthy...?"
    hide munchie_idle
    "Feeling the sleep rub from her eyes, Munchie began to contemplate seriously."
    show munchie_idle at slight_left
    m "Tonight feels like a good time to venture out..."
    hide munchie_idle
    "Though feeling snug in her bed, her mind wanders to the world beyond her cozy bed."
    "She didn’t want to admit that the stories Sarah and James – her caretakers – told her every evening were beginning to get into her head."
    show munchie_idle at slight_left
    m "{i}Sigh{/i}"
    m "I guess my mother was right after all..."
    m "That one day, I’d long for the adventure that ran deep in our family blood."
    hide munchie_idle
    "With a subtle flick of her tail, she leaps on all fours, yawning with her paw outstretched."
    show munchie_walking at walk_left
    m "I guess I’m just as rambunctious as my siblings after all..."
    hide munchie_walking
    "She takes a long look at the windowsill before she springs over to it."
    show munchie_walking at walk_left
    m "Sarah and James must still be in their beds sleeping..."
    hide munchie_walking
    "Then, with one final leap – and a wistful look at her bed – she steps outside."

    scene bg exterior_blue
    "Striding quietly about the deeply shadowed compound of the house, Munchie listens quietly to the eerie stillness about her."
    "Crickets chirp about, and so does a far-off owl hooting."
    show munchie_idle at slight_left
    m "{i}What exactly am I looking for...?{/i}"
    hide munchie_idle
    "But what surprises her the most is to see the outline of a portly creature perched atop a rickety, wrought-iron fence"
    "It sits still, gazing at the starry sky above."
    show munchie_walking at walk_left
    hide munchie_walking
    "She isn’t sure what she is looking at."
    show munchie_walking at walk_left
    m "{i}What is that...?{/i}"
    hide munchie_walking
    "Gingerly, she leaps onto the fence and steps closer."
    show mrkitty_idle at center_above
    "The creature turns out to be a black and white tuxedo cat."
    "And he watches her with his piercing yellow eyes."
    hide mrkitty_idle
    show munchie_idle at slight_left
    show mrkitty_idle at slight_right
    c "Well, well. Who dares tread the night?"
    "The cat purrs in a deep tone."
    "Munchie cocks her head at the cat, curious."
    hide mrkitty_idle
    m "Who are you?"
    hide munchie_idle
    "The cat’s lips stretch into a smirk."
    show mrkitty_idle at slight_right
    c "They call me Mr. Kitty—quite a vicious name, isn’t it?"
    hide mrkitty_idle
    "Munchie sees something akin to mischief sparkle in the cat’s eyes."
    show munchie_idle at slight_left
    m "{i}I’ll be wise to keep away from this cat.{/i}"
    hide munchie_idle
    "She shivers at the thought of getting tangled in something unfortunate."
    show munchie_idle at slight_left
    m "{i}Something about him screams trouble.{/i}"
    hide munchie_idle
    "The cat turns his eyes back to the moonlit sky."
    show mrkitty_idle at slight_right
    mrk "You know, the neighborhood cats scatter like mice when they see me."
    mrk "Can’t imagine why though, I’m such a delightful companion."
    hide mrkitty_idle
    "He licks his paws, flicking his tail lazily."
    show mrkitty_idle at slight_right
    mrk "Yet here you are, as bold as brass—or perhaps just naïve—to strike up a conversation."
    hide mrkitty_idle
    "Munchie blinks at him, not quite getting his point."
    show munchie_idle at slight_left
    m "Should I not talk to you then?"
    hide munchie_idle
    "Mr. Kitty rouses suddenly from his sitting position, causing Munchie to flinch."
    "He grins at Munchie’s reaction, turning his yellow eyes back to her."
    show mrkitty_idle at slight_right
    mrk "Say...since you’re looking to see new things, how about I tell you what I’ve seen?"
    hide mrkitty_idle
    show munchie_idle at slight_left
    "Munchie shudders at what the cat must have in store for her."
    hide munchie_idle
    show mrkitty_idle at slight_right
    mrk "How about...a monster?"
    hide mrkitty_idle
    show munchie_idle at slight_left
    m "A monster...?"
    hide munchie_idle
    "Munchie, whose eyes are as big as two green saucers, gazes warily at the cat, who looks delighted by his idea."
    show mrkitty_idle at slight_right
    mrk "Yes, a monster!"
    mrk "A monster that is..."
    mrk "...A giant refrigerator having a nap, four water bowls for legs, lasers for eyes! four of them! cat doors all over, runs very fast, and says HOOOOOONK HONK!"
    mrk "I have seen two or more of these monsters crash into each other."
    mrk "When that happens, DO NOT stay close."
    mrk "Parts of them can fly past you!"
    hide mrkitty_idle
    "Munchie’s fear gradually gives way to curiosity."
    "She tries her best to imagine the refrigerator with bowl feet and laser eyes..."
    show munchie_idle at slight_left
    m "{i}What could it possibly look like?{/i}"
    show black with dissolve
    call start_puzzle
    hide munchie_idle

    scene bg interior_one with dissolve
    show munchie_napping at slight_low
    hide munchie_napping
    "Munchie’s eyes force open, and she awakens with a start."
    show munchie_idle at slight_left
    m "{i}What was that...?{/i}"
    hide munchie_idle
    "Quickly surveying her empty room, she realizes that..."
    show munchie_idle at slight_left
    m "{i}Phew. It was all a dream.{/i}"
    hide munchie_idle
    "She glances briefly outside her window, where a thin ray of moonlight is streaming through into her room."
    "Sighing, she shakes off a slight shiver."
    show munchie_walking at slight_left
    m "{i}Good thing it was not real. It never happened.{/i}"
    m "{i}Thinking about that cat gives me the creeps...{/i}"
    hide munchie_walking
    "She nestles back into her plush bed, relieved."
    show munchie_napping at slight_low
    "But beyond her window stands a tuxedo cat nearby, watching her with a Cheshire smile on his face..."
    show mrkitty_idle at stand_window
    pause
    show black with dissolve

    call screen credits()
    return

    
label start_puzzle:
    centered "{nw}"

    $ grid_width = 3
    $ grid_height = 3
    $ chosen_img = "puzzle_solved.png"
    
    # and call puzzle label
    call puzzle
    # call screen reassemble_puzzle
    # call reassemble_complete
    return