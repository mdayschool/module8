
def score_input(test_name, test_score=0,
            invalid_message='Invalid test score, try again!'):
    """Validates and prints/returns parameters"""
    MIN_SCORE = 0
    MAX_SCORE = 100
    try:
        if test_score >= MIN_SCORE and test_score <= MAX_SCORE:
            print(test_name + ": 0")
            return {test_name:test_score}
        else:
            print(invalid_message)
            return invalid_message
    except TypeError:
        print(invalid_message)
        return invalid_message

def average_scores(scores):
    if len(scores) > 0:
        total = 0
        for k,v in scores.items():
            total += v
        return total / len(scores)
    else:
        return -1


if __name__=='__main__':
    num_scores = int(input("How many scores would you like to enter?: "))
    score_dict = dict()
    for i in range(0, num_scores):
        name = input("Enter Name: ")
        score = int(input("Enter Score: "))
        score_dict.update({name:score})
    print("Average score is: " + str(round(average_scores(score_dict), 2)))

