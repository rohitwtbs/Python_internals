def outer_fucntion(msg_outer):
    def inner_function(msg_inner):
        print("log from inner fucntion", msg_inner + " " + msg_outer)
    return inner_function

closure = outer_fucntion("rohit")

closure("kumar")
# for code commit