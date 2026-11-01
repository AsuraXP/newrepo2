import importlib.util
import unittest
from pathlib import Path
from types import SimpleNamespace

module_path = Path(__file__).resolve().parents[1] / 'kaggle_render.py'
spec = importlib.util.spec_from_file_location('story_render', module_path)
render = importlib.util.module_from_spec(spec)
spec.loader.exec_module(render)


def event(text, offset):
    return SimpleNamespace(type='WordBoundary', text=text, offset_s=offset, duration_s=0.1)


class WordAlignmentTests(unittest.TestCase):
    def test_split_possessive_and_contraction(self):
        events = [event('grandfather', 0.1), event("'s", 0.4), event('farm', 0.5),
                  event('isn', 0.8), event("'t", 1.0), event('safe', 1.2)]
        self.assertEqual(render.measured_cut_starts("Grandfather's farm isn't safe.", events, [0, 1, 2, 3]),
                         [0.1, 0.5, 0.8, 1.2])

    def test_combined_event_allowed_when_cut_is_on_event_boundary(self):
        events = [event('hello world', 0.1), event('again', 0.9)]
        self.assertEqual(render.measured_cut_starts('Hello world again.', events, [0, 2]), [0.1, 0.9])

    def test_combined_event_cannot_supply_interior_cut(self):
        with self.assertRaisesRegex(ValueError, 'inside a single TTS event'):
            render.measured_cut_starts('Hello world again.', [event('hello world', 0.1), event('again', 0.9)], [0, 1])

    def test_missing_word_is_not_ignored(self):
        with self.assertRaisesRegex(ValueError, 'differs near character'):
            render.measured_cut_starts('one two three', [event('one', 0.1), event('three', 0.3)], [0, 1])

    def test_out_of_order_rejected(self):
        with self.assertRaisesRegex(ValueError, 'out of order'):
            render.measured_cut_starts('one two', [event('one', 0.4), event('two', 0.2)], [0, 1])


if __name__ == '__main__':
    unittest.main()
