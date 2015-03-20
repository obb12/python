first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')

sentence = [first_word, second_word, third_word]
class lexicon:
	
	@staticmethod
	def scan(s):
		
		direction = ("north", "west", "east", "south")
		verbs = ("go", "kill", "eat")
		stop = ("the", "in", "of")
		noun = ("bear","princess")
		num = ("3","91234","1234")
		s  = s.split()
		results = []
		for l in s:
			if l in direction:
				results.append(('direction', l))
			elif l in verbs:
				results.append(('verb', l))
			elif l in stop:
				results.append(('stop', l))
			elif l in noun:
				results.append(('noun', l))
			elif l in num:
				l = int(l)
				results.append(('number', l))
			else:
				results.append(('error', l))
		return results
