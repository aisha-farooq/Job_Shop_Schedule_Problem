import os
import shutil
import unittest

from JSSP.data import Data
from JSSP.solver import Solver
from JSSP.genetic_algorithm import GASelectionEnum
from tests import project_root, tmp_dir

"""
Test the genetic algorithm
"""


class TestGA(unittest.TestCase):

    def setUp(self) -> None:
        if not os.path.exists(tmp_dir):
            os.mkdir(tmp_dir)

        Data.initialize_data_from_csv(
            project_root + os.sep + 'data' + os.sep + 'given_data' + os.sep + 'sequenceDependencyMatrix.csv',
            project_root + os.sep + 'data' + os.sep + 'given_data' + os.sep + 'machineRunSpeed.csv',
            project_root + os.sep + 'data' + os.sep + 'given_data' + os.sep + 'jobTasks.csv')

    def tearDown(self) -> None:
        shutil.rmtree(tmp_dir, ignore_errors=True)

    def test_ga_time(self):

        try:

            # parameters
            runtime = 5  # seconds
            population = None
            population_size = 100
            mutation_probability = 0.8
            selection_size = 5

            # run GA
            solver = Solver()
            solver.genetic_algorithm_time(runtime=runtime,
                                          population=population,
                                          population_size=population_size,
                                          mutation_probability=mutation_probability,
                                          selection_size=selection_size)
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))

        self.assertIsNotNone(solver.solution)
        self.assertIsNotNone(solver.ga_agent)

        # test parameters were set
        self.assertEqual(runtime, solver.ga_agent.runtime)
        self.assertTrue(solver.ga_agent.time_condition)
        self.assertFalse(solver.ga_agent.benchmark)
        self.assertEqual(population_size, solver.ga_agent.population_size)
        self.assertEqual(mutation_probability, solver.ga_agent.mutation_probability)
        self.assertEqual(selection_size, solver.ga_agent.selection_size)

        self.assertNotEqual(0, len(solver.ga_agent.initial_population))
        self.assertNotEqual(0, len(solver.ga_agent.result_population))
        self.assertEqual(len(solver.ga_agent.initial_population), len(solver.ga_agent.result_population))

        # test that the result solution is better than all the solutions in the initial population
        for initial_sol in solver.ga_agent.initial_population:
            self.assertLessEqual(solver.solution, initial_sol)

        # output results
        solver.solution.create_schedule_xlsx_file(tmp_dir, filename='ga_test_schedule')
        self.assertTrue(os.path.exists(tmp_dir + os.sep + 'ga_test_schedule.xlsx'),
                        "ga_test_schedule.xlsx was not produced")

    def test_ga_time_benchmark(self):

        try:

            # parameters
            runtime = 5  # seconds
            population = None
            population_size = 100
            mutation_probability = 0.8
            selection_size = 5

            solver = Solver()
            solver.genetic_algorithm_time(runtime=runtime,
                                          population=population,
                                          population_size=population_size,
                                          mutation_probability=mutation_probability,
                                          selection_size=selection_size,
                                          benchmark=True)
        except Exception as e:
            self.fail("Unexpected exception raised:" + str(e))

        self.assertIsNotNone(solver.solution)
        self.assertIsNotNone(solver.ga_agent)

        # test parameters were set
        self.assertEqual(runtime, solver.ga_agent.runtime)
        self.assertTrue(solver.ga_agent.time_condition)
        self.assertTrue(solver.ga_agent.benchmark)
        self.assertEqual(population_size, solver.ga_agent.population_size)
        self.assertEqual(mutation_probability, solver.ga_agent.mutation_probability)
        self.assertEqual(selection_size, solver.ga_agent.selection_size)

        self.assertNotEqual(0, len(solver.ga_agent.initial_population))
        self.assertNotEqual(0, len(solver.ga_agent.result_population))
        self.assertEqual(len(solver.ga_agent.initial_population), len(solver.ga_agent.result_population))

        # test that the result solution is better than all the solutions in the initial population
        for initial_sol in solver.ga_agent.initial_population:
            self.assertLessEqual(solver.solution, initial_sol)

        # test benchmark results were produced
        self.assertNotEqual(0, len(solver.ga_agent.best_solution_makespan_v_iter))
        self.assertNotEqual(0, len(solver.ga_agent.avg_population_makespan_v_iter))
        self.assertNotEqual(0, len(solver.ga_agent.min_makespan_coordinates))

        # output results
        solver.output_benchmark_results(tmp_dir, name='ga_test_benchmark', auto_open=False)
        self.assertTrue(os.path.exists(tmp_dir + os.sep + 'ga_test_benchmark'),
                        "GA benchmark results were not produced")
        self.assertTrue(os.path.exists(tmp_dir + os.sep + 'ga_test_benchmark' + os.sep + 'index.html'),
                        "GA benchmark results index.html was not produced")
        self.assertTrue(os.path.exists(tmp_dir + os.sep + 'ga_test_benchmark' + os.sep + 'ga_makespans.html'),
                        "GA benchmark results ga_makespans.html was not produced")
        self.assertTrue(os.path.exists(tmp_dir + os.sep + 'ga_test_benchmark' + os.sep + 'ga_schedule.xlsx'),
                        "GA benchmark results ga_schedule.xlsx was not produced")

    def test_ga_iter(self):

        try:

            # parameters
            iterations = 50
            population = None
            population_size = 100
            mutation_probability = 0.8
            selection_size = 5

            # run GA
            solver = Solver()
            solver.genetic_algorithm_iter(iterations=iterations,
                                          population=population,
                                          population_size=population_size,
                                          mutation_probability=mutation_probability,
                                          selection_size=selection_size)
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))

        self.assertIsNotNone(solver.solution)
        self.assertIsNotNone(solver.ga_agent)

        # test parameters were set
        self.assertEqual(iterations, solver.ga_agent.iterations)
        self.assertFalse(solver.ga_agent.time_condition)
        self.assertFalse(solver.ga_agent.benchmark)
        self.assertEqual(population_size, solver.ga_agent.population_size)
        self.assertEqual(mutation_probability, solver.ga_agent.mutation_probability)
        self.assertEqual(selection_size, solver.ga_agent.selection_size)

        self.assertNotEqual(0, len(solver.ga_agent.initial_population))
        self.assertNotEqual(0, len(solver.ga_agent.result_population))
        self.assertEqual(len(solver.ga_agent.initial_population), len(solver.ga_agent.result_population))

        # test that the result solution is better than all the solutions in the initial population
        for initial_sol in solver.ga_agent.initial_population:
            self.assertLessEqual(solver.solution, initial_sol)

        # output results
        solver.solution.create_schedule_xlsx_file(tmp_dir, filename='ga_test_schedule')
        self.assertTrue(os.path.exists(tmp_dir + os.sep + 'ga_test_schedule.xlsx'),
                        "ga_test_schedule.xlsx was not produced")

    def test_ga_iter_benchmark(self):

        try:

            # parameters
            iterations = 50
            population = None
            population_size = 100
            mutation_probability = 0.8
            selection_size = 5

            solver = Solver()
            solver.genetic_algorithm_iter(iterations=iterations,
                                          population=population,
                                          population_size=population_size,
                                          mutation_probability=mutation_probability,
                                          selection_size=selection_size,
                                          benchmark=True)
        except Exception as e:
            self.fail("Unexpected exception raised:" + str(e))

        self.assertIsNotNone(solver.solution)
        self.assertIsNotNone(solver.ga_agent)

        # test parameters were set
        self.assertEqual(iterations, solver.ga_agent.iterations)
        self.assertFalse(solver.ga_agent.time_condition)
        self.assertTrue(solver.ga_agent.benchmark)
        self.assertEqual(population_size, solver.ga_agent.population_size)
        self.assertEqual(mutation_probability, solver.ga_agent.mutation_probability)
        self.assertEqual(selection_size, solver.ga_agent.selection_size)

        self.assertNotEqual(0, len(solver.ga_agent.initial_population))
        self.assertNotEqual(0, len(solver.ga_agent.result_population))
        self.assertEqual(len(solver.ga_agent.initial_population), len(solver.ga_agent.result_population))

        # test that the result solution is better than all the solutions in the initial population
        for initial_sol in solver.ga_agent.initial_population:
            self.assertLessEqual(solver.solution, initial_sol)

        # test benchmark results were produced
        self.assertNotEqual(0, len(solver.ga_agent.best_solution_makespan_v_iter))
        self.assertNotEqual(0, len(solver.ga_agent.avg_population_makespan_v_iter))
        self.assertNotEqual(0, len(solver.ga_agent.min_makespan_coordinates))

        # # output results
        solver.output_benchmark_results(tmp_dir, name='ga_test_benchmark', auto_open=False)
        self.assertTrue(os.path.exists(tmp_dir + os.sep + 'ga_test_benchmark'),
                        "GA benchmark results were not produced")
        self.assertTrue(os.path.exists(tmp_dir + os.sep + 'ga_test_benchmark' + os.sep + 'index.html'),
                        "GA benchmark results index.html was not produced")
        self.assertTrue(os.path.exists(tmp_dir + os.sep + 'ga_test_benchmark' + os.sep + 'ga_makespans.html'),
                        "GA benchmark results ga_makespans.html was not produced")
        self.assertTrue(os.path.exists(tmp_dir + os.sep + 'ga_test_benchmark' + os.sep + 'ga_schedule.xlsx'),
                        "GA benchmark results ga_schedule.xlsx was not produced")


class TestGASelectionMethods(unittest.TestCase):

    def setUp(self) -> None:
        Data.initialize_data_from_csv(
            project_root + os.sep + 'data' + os.sep + 'given_data' + os.sep + 'sequenceDependencyMatrix.csv',
            project_root + os.sep + 'data' + os.sep + 'given_data' + os.sep + 'machineRunSpeed.csv',
            project_root + os.sep + 'data' + os.sep + 'given_data' + os.sep + 'jobTasks.csv')

    def test_tournament_selection(self):

        try:

            # parameters
            iterations = 50
            population = None
            population_size = 100
            mutation_probability = 0.8
            selection_size = 5
            selection_method = GASelectionEnum.TOURNAMENT

            # run GA
            solver = Solver()
            solver.genetic_algorithm_iter(iterations=iterations,
                                          population=population,
                                          population_size=population_size,
                                          selection_method_enum=selection_method,
                                          mutation_probability=mutation_probability,
                                          selection_size=selection_size)
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))

        self.assertIsNotNone(solver.solution)
        self.assertIsNotNone(solver.ga_agent)

        # test parameters were set
        self.assertEqual(iterations, solver.ga_agent.iterations)
        self.assertFalse(solver.ga_agent.time_condition)
        self.assertFalse(solver.ga_agent.benchmark)
        self.assertEqual(population_size, solver.ga_agent.population_size)
        self.assertEqual(mutation_probability, solver.ga_agent.mutation_probability)
        self.assertEqual(selection_size, solver.ga_agent.selection_size)
        self.assertEqual(selection_method, solver.ga_agent.selection_method)

        self.assertNotEqual(0, len(solver.ga_agent.initial_population))
        self.assertNotEqual(0, len(solver.ga_agent.result_population))
        self.assertEqual(len(solver.ga_agent.initial_population), len(solver.ga_agent.result_population))

        # test that the result solution is better than all the solutions in the initial population
        for initial_sol in solver.ga_agent.initial_population:
            self.assertLessEqual(solver.solution, initial_sol)

        # test that the result population does not have duplicate solutions
        seen = []
        self.assertFalse(any(sol in seen or seen.append(sol) for sol in solver.ga_agent.result_population))

    def test_fitness_proportionate_selection(self):

        try:

            # parameters
            iterations = 50
            population = None
            population_size = 100
            mutation_probability = 0.8
            selection_method = GASelectionEnum.FITNESS_PROPORTIONATE

            # run GA
            solver = Solver()
            solver.genetic_algorithm_iter(iterations=iterations,
                                          population=population,
                                          population_size=population_size,
                                          selection_method_enum=selection_method,
                                          mutation_probability=mutation_probability,
                                          selection_size=None)
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))

        self.assertIsNotNone(solver.solution)
        self.assertIsNotNone(solver.ga_agent)

        # test parameters were set
        self.assertEqual(iterations, solver.ga_agent.iterations)
        self.assertFalse(solver.ga_agent.time_condition)
        self.assertFalse(solver.ga_agent.benchmark)
        self.assertEqual(population_size, solver.ga_agent.population_size)
        self.assertEqual(mutation_probability, solver.ga_agent.mutation_probability)
        self.assertEqual(selection_method, solver.ga_agent.selection_method)

        self.assertNotEqual(0, len(solver.ga_agent.initial_population))
        self.assertNotEqual(0, len(solver.ga_agent.result_population))
        self.assertEqual(len(solver.ga_agent.initial_population), len(solver.ga_agent.result_population))

        # test that the result solution is better than all the solutions in the initial population
        for initial_sol in solver.ga_agent.initial_population:
            self.assertLessEqual(solver.solution, initial_sol)

        # test that the result population does not have duplicate solutions
        seen = []
        self.assertFalse(any(sol in seen or seen.append(sol) for sol in solver.ga_agent.result_population))

    def test_random_selection(self):

        try:

            # parameters
            iterations = 50
            population = None
            population_size = 100
            mutation_probability = 0.8
            selection_method = GASelectionEnum.RANDOM

            # run GA
            solver = Solver()
            solver.genetic_algorithm_iter(iterations=iterations,
                                          population=population,
                                          population_size=population_size,
                                          selection_method_enum=selection_method,
                                          mutation_probability=mutation_probability,
                                          selection_size=None)
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))

        self.assertIsNotNone(solver.solution)
        self.assertIsNotNone(solver.ga_agent)

        # test parameters were set
        self.assertEqual(iterations, solver.ga_agent.iterations)
        self.assertFalse(solver.ga_agent.time_condition)
        self.assertFalse(solver.ga_agent.benchmark)
        self.assertEqual(population_size, solver.ga_agent.population_size)
        self.assertEqual(mutation_probability, solver.ga_agent.mutation_probability)
        self.assertEqual(selection_method, solver.ga_agent.selection_method)

        self.assertNotEqual(0, len(solver.ga_agent.initial_population))
        self.assertNotEqual(0, len(solver.ga_agent.result_population))
        self.assertEqual(len(solver.ga_agent.initial_population), len(solver.ga_agent.result_population))

        # test that the result solution is better than all the solutions in the initial population
        for initial_sol in solver.ga_agent.initial_population:
            self.assertLessEqual(solver.solution, initial_sol)

        # test that the result population does not have duplicate solutions
        seen = []
        self.assertFalse(any(sol in seen or seen.append(sol) for sol in solver.ga_agent.result_population))


if __name__ == '__main__':
    unittest.main()