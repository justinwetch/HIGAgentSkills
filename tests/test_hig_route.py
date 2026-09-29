import importlib.util
import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).parents[1]
spec = importlib.util.spec_from_file_location('hig_route', ROOT/'scripts/hig_route.py')
router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(router)


class RouteTests(unittest.TestCase):
    def test_explicit_target_exclusion_applies_to_direct_and_related(self):
        result = router.route(ROOT, 'Design for macOS, not iPhone Duo.', ['designing-for-iphone-duo', 'designing-for-ios'])
        self.assertIn('designing-for-macos', result['initial'])
        self.assertNotIn('references/hig/designing-for-iphone-duo.md', result['files'])
        self.assertNotIn('designing-for-ios', result['initial'])
        result = router.route(ROOT, 'Design for iOS on iPhone, not iPhone Duo.', ['designing-for-iphone-duo'])
        self.assertIn('designing-for-ios', result['initial'])
        self.assertNotIn('references/hig/designing-for-iphone-duo.md', result['files'])
        result = router.route(ROOT, 'iPhone Duo', ['designing-for-games'])
        self.assertNotIn('references/hig/designing-for-games.md', result['files'])
        for topic in ('not-a-topic', 'accessibility'):
            with self.assertRaises(ValueError):
                router.route(ROOT, 'iOS', [topic])

    def test_six_platforms(self):
        for name in ('ios', 'ipados', 'macos', 'tvos', 'visionos', 'watchos'):
            with self.subTest(name=name):
                result = router.route(ROOT, name)
                self.assertIn('designing-for-'+name, result['initial'])
                self.assertEqual(len(result['foundations']), 16)

    def test_duo_implies_ios_and_all_related_without_second_hop(self):
        result = router.route(ROOT, 'Explain tab bar and toolbar for iPhone Duo, two apps side by side.')
        self.assertIn('designing-for-ios', result['initial'])
        self.assertIn('designing-for-iphone-duo', result['initial'])
        self.assertNotIn('multitasking', result['initial'])
        self.assertIn('multitasking', result['one_hop_related'])
        self.assertIn('designing-for-games', result['one_hop_related'])
        self.assertNotIn('references/hig/playing-video.md', result['files'])
        self.assertNotIn('references/hig/windows.md', result['files'])
        self.assertNotIn('references/hig/game-controls.md', result['files'])
        self.assertNotIn('references/hig/augmented-reality.md', result['files'])
        self.assertNotIn('references/hig/generative-ai.md', result['files'])
        self.assertEqual(len(result['files']), len(set(result['files'])))

    def test_actual_literal_match_spans(self):
        request = 'An iOS Tab Bar with ToolbarOverflowMenu.'
        result = router.route(ROOT, request)
        for record in result['initial'].values():
            for match in record['matches']:
                start, end = match['span']
                self.assertEqual(request[start:end], match['matched_text'])
                self.assertTrue(re.fullmatch(router.trigger_pattern(match['trigger']), match['matched_text'], re.IGNORECASE))

    def test_plural_hyphenated_and_bare_symbol_forms_match(self):
        result = router.route(ROOT, 'Design the tab bars, sheets and toggles in my games for iPhones.')
        for topic in ('tab-bars', 'sheets', 'toggles', 'designing-for-games', 'designing-for-ios'):
            self.assertIn(topic, result['initial'])
        result = router.route(ROOT, 'A full-screen always-on sign-in flow with keyboardType and persistentSystemOverlays.')
        for topic in ('going-full-screen', 'always-on', 'managing-accounts', 'virtual-keyboards', 'gestures'):
            self.assertIn(topic, set(result['initial']) | set(result['direct_tier4']))

    def test_generic_words_do_not_trigger_duo(self):
        for request in ('A duo-tone icon', 'Google Duo call screen', 'Duolingo-style streaks',
                        'A vertical controls panel', 'An arrangement view for my music sequencer'):
            with self.subTest(request=request):
                self.assertNotIn('designing-for-iphone-duo', router.route(ROOT, request)['initial'])
        for request in ('iPhone Duo', 'a foldable iPhone', "the iPhone Duo's reserved regions"):
            with self.subTest(request=request):
                self.assertIn('designing-for-iphone-duo', router.route(ROOT, request)['initial'])

    def test_cli_handles_non_ascii_utf16_and_missing_files(self):
        import os, subprocess, sys, tempfile
        env = {**os.environ, 'PYTHONIOENCODING': 'cp1252'}
        env.pop('PYTHONUTF8', None)
        with tempfile.TemporaryDirectory() as tmp:
            for name, data in (('utf8.txt', 'Tab bar for iPhone \U0001f4f1 日本'.encode('utf-8')),
                               ('utf16.txt', 'Tab bar for iPhone é'.encode('utf-16'))):
                path = Path(tmp) / name
                path.write_bytes(data)
                run = subprocess.run([sys.executable, str(ROOT/'scripts/hig_route.py'), '--request-file', str(path)],
                                     capture_output=True, env=env)
                self.assertEqual(run.returncode, 0, run.stderr)
                self.assertIn('tab-bars', json.loads(run.stdout.decode('utf-8'))['initial'])
            run = subprocess.run([sys.executable, str(ROOT/'scripts/hig_route.py'), '--request-file', str(Path(tmp)/'missing.txt')],
                                 capture_output=True, env=env)
            self.assertEqual(run.returncode, 2)
            self.assertNotIn(b'Traceback', run.stderr)

    def test_foundations_never_expand_and_direct_tier4_does_not_expand(self):
        result = router.route(ROOT, 'Explain a pleasant experience.')
        self.assertEqual(len(result['files']), 16)
        self.assertEqual(result['initial'], {})
        self.assertEqual(result['one_hop_related'], {})
        result = router.route(ROOT, 'CareKit')
        self.assertIn('carekit', result['direct_tier4'])
        self.assertNotIn('carekit', result['initial'])
        self.assertEqual(result['one_hop_related'], {})


if __name__ == '__main__':
    unittest.main()
