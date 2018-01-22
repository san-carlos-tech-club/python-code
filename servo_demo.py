#!/usr/bin/env python3

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
from gpiozero import Servo

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('maximum')
    recognizer.expect_phrase('minimum')
    recognizer.expect_phrase('middle')

    button = aiy.voicehat.get_button()
    aiy.audio.get_recorder().start()
    
    servo = Servo(13)

    while True: 
      print('press the button and speak')
      button.wait_for_press()
      print('eating pizza...')
      text = recognizer.recognize()
      if text is None:
        print('please repeat...')
      else:
        print('You said "', text, '"')
        if 'maximum' in text:
          print('moving servo to maximum')
          servo.max()
        elif 'minimum' in text:
          print('moving servo to minimum')
          servo.min()
        elif 'middle' in text:
          print('moving servo to middle')
          servo.mid()

if __name__ == '__main__':
    main()

