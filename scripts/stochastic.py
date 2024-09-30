import math
import random
from typing import List, Dict, Union, Optional
from functools import lru_cache
from itertools import cycle
import click
import numpy as np
from scipy import stats
from pydantic import BaseModel, Field
import matplotlib.pyplot as plt


def poissP(lambda_val: float, T: float, path: bool = True) -> List[float]:
    """
    Returns an array with the times of each arrival in a Poisson Process with rate `lambda` until time `T`.

    Args:
        lambda_val (float): Rate parameter.
        T (float): Time as positive number.
        path (bool, optional): If True, return full path. Defaults to True.

    Returns:
        List[float]: Times of each arrival in a Poisson Process.
    """
    N_t = [0]
    t = 0
    n = 0

    if T <= 0 or lambda_val <= 0:
        return N_t

    while t < T:
        U = random.random()
        exp = -math.log(U) / lambda_val
        t += exp
        if t < T:
            n += 1
            N_t.append(t)

    return N_t if path else [n]


def average(data: List[float]) -> float:
    """
    Returns the average of a list of numbers.

    Args:
        data (List[float]): List of numbers.

    Returns:
        float: Average of the numbers.
    """
    return sum(data) / len(data)


def mode(data: List[float]) -> float:
    """
    Returns the mode of a list of numbers.

    Args:
        data (List[float]): List of numbers.

    Returns:
        float: Mode of the numbers.
    """
    return max(set(data), key=data.count)


def std(values: List[float]) -> float:
    """
    Returns the standard deviation of a list of numbers.

    Args:
        values (List[float]): List of numbers.

    Returns:
        float: Standard deviation of the numbers.
    """
    avg = average(values)
    return math.sqrt(sum((x - avg) ** 2 for x in values) / len(values))


def summary(values: List[float]) -> Dict[str, float]:
    """
    Provides a summary of a set of data.

    Args:
        values (List[float]): List of numbers.

    Returns:
        Dict[str, float]: Summary statistics of the data.
    """
    sorted_values = sorted(values)
    return {
        "min": min(values),
        "max": max(values),
        "mean": average(values),
        "median": sorted_values[len(values) // 2],
        "std": std(values),
        "q1": sorted_values[len(values) // 4],
        "q3": sorted_values[3 * len(values) // 4],
    }


def mock(values: List[float], num: Optional[int] = None) -> List[float]:
    """
    Returns a mock data set that uses the same standard deviation and average.

    Args:
        values (List[float]): Original data set.
        num (Optional[int]): Number of mock values to generate. Defaults to len(values).

    Returns:
        List[float]: Mock data set.
    """
    return list(np.random.normal(average(values), std(values), num or len(values)))


def rsn(n: int, location: float, scale: float, shape: float = 0) -> List[float]:
    """
    Returns the Skew-Normal (SN) probability distribution.

    Args:
        n (int): Number of samples.
        location (float): Location parameter.
        scale (float): Scale parameter.
        shape (float, optional): Shape parameter. Defaults to 0.

    Returns:
        List[float]: Samples from the Skew-Normal distribution.
    """
    return list(stats.skewnorm.rvs(shape, loc=location, scale=scale, size=n))


def norm(mu: float = 1, sigma: float = 0, num: int = 1) -> List[float]:
    """
    Returns an array with `num` normal random variables in a normal distribution of mean `mu` and standard deviation `sigma`.

    Args:
        mu (float, optional): Mean of the distribution. Defaults to 1.
        sigma (float, optional): Standard deviation of the distribution. Defaults to 0.
        num (int, optional): Number of samples. Defaults to 1.

    Returns:
        List[float]: Samples from the normal distribution.
    """
    return list(np.random.normal(mu, sigma, num))


def brown(
    mu: float, sigma: float, T: float, steps: int, path: bool = True
) -> List[float]:
    """
    Returns an array corresponding to the path of Brownian motion.

    Args:
        mu (float): Drift parameter.
        sigma (float): Volatility parameter.
        T (float): Time.
        steps (int): Number of steps.
        path (bool, optional): If True, return full path. Defaults to True.

    Returns:
        List[float]: Brownian motion path.
    """
    if not (T > 0) or not (steps > 0):
        return [0]

    if not path:
        return [(mu * T) + (sigma * norm(0, math.sqrt(T), 1)[0])]

    dt = T / steps
    B_t = [0]
    B = 0

    for _ in range(steps):
        dB = (mu * dt) + (sigma * norm(0, math.sqrt(dt), 1)[0])
        B += dB
        B_t.append(B)

    return B_t


def GBM(
    S0: float, mu: float, sigma: float, T: float, steps: int, path: bool = True
) -> List[float]:
    """
    Returns an array corresponding to the path of geometric Brownian motion.

    Args:
        S0 (float): Initial value.
        mu (float): Drift parameter.
        sigma (float): Volatility parameter.
        T (float): Time.
        steps (int): Number of steps.
        path (bool, optional): If True, return full path. Defaults to True.

    Returns:
        List[float]: Geometric Brownian motion path.
    """
    if not (T > 0) or not (steps > 0):
        return [0]

    if not path:
        return [
            S0
            * math.exp(
                (mu - (sigma * sigma / 2)) * T + (sigma * norm(0, math.sqrt(T), 1)[0])
            )
        ]

    B_t = brown((mu - (sigma * sigma / 2)), sigma, T, steps, True)
    return [S0 * math.exp(B) for B in B_t]


def DTMC(
    transMatrix: List[List[float]], steps: int, start: int, path: bool = True
) -> List[int]:
    """
    Returns an array with the states at each step of the discrete-time Markov Chain.

    Args:
        transMatrix (List[List[float]]): Transition matrix.
        steps (int): Number of steps.
        start (int): Initial state.
        path (bool, optional): If True, return full path. Defaults to True.

    Returns:
        List[int]: Markov Chain path.
    """
    state = start
    path_list = [state]
    for _ in range(steps):
        state = random.choices(
            range(len(transMatrix[state])), weights=transMatrix[state]
        )[0]
        path_list.append(state)
    return path_list if path else [path_list[-1]]


def collate(states: List[int]) -> List[List[float]]:
    """
    Returns the transition matrix for an array of mapped states to numerical values.

    Args:
        states (List[int]): List of states.

    Returns:
        List[List[float]]: Transition matrix.
    """
    n = max(states) + 1
    counts = [[0] * n for _ in range(n)]
    for i in range(len(states) - 1):
        counts[states[i]][states[i + 1]] += 1
    return [
        [count / sum(row) if sum(row) > 0 else 0 for count in row] for row in counts
    ]


def CTMC(
    transMatrix: List[List[float]], T: float, start: int, path: bool = True
) -> Dict[float, int]:
    """
    Returns an object with the {key:value} pair {time:state} at each step of the continuous-time Markov Chain.

    Args:
        transMatrix (List[List[float]]): Transition matrix.
        T (float): Time.
        start (int): Initial state.
        path (bool, optional): If True, return full path. Defaults to True.

    Returns:
        Dict[float, int]: Continuous-time Markov chain.
    """
    state = start
    t = 0
    path_dict = {0: state}
    while t < T:
        rate = sum(transMatrix[state])
        t += random.expovariate(rate)
        if t > T:
            break
        state = random.choices(
            range(len(transMatrix[state])), weights=transMatrix[state]
        )[0]
        path_dict[t] = state
    return path_dict if path else {T: state}


def sample(arr: List[float], n: int) -> List[float]:
    """
    Generates a random sample (with replacement) from array `arr` of observations.

    Args:
        arr (List[float]): Array of observations.
        n (int): Number of samples.

    Returns:
        List[float]: Random sample.
    """
    return random.choices(arr, k=n)


def exp(lambda_val: float = 1) -> float:
    """
    Generates an exponential random variable with rate parameter `lambda`.

    Args:
        lambda_val (float, optional): Rate parameter. Defaults to 1.

    Returns:
        float: Exponential random variable.
    """
    return random.expovariate(lambda_val)


def pareto(x_m: float, alpha: float) -> float:
    """
    Generates a Pareto random variable with parameters `x_m` and `alpha`.

    Args:
        x_m (float): Scale parameter.
        alpha (float): Shape parameter.

    Returns:
        float: Pareto random variable.
    """
    return x_m / (random.random() ** (1 / alpha))


def hist(arr: List[float], n: Optional[int] = None) -> Dict[float, int]:
    """
    Generates a histogram object from an array of data.

    Args:
        arr (List[float]): Array of data.
        n (Optional[int]): Number of bins. If None, calculated based on data.

    Returns:
        Dict[float, int]: Histogram.
    """
    if n is None:
        n = int(math.sqrt(len(arr)))
    counts, bins = np.histogram(arr, bins=n)
    return dict(zip(bins[:-1], counts))


def create_mock_data(n: int = 1000, mu: float = 0, sigma: float = 1) -> List[float]:
    """
    Create mock data following a normal distribution.

    Args:
        n (int): Number of data points. Defaults to 1000.
        mu (float): Mean of the distribution. Defaults to 0.
        sigma (float): Standard deviation of the distribution. Defaults to 1.

    Returns:
        List[float]: Mock data following a normal distribution.
    """
    return list(np.random.normal(mu, sigma, n))


def plot_histogram(
    data: List[float], bins: Optional[int] = None, title: str = "Histogram of Mock Data"
):
    """
    Plot a histogram of the given data.

    Args:
        data (List[float]): Data to plot.
        bins (Optional[int]): Number of bins for the histogram. If None, automatically determined.
        title (str): Title of the plot. Defaults to "Histogram of Mock Data".
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, edgecolor="black")
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()


@click.command()
@click.option(
    "--function",
    type=click.Choice(
        [
            "poissP",
            "norm",
            "brown",
            "GBM",
            "DTMC",
            "CTMC",
            "mock_histogram",
            "mock_normal",
        ]
    ),
    default="mock_histogram",
    help="Function to test",
)
@click.option("--params", help="Comma-separated list of parameters")
def test_function(function: str, params: Optional[str]):
    """
    Test a stochastic function with given parameters or create mock data.
    """
    if function in ["mock_histogram", "mock_normal"]:
        if params:
            n, mu, sigma = map(float, params.split(","))
        else:
            n, mu, sigma = 1000, 0, 1

        data = create_mock_data(int(n), mu, sigma)

        if function == "mock_histogram":
            plot_histogram(
                data, title=f"Histogram of Mock Data (n={int(n)}, μ={mu}, σ={sigma})"
            )
        else:  # mock_normal
            click.echo(f"Generated {int(n)} mock data points with μ={mu} and σ={sigma}")
            click.echo(f"Sample mean: {np.mean(data):.4f}")
            click.echo(f"Sample standard deviation: {np.std(data):.4f}")

    elif params:
        params = [float(p) for p in params.split(",")]
        result = globals()[function](*params)
        click.echo(f"Result of {function}{tuple(params)}: {result}")

    else:
        click.echo(f"Please provide parameters for the {function} function.")


if __name__ == "__main__":
    test_function()
