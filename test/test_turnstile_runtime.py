import unittest


class SentinelRuntimeTests(unittest.TestCase):
    def test_real_sentinel_sdk_initializes(self) -> None:
        from utils.turnstile import _build_ctx

        context = _build_ctx(None)
        self.assertIsNotNone(context.eval("typeof SentinelSDK", timeout=2_000))


if __name__ == "__main__":
    unittest.main()
