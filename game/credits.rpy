# directly lifted from https://www.reddit.com/r/RenPy/comments/16i3kid/comment/k0hhyd4/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

transform credits_scroll(speed):
    xcenter 0.5 yanchor 0.0 ypos 1.0
    ypos 600
    linear speed ypos -66000

screen credits:

    ## Ensure that the game_menu screens can't be stopped
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"

    timer 10 action Return()
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.

    frame at credits_scroll(400.0): #bigger is slower
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            label "Credits" xalign 0.5
            null height 75
            text "Pia Leo - Director / Illustrator"
            null height 10
            text "Frances Lafontaine Martinez - Producer"
            null height 10
            text "Júllia Martins - Pixel Artist / Animator"
            null height 10
            text "Cherin Oh - Programmer"
            null height 10
            text "Jane - Narrative Designer"
            null height 50
            text "Music from https://opengameart.org/users/genderfreak"
            null height 10

style credits_hbox:
    spacing 40
    ysize 30

style credits_vbox:
    xalign 0.5
    text_align 0.5

style credits_label_text:
    xalign 0.5
    justify True
    size 125
    text_align 0.5
    color "#cc6600"

style credits_text:
    xalign 0.5
    size 60
    justify True
    text_align 0.5
    color "#ffffff"