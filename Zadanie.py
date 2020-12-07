#!/usr/bin/env python3
# -*- config: utf-8 -*-

if __name__ == '__main__':
    with open('text.txt', 'r')as f:
        text = f.read()

        text = text.replace("!", ".")
        text = text.replace("?", ".")

        while ".." in text:
            text.replace("..", ".")

        sentences = text.split(".")

        for sentence in sentences:
            if "," in sentence:
                with open('text.txt', 'r')as a:
                    a_text = a.read()
                    if sentence in a_text:
                        print(f'{sentence}{a_text[a_text.rfind(sentence)+len(sentence)]}')
