import os
import unittest

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = '''
    快速测试: 没有数据库migration的单元测试, 区别于django test.
    但是连接的不是测试数据库, 而是实际开发用的数据库，对于数据库的操作会保留下来.
    因此最好不要测试含有数据库操作的代码，适用于"工具算法测试"或"第三方API测试".
    TODO: 对于这点，以后再优化.
    '''
    test_suite = unittest.TestSuite
    test_runner = unittest.TextTestRunner
    test_loader = unittest.defaultTestLoader
    verbosity = 1
    failfast = False
    default_test_file = 'app.fast_tests'  # TODO: 指定文件名或patter, 遍历django installed apps

    def add_arguments(self, parser):
        parser.add_argument(
            'test_labels',
            nargs='*',
            help='测试文件,类或方法。例如%s, 默认%s,' %('app.tests.TestAlgorithm', self.default_test_file),
        )

    def build_suite(self, test_labels=None):
        suite = self.test_suite()
        test_labels = test_labels or [self.default_test_file]

        for label in test_labels:
            label_as_path = os.path.abspath(label)

            # if a module, or "module.ClassName[.method_name]", just run those
            if not os.path.exists(label_as_path):
                tests = self.test_loader.loadTestsFromName(label)
                suite.addTests(tests)

        return suite

    def run_suite(self, suite, **kwargs):
        return self.test_runner(
            verbosity=self.verbosity,
            failfast=self.failfast,
        ).run(suite)

    def init(self, *args, **options):
        unittest.installHandler()

    def deinit(self):
        unittest.removeHandler()

    def handle(self, *args, **options):
        self.verbosity = options.get('verbosity', 1)
        test_labels = options.get('test_labels')
        self.init(*args, **options)
        suite = self.build_suite(test_labels)
        result = self.run_suite(suite)
        self.deinit()
