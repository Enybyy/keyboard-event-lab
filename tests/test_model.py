import json
import unittest
from model import Session


class SessionTests(unittest.TestCase):
    def test_explicit_start_and_pause(self):
        s = Session()
        self.assertIsNone(s.record('A'))
        s.start()
        self.assertEqual(s.record('ñ','ñ').character, 'ñ')
        s.pause()
        self.assertIsNone(s.record('B'))
        self.assertEqual(len(s.events), 1)

    def test_bounded_history_and_sequence(self):
        s = Session(2)
        s.start()
        for key in 'ABC': s.record(key, key)
        self.assertEqual([e.sequence for e in s.events], [2,3])
        self.assertEqual([e.key for e in s.events], ['B','C'])

    def test_export_unicode_and_clear(self):
        s = Session()
        s.start()
        s.record('ñ', 'ñ')
        data = json.loads(s.export())
        self.assertEqual(data['events'][0]['character'], 'ñ')
        self.assertEqual(data['scope'], 'own input area')
        s.clear()
        self.assertEqual(json.loads(s.export())['events'], [])
        self.assertEqual(s.record('a').sequence, 1)

    def test_limit(self):
        with self.assertRaises(ValueError): Session(0)


if __name__ == '__main__': unittest.main()
