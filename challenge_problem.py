import random
import matplotlib.pyplot as plt


def flip(prob):
    """
    Return H or T representing the outcome of coin flip
    """
    if random.random() < prob:
        return "H"
    else:
        return "T"


def count_longest_run(lst):
    """
    Return longest run in given experiment outcomes list
    """
    Y_longest_run = count = 0
    current = lst[0]
    for outcome in lst:
        if outcome == current:
            count += 1
        else:
            count = 1
            current = outcome
        Y_longest_run = max(count, Y_longest_run)
    return Y_longest_run


def count_longest_heads_run(lst):
    """
    Return longest Heads run in given experiment outcomes list
    """
    count = X_longest_run = 0
    for outcome in lst:
        if outcome == 'H':
            count += 1
        else:
            count = 0
        if count > X_longest_run:
            X_longest_run = count

    return X_longest_run


def conduct_experiment(tosses, heads_probability):
    """
    Return list representing outcomes of the experiment
    """
    experiment = []
    for _ in range(tosses):
        experiment.append(flip(heads_probability))
    return experiment


def cdf(n, k, experiments_num, heads_probability):
    """
    Return cumulative distribution function of that the largest run of Heads 
    in a sequence of n flips is length k or less.
    """
    counter = 0
    for _ in range(experiments_num):
        if count_longest_heads_run(conduct_experiment(n, heads_probability)) <= k:
            counter += 1

    return float(counter / experiments_num)


def pmf(n, k, experiments_num, heads_probability):
    """
    Return probability mass function of that the largest run of Heads in a
    sequence of n flips is length k or less.
    """
    counter = 0
    for _ in range(experiments_num):
        if count_longest_heads_run(conduct_experiment(n, heads_probability)) == k:
            counter += 1

    return float(counter / experiments_num)


def make_table(n, start, k, heads_probability):
    print(
        f"\n\nApproximate values for PMF and CDF with n={n}, k={k} and P(H)={heads_probability} \n")
    print(f" k          CDF(P(M{n} ≤ k))     PMF(P(M{n} = k))")
    print("_____________________________________________________\n")
    for i in range(start, k+1):
        print(f' {i}       |       {cdf(n, i, 10000, heads_probability)}       |       {pmf(n, i, 10000, heads_probability)}')
    print("\n\n")


def problemB():
    """
    Print result table showing obtained results for problem B
    """
    print("--- PROBLEM B ---\n\n")
    for i in [0.1, 0.3, 0.5, 0.7]:
        make_table(100, 3, 8, i)
    # make_table(50, 2, 8, 0.5)


def pmf2(n, k, experiments_num, heads_probability):
    """
    Return probability mass function of that the largest run of Heads in a
    sequence of n flips is length k or less.
    """
    counter = 0
    for _ in range(experiments_num):
        if count_longest_heads_run(conduct_experiment(n, heads_probability)) == k:
            counter += 1

    return float(counter / experiments_num)


def problemC():
    """
    Print result table showing obtained results for problem C
    """
    print("--- PROBLEM C ---\n\n")
    Y = []
    X = []

    array = conduct_experiment(50, 0.5)
    counter = 0
    for _ in range(10):
        for _ in range(100):
            if count_longest_heads_run(array) == 8:
                counter += 1
        X.append(float(counter / 10))

        for _ in range(100):
            if count_longest_run(array) == 8:
                counter += 1
        Y.append(float(counter / 10))

    # for _ in range(10):
    #     Y.append(pmf2(100, 8, 1000, 0.5))
    #     X.append(pmf(100, 8, 1000, 0.5))

    plt.plot([i for i in range(10)], X)
    plt.plot([i for i in range(10)], Y)
    plt.xlabel('No. of experiments')
    plt.ylabel('Probability')
    plt.title(
        f"Relations between p.m.f. of X and Y")

    plt.savefig('1.png')
    plt.close()


if __name__ == "__main__":
    problemB()
    problemC()
