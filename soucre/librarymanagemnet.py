import re

def library_chatbot(user_input):
    user_input = user_input.lower()

    # Rule 1: Library timings
    if re.search(r"(open|timing|hours)", user_input):
        return "The library is open from 9 AM to 6 PM, Monday to Saturday."

    # Rule 2: Membership
    elif "membership" in user_input:
        return "You can become a member by filling out the membership form at the front desk."

    # Rule 3: Borrowing
    elif re.search(r"(borrow|issue)", user_input):
        return "Books can be borrowed for 14 days."

    # Rule 4: Returning
    elif "return" in user_input:
        return "Late returns incur a fine of ₹10 per day."

    # Rule 5: Default response
    else:
        return "Sorry, I don’t understand that. Please ask about timings, membership, borrowing, or returning."

# Example interaction
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", library_chatbot(query))
