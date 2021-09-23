def interpret(seq, values):

    #check if seq is a list, if not evaluate the string
    if not isinstance(seq, list):

        if seq == "true":
            return "true"
        if seq == "false":
            return "false"

        return values[seq]

    #NOT operator
    if len(seq) == 2:

        #get value of expr 1
        expr_1 = interpret(seq[1],values)

        #Evaluate expr 1
        if expr_1 == "false":
            return "true"
        if expr_1 == "true":
            return "false"

    #AND , OR operator
    if len(seq) == 3:

        #get values of expr 1 & 2
        expr_1 = interpret(seq[0], values)
        expr_2 = interpret(seq[2], values)

        #determin the operator
        if seq[1] == "AND":

            if expr_1 == "true" and expr_2 == "true":
                return "true"
            else:
                return "false"

        if seq[1] == "OR":

            if expr_1 == "true" or expr_2 == "true":
                return "true"
            else:
                return "false"

interpret(["door_open", "AND", "cat_gone"],
                         {"door_open" : "false", "cat_gone" : "true", "cat_asleep" : "true"} )

