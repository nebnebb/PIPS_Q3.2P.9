# cheat.py - Gives the answers to various exercises of the assignments of
# Programming in Psychological Sciences
#
# Record of Revisions
#
# Date            Programmers                         Descriptions of Change
# ====         ================                       ======================
# 28-1-2022      Zyneb Al-Hassaan                            Original code


def cheat(exercise):
    """ Give the answer to the exercise

    This function returns the answers to certain exercises of the course
    Programming in Psychological Sciences of the University of Amsterdam

    Parameters
    ----------
    exercise str
            in the format of Qweek.2Pexercise. For example, "Q1.2P7"

    Returns
    -------
    str containing what to do in that exercise

    Raises
    ------
    ValueError
        if parameter is not one string

    """

    if not isinstance(exercise, str):
        raise ValueError("Only strings allowed")

    if len(exercise.split()) != 1:
        raise ValueError("Only one exercise as input is allowed")

    if not exercise.startswith("Q"):
        raise ValueError("All exercises should be formatted like Q{week}.2P."
                         "{exercise number}")

    if exercise == "Q1.2P7":
        print("You can calculate the mean of a vector with nan using "
              "np.nanmean(sample_scores)")
    elif exercise == "Q1.2P9":
        print("You can retrieve the keys of a dictionary with dict.keys()")
    elif exercise == "Q2.2P4":
        print("You can calculate the phase angle with math.atan(i / r)")
    elif exercise == "Q3.2P1":
        print("To make a boxplot, use plt.boxplot(). To make a violin plot"
              "with jitter, use first sns.violinplot() followed by s"
              "ns.stripplot()")
    else:
        print("Sorry, I do not have the answer to that exercise :(")








