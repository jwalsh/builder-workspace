# File: metrics_simulator.py

import time
import argparse
import random
from prometheus_client import start_http_server, Counter, Histogram, Gauge, Summary
from stochastic.processes.continuous import OrnsteinUhlenbeckProcess
from stochastic.processes.continuous import GeometricBrownianMotion
from stochastic.processes.noise import GaussianNoise

# RFC Metrics
RFC_TASKS_PROCESSED = Counter('rfc_tasks_processed', 'Number of RFC tasks processed')
RFC_PROCESSING_TIME = Histogram('rfc_processing_time_seconds', 'Time taken to process RFC tasks')
RFC_TASKS_FAILED = Counter('rfc_tasks_failed', 'Number of RFC tasks that failed processing')
CURRENT_RFC_TASKS = Gauge('current_rfc_tasks', 'Number of RFC tasks currently being processed')

# Implementation Metrics
IMPL_TASKS_STARTED = Counter('impl_tasks_started', 'Number of implementation tasks started')
IMPL_TASKS_COMPLETED = Counter('impl_tasks_completed', 'Number of implementation tasks completed')
IMPL_TIME = Histogram('impl_time_hours', 'Time taken to complete an implementation task')
CURRENT_IMPL_TASKS = Gauge('current_impl_tasks', 'Number of implementation tasks in progress')

# Code Review Metrics
CODE_REVIEWS_STARTED = Counter('code_reviews_started', 'Number of code reviews started')
CODE_REVIEWS_COMPLETED = Counter('code_reviews_completed', 'Number of code reviews completed')
CODE_REVIEW_TIME = Histogram('code_review_time_minutes', 'Time taken to complete a code review')
CURRENT_CODE_REVIEWS = Gauge('current_code_reviews', 'Number of code reviews in progress')

# Testing Metrics
TESTS_STARTED = Counter('tests_started', 'Number of test runs started')
TESTS_COMPLETED = Counter('tests_completed', 'Number of test runs completed')
TEST_DURATION = Histogram('test_duration_seconds', 'Duration of test runs')
TEST_COVERAGE = Gauge('test_coverage_percentage', 'Current test coverage percentage')
TEST_PASS_RATE = Gauge('test_pass_rate_percentage', 'Current test pass rate percentage')

# Agent Performance Metrics
AGENT_TASK_COMPLETION_RATE = Summary('agent_task_completion_rate', 'Task completion rate per agent', ['agent_type'])
AGENT_ERROR_RATE = Summary('agent_error_rate', 'Error rate per agent', ['agent_type'])

# DORA Metrics
DEPLOYMENT_FREQUENCY = Counter('deployment_frequency', 'Number of deployments', ['project'])
LEAD_TIME_FOR_CHANGES = Histogram('lead_time_for_changes_hours', 'Lead time for changes', ['project'])
TIME_TO_RESTORE_SERVICE = Histogram('time_to_restore_service_hours', 'Time to restore service', ['project'])
CHANGE_FAILURE_RATE = Gauge('change_failure_rate_percentage', 'Change failure rate', ['project'])

# SLO/SLI Metrics
SLO_AVAILABILITY = Gauge('slo_availability_percentage', 'Service availability percentage', ['project'])
SLO_LATENCY = Histogram('slo_latency_seconds', 'Service latency', ['project'])
SLO_ERROR_RATE = Gauge('slo_error_rate_percentage', 'Service error rate percentage', ['project'])

class MetricsSimulator:
    def __init__(self, num_projects=1000):
        self.ou_process = OrnsteinUhlenbeckProcess(speed=0.1, mean=0.5, vol=0.05)
        self.gbm_process = GeometricBrownianMotion(drift=0.1, volatility=0.2)
        self.gn_process = GaussianNoise(t=1.0)
        self.time = 0.0
        self.num_projects = num_projects
        self.projects = [f'project_{i}' for i in range(num_projects)]

    def simulate_rfc_metrics(self):
        processing_time = max(0.1, self.ou_process.sample(self.time))
        RFC_PROCESSING_TIME.observe(processing_time)
        current_tasks = max(1, int(self.gbm_process.sample(self.time)[-1] * 10))
        CURRENT_RFC_TASKS.set(current_tasks)
        RFC_TASKS_PROCESSED.inc()
        if self.gn_process.sample(self.time)[-1] > 1.5:
            RFC_TASKS_FAILED.inc()

    def simulate_impl_metrics(self):
        IMPL_TASKS_STARTED.inc()
        IMPL_TASKS_COMPLETED.inc(0.9)  # Assuming 90% completion rate
        IMPL_TIME.observe(max(1, self.ou_process.sample(self.time) * 10))  # in hours
        CURRENT_IMPL_TASKS.set(max(1, int(self.gbm_process.sample(self.time)[-1] * 5)))

    def simulate_code_review_metrics(self):
        CODE_REVIEWS_STARTED.inc()
        CODE_REVIEWS_COMPLETED.inc(0.95)  # Assuming 95% completion rate
        CODE_REVIEW_TIME.observe(max(15, self.ou_process.sample(self.time) * 60))  # in minutes
        CURRENT_CODE_REVIEWS.set(max(1, int(self.gbm_process.sample(self.time)[-1] * 3)))

    def simulate_testing_metrics(self):
        TESTS_STARTED.inc()
        TESTS_COMPLETED.inc()
        TEST_DURATION.observe(max(10, self.ou_process.sample(self.time) * 100))  # in seconds
        TEST_COVERAGE.set(min(100, max(70, 85 + self.gn_process.sample(self.time)[-1] * 5)))
        TEST_PASS_RATE.set(min(100, max(90, 95 + self.gn_process.sample(self.time)[-1] * 2)))

    def simulate_agent_performance(self):
        agent_types = ['rfc_processor', 'implementer', 'code_reviewer', 'tester']
        for agent_type in agent_types:
            AGENT_TASK_COMPLETION_RATE.labels(agent_type=agent_type).observe(
                max(0.5, min(1.0, 0.8 + self.gn_process.sample(self.time)[-1] * 0.1))
            )
            AGENT_ERROR_RATE.labels(agent_type=agent_type).observe(
                max(0, min(0.1, 0.05 + self.gn_process.sample(self.time)[-1] * 0.02))
            )

    def simulate_dora_metrics(self):
        for project in random.sample(self.projects, 10):  # Simulate for 10 random projects
            DEPLOYMENT_FREQUENCY.labels(project=project).inc(random.randint(1, 5))
            LEAD_TIME_FOR_CHANGES.labels(project=project).observe(max(0.1, self.ou_process.sample(self.time) * 24))
            TIME_TO_RESTORE_SERVICE.labels(project=project).observe(max(0.1, self.ou_process.sample(self.time) * 2))
            CHANGE_FAILURE_RATE.labels(project=project).set(min(100, max(0, 5 + self.gn_process.sample(self.time)[-1] * 2)))

    def simulate_slo_metrics(self):
        for project in random.sample(self.projects, 10):  # Simulate for 10 random projects
            SLO_AVAILABILITY.labels(project=project).set(min(100, max(90, 99.9 + self.gn_process.sample(self.time)[-1] * 0.1)))
            SLO_LATENCY.labels(project=project).observe(max(0.01, self.ou_process.sample(self.time) * 0.1))
            SLO_ERROR_RATE.labels(project=project).set(min(10, max(0, 1 + self.gn_process.sample(self.time)[-1] * 0.5)))

    def simulate_normal_operation(self):
        self.simulate_rfc_metrics()
        self.simulate_impl_metrics()
        self.simulate_code_review_metrics()
        self.simulate_testing_metrics()
        self.simulate_agent_performance()
        self.simulate_dora_metrics()
        self.simulate_slo_metrics()
        self.time += 1.0

    def simulate_problem_scenario(self):
        # RFC problems
        for _ in range(20):
            RFC_TASKS_PROCESSED.inc()
            RFC_TASKS_FAILED.inc()
        RFC_PROCESSING_TIME.observe(self.ou_process.sample(self.time) * 5)
        CURRENT_RFC_TASKS.set(int(self.gbm_process.sample(self.time)[-1] * 50))

        # Implementation problems
        CURRENT_IMPL_TASKS.set(int(self.gbm_process.sample(self.time)[-1] * 20))
        IMPL_TIME.observe(self.ou_process.sample(self.time) * 20)

        # Code review bottleneck
        CURRENT_CODE_REVIEWS.set(int(self.gbm_process.sample(self.time)[-1] * 10))
        CODE_REVIEW_TIME.observe(self.ou_process.sample(self.time) * 120)

        # Testing issues
        TEST_DURATION.observe(self.ou_process.sample(self.time) * 200)
        TEST_COVERAGE.set(max(50, 70 + self.gn_process.sample(self.time)[-1] * 10))
        TEST_PASS_RATE.set(max(70, 80 + self.gn_process.sample(self.time)[-1] * 5))

        # Agent performance degradation
        for agent_type in ['rfc_processor', 'implementer', 'code_reviewer', 'tester']:
            AGENT_TASK_COMPLETION_RATE.labels(agent_type=agent_type).observe(
                max(0.3, 0.5 + self.gn_process.sample(self.time)[-1] * 0.1)
            )
            AGENT_ERROR_RATE.labels(agent_type=agent_type).observe(
                min(0.2, 0.1 + self.gn_process.sample(self.time)[-1] * 0.05)
            )

        # DORA metrics problems
        for project in random.sample(self.projects, 5):
            TIME_TO_RESTORE_SERVICE.labels(project=project).observe(self.ou_process.sample(self.time) * 10)
            CHANGE_FAILURE_RATE.labels(project=project).set(min(100, max(0, 20 + self.gn_process.sample(self.time)[-1] * 10)))

        # SLO breaches
        for project in random.sample(self.projects, 5):
            SLO_AVAILABILITY.labels(project=project).set(min(100, max(80, 90 + self.gn_process.sample(self.time)[-1] * 5)))
            SLO_LATENCY.labels(project=project).observe(self.ou_process.sample(self.time) * 0.5)
            SLO_ERROR_RATE.labels(project=project).set(min(20, max(0, 5 + self.gn_process.sample(self.time)[-1] * 2)))

        self.time += 10.0

def run_simulator(duration_minutes, port):
    start_http_server(port)
    print(f"Metrics server started on port {port}")

    simulator = MetricsSimulator()
    start_time = time.time()
    last_problem_time = start_time - 900  # Start 15 minutes ago to trigger first problem immediately

    while time.time() - start_time < duration_minutes * 60:
        current_time = time.time()
        
        if current_time - last_problem_time >= 900:  # Every 15 minutes
            print("Simulating problem scenario...")
            simulator.simulate_problem_scenario()
            last_problem_time = current_time
            problem_end_time = current_time + 60
            while time.time() < problem_end_time:
                simulator.simulate_problem_scenario()
                time.sleep(1)
        else:
            simulator.simulate_normal_operation()
        
        time.sleep(1)  # Sleep for 1 second between iterations

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Agent Metrics Simulator")
    parser.add_argument("--duration", type=int, default=60, help="Duration to run the simulator (in minutes)")
    parser.add_argument("--port", type=int, default=9180, help="Port for the metrics server")
    args = parser.parse_args()

    run_simulator(args.duration, args.port)
