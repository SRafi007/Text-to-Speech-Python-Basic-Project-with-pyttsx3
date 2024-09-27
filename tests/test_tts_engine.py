import unittest
from app.tts_engine import init_tts_engine

class TestTTSEngine(unittest.TestCase):
    def test_engine_initialization(self):
        engine = init_tts_engine(rate=200, volume=1.0, voice_gender='male')
        self.assertIsNotNone(engine)
    
    def test_invalid_voice_gender(self):
        with self.assertRaises(ValueError):
            init_tts_engine(voice_gender='unknown')

if __name__ == '__main__':
    unittest.main()
