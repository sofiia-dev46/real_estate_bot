from unittest import TestCase

from guardian_sample import GuardianSample


class TestGuardianSample(TestCase):
    def test_guardian_sample(self):
        assert GuardianSample()
