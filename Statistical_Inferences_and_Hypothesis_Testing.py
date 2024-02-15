import numpy as np
import math

# Name: Edilberto Carrizales
# Language: Python
# Language version: 3.9


# Calculate the mean of the data
def data_mean(data):
    data_sum = 0
    for i in range(len(data)):
        data_sum += data[i]

    mean = 1 / len(data) * data_sum
    return mean


# Calculates the population variance of the data (because its only n, if it were sample variance it would be n - 1)
def data_variance(data):
    data_sum = 0
    mean = data_mean(data)

    for i in range(len(data)):
        data_sum += (data[i] - mean) ** 2

    variance = 1 / len(data) * data_sum
    return variance


def data_sample_variance(data):
    data_sum = 0
    mean = data_mean(data)

    for i in range(len(data)):
        data_sum += (data[i] - mean) ** 2

    sample_variance = 1 / (len(data) - 1) * data_sum
    return sample_variance


# Calculates Kth moment of the data
def kth_moment(data, k):
    data_sum = 0

    for i in range(len(data)):
        data_sum += (data[i]) ** k

    kth_moment = 1 / len(data) * data_sum
    return kth_moment


def construct_confidence_interval(data, confidence_interval, z_score, sigma, z_test):
    # Formula: (1 - alpha) = confidence_interval (x%)
    alpha = 1 - confidence_interval
    alpha = round(alpha, 3)  # round to 3 decimal places
    # print("The value of 𝜶: " + str(alpha))

    alpha2 = alpha / 2
    # print("The value of 𝜶/𝟐: " + str(alpha2))

    # We have to look up the quantile of 𝒁(𝜶/𝟐) this can be done  using a table and will be based on the confidence interval (example: 95%)
    # print("The value of 𝒁(𝜶/𝟐): " + str(z_score))

    n = len(data)  # number of values in data
    # print("The sample size n: " + str(n))

    s = sigma / math.sqrt(n)
    s = round(s, 4)
    # print("The standard error s: " + str(s))

    sample_mean = data_mean(data)  # mean
    # print("The value of the sample mean of Triple , 𝑿̅: " + str(sample_mean))

    margin_of_error = z_score * s
    margin_of_error = round(margin_of_error, 4)
    # print("The value of the margin of error: " + str(margin_of_error))

    lower_limit = sample_mean - margin_of_error
    lower_limit = round(lower_limit, 4)
    # print("The value of the lower limit of the confidence interval: " + str(lower_limit))

    upper_limit = sample_mean + margin_of_error
    upper_limit = round(upper_limit, 4)
    # print("The value of the upper limit of the confidence interval: " + str(upper_limit))

    result = False
    if lower_limit < z_test < upper_limit:
        result = True
    print(str(confidence_interval * 100) + "%: " + str(lower_limit) + " < " + str(z_test) + " < " + str(
        upper_limit) + " : " + str(result))


def problem1():
    print("\n------------------ Problem 1. Method of Moments for X^3 ------------------")

    """
    Notes: Formulas in Lecture 9.1
    
    The First Moment is the mean X bar of the population.
    The Second Moment is the variance of the population.
    
    Find:
    • Show the mean of sample Teetertotter
    • Show the variance of sample Teetertotter
    • Show the 3rd moment of sample Teetertotter
    • Solve for A, B, and C
    """

    # Read in the sample file Teetertotter.txt
    path = "/Users/Eddie Carrizales/OneDrive/Desktop/Teetertotter.txt"

    teetertotter_data = np.loadtxt(path, delimiter=" ")
    # print(teetertotter_data)

    print("\nFind:")
    teetertotter_mean = data_mean(teetertotter_data)
    print("teetertotter_mean: " + str(teetertotter_mean))

    teetertotter_variance = data_variance(teetertotter_data)
    print("teetertotter_variance: " + str(teetertotter_variance))

    teetertotter_3rd_moment = kth_moment(teetertotter_data, 3)
    teetertotter_3rd_moment = round(teetertotter_3rd_moment, 4)
    print("teetertotter_3rd_moment: " + str(teetertotter_3rd_moment))


def problem2():
    print("\n----- Problem 2. Confidence Interval with a known Standard Deviation -----")

    """
    Notes: Similar to Lecture 9.2 Example
    
    Given:
    For a 97% confidence interval
    The standard deviation 𝜎 = 59.5
    
    Find:
    • What is the value of 𝜶?
    • What is the value of 𝜶/𝟐?
    • What is the value of 𝒁(𝜶/𝟐)?
    • What is the sample size n?
    • What is the standard error s?
    • What is the value of the sample mean of Triple , 𝑿̅?
    • What is the value of the margin?
    • What is the value of the lower limit of the confidence interval?
    • What is the value of the upper limit of the confidence interval?
    """

    # Read in the sample file Triple.txt
    path = "/Users/Eddie Carrizales/OneDrive/Desktop/Triple.txt"

    triple_data = np.loadtxt(path, delimiter=" ")
    # print(triple_data)

    print("\nGiven:")
    print("For a 97% confidence interval")
    sigma = 59.5  # population standard deviation
    print("𝜎: " + str(sigma) + "\n")

    print("Find:")
    # Formula: (1 - alpha) = x%
    alpha = 1 - 0.97
    alpha = round(alpha, 3)  # round to 3 decimal places
    print("The value of 𝜶: " + str(alpha))

    alpha2 = alpha / 2
    print("The value of 𝜶/𝟐: " + str(alpha2))

    # We have to look up the quantile of 𝒁(𝜶/𝟐) for Z(0.025), this can be done  using a table, for 97% we know its 2.17
    z_score = 2.17
    print("The value of 𝒁(𝜶/𝟐): " + str(z_score))

    n = len(triple_data)  # number of values in data
    print("The sample size n: " + str(n))

    s = sigma / math.sqrt(n)
    s = round(s, 4)
    print("The standard error s: " + str(s))

    sample_mean = data_mean(triple_data)  # mean
    print("The value of the sample mean of Triple , 𝑿̅: " + str(sample_mean))

    margin_of_error = z_score * s
    margin_of_error = round(margin_of_error, 4)
    print("The value of the margin of error: " + str(margin_of_error))

    lower_limit = sample_mean - margin_of_error
    lower_limit = round(lower_limit, 4)
    print("The value of the lower limit of the confidence interval: " + str(lower_limit))

    upper_limit = sample_mean + margin_of_error
    upper_limit = round(upper_limit, 4)
    print("The value of the upper limit of the confidence interval: " + str(upper_limit))


def problem3():
    print("\n----- Problem 3. Selection of a Sample Size for a Confidence Interval -----\n")

    """
    Notes: Last slide of Lecture 9.2
    
    Given:
    • The precision Δ = 0.01
    • The standard deviation 𝜎 = 8.75
    • The confidence interval is for 90%
    
    Find:
    • What is the value of 𝛼?
    • What is the value of 𝜶/𝟐?
    • What is the value of 𝒁(𝜶/𝟐)?
    • What is the sample size n?
    """
    print("Given:")
    delta = 0.01  # precision (delta)
    print("Δ: " + str(delta))
    print("For a 90% confidence interval")
    sigma = 8.75  # standard deviation of population is given (sigma)
    print("𝜎: " + str(sigma))

    print("\nFind:")
    # Formula: (1 - alpha) = x%
    alpha = 1 - .90
    alpha = round(alpha, 3)
    print("The value of 𝜶: " + str(alpha))

    alpha2 = alpha / 2
    print("The value of 𝜶/2: " + str(alpha2))

    # We have to look up the quantile of 𝒁(𝜶/𝟐) for Z(0.025), this can be done  using a table, for 90% we know its 1.645
    z_score = 1.645
    print("The value of 𝒁(𝜶/𝟐): " + str(z_score))

    # Formula for estimating n with a given precision
    n = (z_score * sigma / delta) ** 2
    n = round(n, 4)
    print("The sample size n: " + str(n))


def problem4():
    print("\n--------- Problem 4. Confidence Interval for two proportions ---------\n")

    """
    Notes: 
    • Lecture 9.3
    • standard error formula s will change for two proportions
    
    Given:
    • Sample X has 25 items out of 100
    • Sample Y has 12 items out of 200
    • The confidence interval is 95%
    
    Find:
    • What is the sample X proportional probability estimator, 𝒑̂𝒙?
    • What is the sample Y proportional probability estimator, 𝒑̂𝒚?
    • What is the value of 𝜶?
    • What is the value of 𝜶/𝟐?
    • What is the value of 𝒁(𝜶/𝟐)?
    • What is the difference between the proportional probability estimators?
    • What is the value of the margin?
    • What is the value of the lower limit of the confidence interval?
    • What is the value of the upper limit of the confidence interval?
    """

    print("Given:")
    print("Sample X has 25 items out of 100.")
    print("Sample Y has 12 items out of 200.")
    print("The confidence interval is 95%")

    print("\nFind:")
    # Sample X has 25 items out of 100
    pX = 25 / 100
    nX = 100
    print("The value of Px: " + str(pX))

    # Sample Y has 12 items out of 200
    pY = 12 / 200
    nY = 200
    print("The value of Py: " + str(pY))

    # Formula: (1 - alpha) = x%
    alpha = 1 - .95
    alpha = round(alpha, 3)
    print("The value of 𝜶: " + str(alpha))

    alpha2 = alpha / 2
    print("The value of 𝜶/2: " + str(alpha2))

    # We have to look up the quantile of 𝒁(𝜶/𝟐) for Z(0.025), this can be done  using a table, for 95% we know its 1.96
    z_score = 1.96
    print("The value of 𝒁(𝜶/𝟐): " + str(z_score))

    # Also known as parameter
    theta = pX - pY
    print("The difference between the proportional probability estimators: " + str(theta))

    # ---Margin of error formula for TWO proportions (standard error formula is different)---

    #  -Standard error formula for two proportions (s formula is different for two)
    s = math.sqrt((pX * (1 - pX)) / nX + (pY * (1 - pY)) / nY)

    margin_of_error = z_score * s
    margin_of_error = round(margin_of_error, 4)
    print("The value of the margin of error: " + str(margin_of_error))

    lower_limit = (pX - pY) - margin_of_error
    lower_limit = round(lower_limit, 4)
    print("The value of the lower limit of the confidence interval: " + str(lower_limit))

    upper_limit = (pX - pY) + margin_of_error
    upper_limit = round(upper_limit, 4)
    print("The value of the upper limit of the confidence interval: " + str(upper_limit))


def problem5():
    print("\n-------------------- Problem 5. Sample-T Problem --------------------\n")
    """
    Notes: Lecture 9.3
    
    Given:
    • The sample file PI.txt
    • The standard deviation of the population is unknown.
    • For a confidence interval of 95%
    
    Find:
    • What is the value of 𝜶?
    • What is the value of 𝜶𝟐⁄?
    • What is the size of sample Pi, n?
    • What is the value of the degrees of freedom?
    • What is the value of 𝒕(𝜶/𝟐)?
    • What is the value of the sample mean of Pi, 𝑿̅?
    • What is the value of the margin?
    • What is the lower limit of the confidence interval?
    • What is the upper bound of the confidence interval?
    """

    # Read in the sample file PI.txt
    path = "/Users/Eddie Carrizales/OneDrive/Desktop/PI.txt"

    pi_data = np.loadtxt(path, delimiter=" ")
    # print(pi_data)

    print("Given:")
    print("The standard deviation of the population is unknown.")
    print("The confidence interval is 95%")

    print("\nFind:")
    # Formula: (1 - alpha) = x%
    alpha = 1 - .95
    alpha = round(alpha, 3)
    print("The value of 𝜶: " + str(alpha))

    alpha2 = alpha / 2
    print("The value of 𝜶/2: " + str(alpha2))

    n = len(pi_data)
    print("The sample size n: " + str(n))

    # Students T problem (Sample T) has n-1 degree of freedom
    degrees_of_freedom = n - 1
    print("The degrees of freedom: " + str(degrees_of_freedom))

    # For 𝒕(𝜶/𝟐) we have to find the t-score from the T table with 95% confidence interval
    # So 𝒕(𝜶/𝟐, n-1) = 𝒕(0.025, 49)
    t_score = 2.009575  # from the table we get
    print("The value of 𝒕(𝜶/𝟐): " + str(t_score))

    pi_mean = data_mean(pi_data)
    print("The value of the sample mean of Pi, 𝑿̅: " + str(pi_mean))

    # sample standard error formula
    sum = 0
    for i in range(len(pi_data)):
        sum += (pi_data[i] - pi_mean) ** 2
    s = math.sqrt(sum / n - 1)

    # Variance is the sample standard deviation squared (so we can also get std from by taking square root)
    pi_data_variance = data_variance(pi_data)
    s = math.sqrt(pi_data_variance)

    margin_of_error = t_score * (s / math.sqrt(n))  # margin of error formula for Students T
    margin_of_error = round(margin_of_error, 4)
    print("The value of the margin of error: " + str(margin_of_error))

    lower_limit = pi_mean - margin_of_error
    lower_limit = round(lower_limit, 4)
    print("The value of the lower limit of the confidence interval: " + str(lower_limit))

    upper_limit = pi_mean + margin_of_error
    upper_limit = round(upper_limit, 4)
    print("The value of the upper bound of the confidence interval: " + str(upper_limit))


def problem6():
    print("\n----------------- Problem 6. Satterthwaite Estimation ----------------")
    """
    Notes: Last topic of Lecture 9.3 ("Comparison of two populations with unknown variances")
            # Variance = (Sample standard deviation) ** 2

    Given:
    • The sample file SatterthwaiteX.txt
    • The sample file SatterthwaiteY.txt

    Find:
    • What is the size of sample Satterthwaite-X, n?
    • What is the size of sample Satterthwaite-Y, m?
    • What is the sample standard deviation of Satterthwaite-X, 𝒔𝒙?
    • What is the sample standard deviation of Satterthwaite-Y, 𝒔𝒚?
    • Estimate the number of degrees of freedom v.
    """
    # ---Read in the sample files satterthwaiteX.txt and satterthwaiteY.txt---
    path1 = "/Users/Eddie Carrizales/OneDrive/Desktop/satterthwaiteX.txt"

    satterthwaiteX_data = np.loadtxt(path1, delimiter=" ")
    # print(satterthwaiteX_data)
    # print("")

    path2 = "/Users/Eddie Carrizales/OneDrive/Desktop/satterthwaiteY.txt"

    satterthwaiteY_data = np.loadtxt(path2, delimiter=" ")
    # print(satterthwaiteY_data)

    print("\nFind:")
    n = len(satterthwaiteX_data)
    print("The value of the sample Satterthwaite-X: " + str(n))

    m = len(satterthwaiteY_data)
    print("The value of the sample Satterthwaite-Y: " + str(m))

    s_X = math.sqrt(data_sample_variance(satterthwaiteX_data))
    s_X = round(s_X, 4)
    print("The value of the sample standard deviation of Satterthwaite-X, 𝒔𝒙: " + str(s_X))

    s_Y = math.sqrt(data_sample_variance(satterthwaiteY_data))
    s_Y = round(s_Y, 4)
    print("The value of the sample standard deviation of Satterthwaite-Y, 𝒔𝒚: " + str(s_Y))

    v = (s_X ** 2 / n + s_Y ** 2 / m) ** 2 / ((s_X ** 4 / (n ** 2 * (n - 1))) + (s_Y ** 4 / (m ** 2 * (m - 1))))
    v = round(v, 4)
    print("The estimated degrees of freedom v: " + str(v))


def problem7():
    print("\n-------------------- Problem 7. Hypothesis Testing -------------------\n")
    """
    Notes: 

    Given:
    • Sample file Duality.txt
    • The dataset has a normal distribution.
    • The confidence intervals are 99%, 95%, and 90%
    • The Z-Test target values are: 1.75, 2.50, and 3.00.
    • The population standard deviation is 1.2.

    Find:
    • Construct the three confidence intervals.
    • For each of the Z-Test targets
        o For each of the confidence intervals
            ▪ Show if the Z-Test targets fall within the confidence interval.
    """

    # Read in the sample file Duality.txt
    path = "/Users/Eddie Carrizales/OneDrive/Desktop/Duality.txt"

    duality_data = np.loadtxt(path, delimiter=" ")
    # print(duality_data)
    # print("")

    print("Given:")
    print("The dataset has a normal distribution.")
    print("The confidence intervals are 99%, 95%, and 90%")
    print("The Z-Test target values are: 1.75, 2.50, and 3.00.")
    sigma = 1.2
    print("The population standard deviation is: " + str(sigma))

    print("\nFind:")
    print(
        "Construct the three confidence intervals:")  # a confidence interval is basically: [lower_limit, upper_limit] interval
    print("For each of the Z-Test targets and for each of the confidence intervals")
    print("show if the Z-Test targets fall within the confidence interval:\n")
    confidence_interval_list = [.90, .95, .99]
    z_score_list = [1.645, 1.960, 2.576]
    z_test_list = [1.75, 2.50, 3.00]

    for i in range(len(z_test_list)):
        print("------------------------- Z-Test Target: " + str(z_test_list[i]) + "-------------------------")
        for j in range(len(confidence_interval_list)):
            construct_confidence_interval(duality_data, confidence_interval_list[j], z_score_list[j], sigma,
                                          z_test_list[i])
    print("---------------------------------------------------------------------")


def main():
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem6()
    problem7()


if __name__ == "__main__":
    main()
