#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self, knowledge = []):
        self.knowledge = knowledge



    def learn(self, word):
        self.knowledge.append(word)