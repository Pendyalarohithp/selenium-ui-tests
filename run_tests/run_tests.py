import unittest

loader = unittest.TestLoader()
suite = loader.discover('run_tests')  # ← change from 'tests' to 'run_tests'

runner = unittest.TextTestRunner()
runner.run(suite)
