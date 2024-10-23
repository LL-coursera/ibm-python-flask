import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        #test whether the emotion_detector return the dominant_emotion of the json is equal to joy
        self.assertEquals(emotion_detector("I am glad this happened")['dominant_emotion'],'joy')
        #test whether the emotion_detector return the dominant_emotion of the json is equal to anger
        self.assertEquals(emotion_detector("I am really mad about this")['dominant_emotion'],'anger')
        #test whether the emotion_detector return the dominant_emotion of the json is equal to disgust
        self.assertEquals(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'],'disgust')
        #test whether the emotion_detector return the dominant_emotion of the json is equal to sadness
        self.assertEquals(emotion_detector("I am so sad about this")['dominant_emotion'],'sadness')
        #test whether the emotion_detector return the dominant_emotion of the json is equal to fear
        self.assertEquals(emotion_detector("I am really afraid that this will happen")['dominant_emotion'],'fear')
unittest.main()