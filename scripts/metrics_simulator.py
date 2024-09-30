#!/usr/bin/env python3

import time
from typing import List, Dict, Callable
from functools import partial, lru_cache
from itertools import cycle, islice
import random
import click
from pydantic import BaseModel, Field
import numpy as np
from prometheus_client import start_http_server, Counter, Histogram, Gauge, Summary

# Metric definitions
RFC_TASKS_PROCESSED = Counter("rfc_tasks_processed", "Number of RFC tasks processed")
RFC_PROCESSING_TIME = Histogram(
    "rfc_processing_time_seconds", "Time taken to process RFC tasks"
)
RFC_TASKS_FAILED = Counter(
    "rfc_tasks_failed", "Number of RFC tasks that failed processing"
)
CURRENT_RFC_TASKS = Gauge(
    "current_rfc_tasks", "Number of RFC tasks currently being processed"
)

IMPL_TASKS_STARTED = Counter(
    "impl_tasks_started", "Number of implementation tasks started"
)
IMPL_TASKS_COMPLETED = Counter(
    "impl_tasks_completed", "Number of implementation tasks completed"
)
IMPL_TIME = Histogram(
    "impl_time_hours", "Time taken to complete an implementation task"
)
CURRENT_IMPL_TASKS = Gauge(
    "current_impl_tasks", "Number of implementation tasks in progress"
)

CODE_REVIEWS_STARTED = Counter("code_reviews_started", "Number of code reviews started")
CODE_REVIEWS_COMPLETED = Counter(
    "code_reviews_completed", "Number of code reviews completed"
)
CODE_REVIEW_TIME = Histogram(
    "code_review_time_minutes", "Time taken to complete a code review"
)
CURRENT_CODE_REVIEWS = Gauge(
    "current_code_reviews", "Number of code reviews in progress"
)

TESTS_STARTED = Counter("tests_started", "Number of test runs started")
TESTS_COMPLETED = Counter("tests_completed", "Number of test runs completed")
TEST_DURATION = Histogram("test_duration_seconds", "Duration of test runs")
TEST_COVERAGE = Gauge("test_coverage_percentage", "Current test coverage percentage")
TEST_PASS_RATE = Gauge("test_pass_rate_percentage", "Current test pass rate percentage")

AGENT_TASK_COMPLETION_RATE = Summary(
    "agent_task_completion_rate", "Task completion rate per agent", ["agent_type"]
)
AGENT_ERROR_RATE = Summary("agent_error_rate", "Error rate per agent", ["agent_type"])

DEPLOYMENT_FREQUENCY = Counter(
    "deployment_frequency", "Number of deployments", ["project"]
)
LEAD_TIME_FOR_CHANGES = Histogram(
    "lead_time_for_changes_hours", "Lead time for changes", ["project"]
)
TIME_TO_RESTORE_SERVICE = Histogram(
    "time_to_restore_service_hours", "Time to restore service", ["project"]
)
CHANGE_FAILURE_RATE = Gauge(
    "change_failure_rate_percentage", "Change failure rate", ["project"]
)

SLO_AVAILABILITY = Gauge(
    "slo_availability_percentage", "Service availability percentage", ["project"]
)
SLO_LATENCY = Histogram("slo_latency_seconds", "Service latency", ["project"])
SLO_ERROR_RATE = Gauge(
    "slo_error_rate_percentage", "Service error rate percentage", ["project"]
)


class Project(BaseModel):
    """Represents a project in the system."""

    id: str = Field(..., description="Unique identifier for the project")
    name: str = Field(..., description="Name of the project")


class MetricsSimulator:
    """
    Simulates metrics for an AI-assisted software development environment.

    This class generates realistic metrics data for various aspects of the
    development process, including RFC processing, implementation tasks,
    code reviews, testing, and overall project health.
    """

    def __init__(self, num_projects: int = 100):
        """
        Initialize the MetricsSimulator.

        Args:
            num_projects (int): Number of projects to simulate metrics for.
        """
        self.time = 0.0
        self.projects = [
            Project(id=f"project_{i}", name=f"Project {i}") for i in range(num_projects)
        ]

    def __repr__(self) -> str:
        """
        Return a string representation of the MetricsSimulator.

        This method returns the current status summary as a formatted string.

        Returns:
            str: A formatted string containing the current simulation status.
        """
        summary = self.get_status_summary()
        return "\n".join(f"{key}: {value:.2f}" for key, value in summary.items())

    @lru_cache(maxsize=None)
    def _get_random_projects(self, n: int) -> List[Project]:
        """
        Get a list of random projects.

        Args:
            n (int): Number of random projects to return.

        Returns:
            List[Project]: A list of randomly selected projects.
        """
        return random.sample(self.projects, n)

    def simulate_rfc_metrics(self) -> None:
        """Simulate RFC processing metrics."""
        processing_time = max(0.1, np.random.normal(0.5, 0.1))
        RFC_PROCESSING_TIME.observe(processing_time)
        current_tasks = max(1, int(np.random.gamma(10, 1)))
        CURRENT_RFC_TASKS.set(current_tasks)
        RFC_TASKS_PROCESSED.inc()
        if np.random.random() > 0.95:  # 5% chance of failure
            RFC_TASKS_FAILED.inc()

    def simulate_impl_metrics(self) -> None:
        """Simulate implementation task metrics."""
        IMPL_TASKS_STARTED.inc()
        IMPL_TASKS_COMPLETED.inc(0.9)  # Assuming 90% completion rate
        IMPL_TIME.observe(max(1, np.random.normal(10, 2)))  # in hours
        CURRENT_IMPL_TASKS.set(max(1, int(np.random.gamma(5, 1))))

    def simulate_code_review_metrics(self) -> None:
        """Simulate code review metrics."""
        CODE_REVIEWS_STARTED.inc()
        CODE_REVIEWS_COMPLETED.inc(0.95)  # Assuming 95% completion rate
        CODE_REVIEW_TIME.observe(max(15, np.random.normal(60, 15)))  # in minutes
        CURRENT_CODE_REVIEWS.set(max(1, int(np.random.gamma(3, 1))))

    def simulate_testing_metrics(self) -> None:
        """Simulate testing metrics."""
        TESTS_STARTED.inc()
        TESTS_COMPLETED.inc()
        TEST_DURATION.observe(max(10, np.random.normal(100, 20)))  # in seconds
        TEST_COVERAGE.set(min(100, max(70, np.random.normal(85, 5))))
        TEST_PASS_RATE.set(min(100, max(90, np.random.normal(95, 2))))

    def simulate_agent_performance(self) -> None:
        """Simulate agent performance metrics."""
        agent_types = ["rfc_processor", "implementer", "code_reviewer", "tester"]
        for agent_type in agent_types:
            AGENT_TASK_COMPLETION_RATE.labels(agent_type=agent_type).observe(
                max(0.5, min(1.0, np.random.normal(0.8, 0.1)))
            )
            AGENT_ERROR_RATE.labels(agent_type=agent_type).observe(
                max(0, min(0.1, np.random.normal(0.05, 0.02)))
            )

    def simulate_dora_metrics(self) -> None:
        """Simulate DORA (DevOps Research and Assessment) metrics."""
        for project in self._get_random_projects(10):
            DEPLOYMENT_FREQUENCY.labels(project=project.id).inc(np.random.randint(1, 6))
            LEAD_TIME_FOR_CHANGES.labels(project=project.id).observe(
                max(0.1, np.random.normal(24, 6))
            )
            TIME_TO_RESTORE_SERVICE.labels(project=project.id).observe(
                max(0.1, np.random.normal(2, 0.5))
            )
            CHANGE_FAILURE_RATE.labels(project=project.id).set(
                min(100, max(0, np.random.normal(5, 2)))
            )

    def simulate_slo_metrics(self) -> None:
        """Simulate SLO (Service Level Objective) metrics."""
        for project in self._get_random_projects(10):
            SLO_AVAILABILITY.labels(project=project.id).set(
                min(100, max(90, np.random.normal(99.9, 0.1)))
            )
            SLO_LATENCY.labels(project=project.id).observe(
                max(0.01, np.random.normal(0.1, 0.02))
            )
            SLO_ERROR_RATE.labels(project=project.id).set(
                min(10, max(0, np.random.normal(1, 0.5)))
            )

    def simulate_normal_operation(self) -> None:
        """Simulate metrics for normal operation."""
        self.simulate_rfc_metrics()
        self.simulate_impl_metrics()
        self.simulate_code_review_metrics()
        self.simulate_testing_metrics()
        self.simulate_agent_performance()
        self.simulate_dora_metrics()
        self.simulate_slo_metrics()
        self.time += 1.0

    def get_status_summary(self) -> Dict[str, float]:
        """
        Provide a high-level summary of the current simulation status.
        
        Returns:
        Dict[str, float]: A dictionary containing key metrics.
        """
        return {
            "time": round(self.time, 2),
            "rfc_tasks": CURRENT_RFC_TASKS._value.get(),
            "impl_tasks": CURRENT_IMPL_TASKS._value.get(),
            "code_reviews": CURRENT_CODE_REVIEWS._value.get(),
            "test_coverage": TEST_COVERAGE._value.get(),
            "test_pass_rate": TEST_PASS_RATE._value.get(),
            "avg_slo_availability": np.mean(
                [
                    SLO_AVAILABILITY.labels(project=p.id)._value.get()
                    for p in self._get_random_projects(10)
                ]
            ),
            "avg_change_failure_rate": np.mean(
                [
                    CHANGE_FAILURE_RATE.labels(project=p.id)._value.get()
                    for p in self._get_random_projects(10)
                ]
            ),
        }

    def simulate_problem_scenario(self) -> None:
        """Simulate metrics for a problem scenario."""
        # RFC problems
        for _ in range(20):
            RFC_TASKS_PROCESSED.inc()
            RFC_TASKS_FAILED.inc()
        RFC_PROCESSING_TIME.observe(np.random.normal(2.5, 0.5))
        CURRENT_RFC_TASKS.set(int(np.random.gamma(50, 1)))

        # Implementation problems
        CURRENT_IMPL_TASKS.set(int(np.random.gamma(20, 1)))
        IMPL_TIME.observe(np.random.normal(20, 4))

        # Code review bottleneck
        CURRENT_CODE_REVIEWS.set(int(np.random.gamma(10, 1)))
        CODE_REVIEW_TIME.observe(np.random.normal(120, 30))

        # Testing issues
        TEST_DURATION.observe(np.random.normal(200, 40))
        TEST_COVERAGE.set(max(50, np.random.normal(70, 10)))
        TEST_PASS_RATE.set(max(70, np.random.normal(80, 5)))

        # Agent performance degradation
        for agent_type in ["rfc_processor", "implementer", "code_reviewer", "tester"]:
            AGENT_TASK_COMPLETION_RATE.labels(agent_type=agent_type).observe(
                max(0.3, np.random.normal(0.5, 0.1))
            )
            AGENT_ERROR_RATE.labels(agent_type=agent_type).observe(
                min(0.2, np.random.normal(0.1, 0.05))
            )

        # DORA metrics problems
        for project in self._get_random_projects(5):
            TIME_TO_RESTORE_SERVICE.labels(project=project.id).observe(
                np.random.normal(10, 2)
            )
            CHANGE_FAILURE_RATE.labels(project=project.id).set(
                min(100, max(0, np.random.normal(20, 5)))
            )

        # SLO breaches
        for project in self._get_random_projects(5):
            SLO_AVAILABILITY.labels(project=project.id).set(
                min(100, max(80, np.random.normal(90, 5)))
            )
            SLO_LATENCY.labels(project=project.id).observe(np.random.normal(0.5, 0.1))
            SLO_ERROR_RATE.labels(project=project.id).set(
                min(20, max(0, np.random.normal(5, 2)))
            )

        self.time += 10.0

def run_simulator(duration_minutes: int, port: int) -> None:
    """
    Run the metrics simulator for a specified duration.

    Args:
        duration_minutes (int): Duration to run the simulator in minutes.
        port (int): Port number to start the HTTP server on.
    """
    start_http_server(port)
    print(f"Metrics server started on port {port}")

    simulator = MetricsSimulator()
    start_time = time.time()
    last_problem_time = start_time  # Initialize to start_time
    last_summary_time = start_time
    problem_duration = 60  # Duration of problem scenario in seconds

    print(f"Starting simulation for {duration_minutes} minutes...")
    print("Normal operation will run for 15 minutes before the first problem scenario.")

    for _ in range(int(duration_minutes * 60)):
        current_time = time.time()
        elapsed_time = current_time - start_time

        # Check if it's time for a problem scenario (every 15 minutes, but not at the start)
        if elapsed_time >= 900 and current_time - last_problem_time >= 900:
            print(f"\n[{elapsed_time:.0f}s] Simulating problem scenario for 1 minute...")
            problem_end_time = current_time + problem_duration
            while time.time() < problem_end_time:
                simulator.simulate_problem_scenario()
                time.sleep(1)
            last_problem_time = time.time()
            print(f"[{elapsed_time + problem_duration:.0f}s] Problem scenario ended. Resuming normal operation.")
        else:
            simulator.simulate_normal_operation()

        # Print summary every 60 seconds
        if current_time - last_summary_time >= 60:
            elapsed_minutes = (current_time - start_time) / 60
            print(f"\n[{elapsed_minutes:.1f} minutes] Current Simulation Status:")
            print(simulator)
            last_summary_time = current_time

        time.sleep(1)  # Sleep for 1 second between iterations

    total_runtime = time.time() - start_time
    print(f"\nSimulation completed. Total runtime: {total_runtime/60:.2f} minutes.")
    print("Final Simulation Status:")
    print(simulator)


@click.command()
@click.option(
    "--duration", default=60, help="Duration to run the simulator (in minutes)"
)
@click.option("--port", default=9180, help="Port for the metrics server")
def main(duration: int, port: int) -> None:
    """
    Main entry point for the metrics simulator.

    This function sets up and runs the metrics simulator with the specified duration and port.

    Args:
        duration (int): Duration to run the simulator in minutes.
        port (int): Port number to start the HTTP server on.
    """
    click.echo(f"Starting metrics simulator for {duration} minutes on port {port}")
    run_simulator(duration, port)
    click.echo("Metrics simulation completed")


if __name__ == "__main__":
    main()
