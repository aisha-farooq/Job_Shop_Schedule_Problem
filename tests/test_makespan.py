import pickle
import unittest

from JSSP.data import Data
from JSSP.solution.makespan import compute_machine_makespans

"""
Test integrity of solution.makespan.compute_machine_makespans() function 
"""


class TestMakespan(unittest.TestCase):

    def __init__(self, *args):
        Data.initialize_data_from_csv('../data/given_data/sequenceDependencyMatrix.csv',
                                      '../data/given_data/machineRunSpeed.csv',
                                      '../data/given_data/jobTasks.csv')
        super(TestMakespan, self).__init__(*args)

    def test_makespan_integrity1(self):
        with open('./operation_matrices/operation_matrix1.pkl', 'rb') as fin:
            operation_matrix = pickle.load(fin)

        machine_makespans = [7996.268342767385, 8398.781671526705, 8343.87056502593, 6924.5613419194015,
                             7787.349643580393, 7397.651671526705, 8520.94199359736, 6546.192632325946]

        self.assertEqual(machine_makespans, list(compute_machine_makespans(operation_matrix,
                                                                           Data.machine_speeds,
                                                                           Data.sequence_dependency_matrix,
                                                                           Data.dependency_matrix_index_encoding)))

    def test_makespan_integrity2(self):
        with open('./operation_matrices/operation_matrix2.pkl', 'rb') as fin:
            operation_matrix = pickle.load(fin)

        machine_makespans = [7164.84732684664, 7826.668527368575, 7298.214357227469, 6836.4973312287375,
                             6670.195475155797, 7201.790941161677, 6566.151253038425, 6003.240322893379]

        self.assertEqual(machine_makespans, list(compute_machine_makespans(operation_matrix,
                                                                           Data.machine_speeds,
                                                                           Data.sequence_dependency_matrix,
                                                                           Data.dependency_matrix_index_encoding)))

    def test_makespan_integrity3(self):
        with open('./operation_matrices/operation_matrix3.pkl', 'rb') as fin:
            operation_matrix = pickle.load(fin)

        machine_makespans = [5622.211909610022, 6668.672413793104, 6198.45099818512, 7328.462489909265,
                             5576.7756781282205, 6459.11152450091, 6441.177636208749, 6614.8161680749035]

        self.assertEqual(machine_makespans, list(compute_machine_makespans(operation_matrix,
                                                                           Data.machine_speeds,
                                                                           Data.sequence_dependency_matrix,
                                                                           Data.dependency_matrix_index_encoding)))

    def test_makespan_integrity4(self):
        with open('./operation_matrices/operation_matrix4.pkl', 'rb') as fin:
            operation_matrix = pickle.load(fin)

        machine_makespans = [9989.582752327537, 10803.08454507686, 9811.387630376317, 7800.677606979643,
                             7691.085943026534, 10134.502752327537, 9078.174622487135, 9977.302745579258]

        self.assertEqual(machine_makespans, list(compute_machine_makespans(operation_matrix,
                                                                           Data.machine_speeds,
                                                                           Data.sequence_dependency_matrix,
                                                                           Data.dependency_matrix_index_encoding)))

    def test_makespan_integrity5(self):
        with open('./operation_matrices/operation_matrix5.pkl', 'rb') as fin:
            operation_matrix = pickle.load(fin)

        machine_makespans = [7887.918413494386, 8837.07330635202, 8506.797444283055, 7980.680300819141,
                             8334.323760072528, 7838.29338568095, 7910.037297677689, 7943.372792640731]

        self.assertEqual(machine_makespans, list(compute_machine_makespans(operation_matrix,
                                                                           Data.machine_speeds,
                                                                           Data.sequence_dependency_matrix,
                                                                           Data.dependency_matrix_index_encoding)))


if __name__ == '__main__':
    unittest.main()