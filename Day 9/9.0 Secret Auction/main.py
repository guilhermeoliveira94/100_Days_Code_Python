from art import logo

bids = {}
other_bidders_true = True

def clear():
    try:
        import os
        lines = os.get_terminal_size().lines
    except AttributeError:
        lines = 130
    print("\n" * lines)

def add_to_dictionary(bid, bidder):
    bids[bid] = bidder

print(logo)
print("Welcome to the Secret Auction Program.")

should_end = False
while not should_end:

    bidder = input("What is your name?: ")
    bid = input("What's your bid?: $")

    other_bidders = input("Are there any other bidders? Type 'Yes' or 'No'.\n").lower()
    # TODO clear screen

    add_to_dictionary(bid, bidder)

    if other_bidders == "no":
        should_end = True

        print(f"The winner is {bids[max(bids.keys())]} with a bid of ${max(bids.keys())}.")