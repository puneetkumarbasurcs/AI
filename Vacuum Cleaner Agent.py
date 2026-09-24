# Vacuum Cleaner Agent
def vacuum_cleaner(room_a, room_b, position):

    print("\nInitial State:")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Vacuum Position:", position)
    if position == "A":

        if room_a == "DIRTY":
            print("A is DIRTY")
            print("SUCK")
            room_a = "CLEAN"
            print("A becomes CLEAN")

        print("MOVE RIGHT")
        position = "B"
        if room_b == "DIRTY":
            print("B is DIRTY")
            print("SUCK")
            room_b = "CLEAN"
            print("B becomes CLEAN")

    elif position == "B":

        if room_b == "DIRTY":
            print("B is DIRTY")
            print("SUCK")
            room_b = "CLEAN"
            print("B becomes CLEAN")

        print("MOVE LEFT")
        position = "A"

        if room_a == "DIRTY":
            print("A is DIRTY")
            print("SUCK")
            room_a = "CLEAN"
            print("A becomes CLEAN")

    print("\nFinal State:")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Vacuum Position:", position)
    print("STOP")

room_a = input("Enter status of Room A (DIRTY/CLEAN): ").upper()
room_b = input("Enter status of Room B (DIRTY/CLEAN): ").upper()
position = input("Enter vacuum position (A/B): ").upper()

if room_a not in ["DIRTY", "CLEAN"]:
    print("Invalid Room A status")
elif room_b not in ["DIRTY", "CLEAN"]:
    print("Invalid Room B status")
elif position not in ["A", "B"]:
    print("Invalid vacuum position")
else:
    vacuum_cleaner(room_a, room_b, position)