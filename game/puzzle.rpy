init python:
    def setup_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc) # Add the random locations to a list so we can use them to place each piece.

    def piece_drop(dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to its location.
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to be dragged.
            finished_pieces += 1
            renpy.music.play("Pickup_Coin.ogg", channel="sound")

            if finished_pieces == page_pieces:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("reassemble_complete")

label reassemble_complete:
    scene bg exterior_orange
    show munchie_idle at enlarge_and_left
    m "I did it!"
    hide munchie_idle
    show munchie_napping at enlarge_and_left
    m "That took a lot out of me. Time for a nap."
    

screen reassemble_puzzle:
    image "UI/puzzle-background.png"
    frame:
        background "UI/puzzle-frame.png"
        xysize full_page_size
        anchor(0.5, 0.5)
        pos(650, 535)

    draggroup:
        # Group of draggable pieces, and the spots they can be dragged to.
        # Paper pieces
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise True
                image "Pieces/piece-%s.png" % (i + 1)

        # Snappable spots to drag to.
        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                image "Pieces/piece-%s.png" % (i + 1) alpha 0.0 # Have the alpha at a higher value when first placing the pieces to make sure it looks correct.

default page_pieces = 12 # Amount of pieces for this puzzle.
default full_page_size = (711, 996)
default piece_coordinates = [(451, 149), (719, 139), (868, 238), (421, 399), (658, 318), (700, 488), (796, 538), (453, 718), (776, 773), (464, 925), (743, 958), (921, 888)] # The correct coordinates for each piece.
default initial_piece_coordinates = [] # Will be filled with random initial locations of the pieces.
default finished_pieces = 0 # Keeps track of the amount of pieces that have been placed correctly.