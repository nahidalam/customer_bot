'''
Author: Nahid Alam
Reference: https://github.com/JustinaPetr/Weatherbot_Tutorial
Works with Rasa NLU 0.12.3
'''

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configuration, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configuration))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'customernlu')
	return model_directory

def run_nlu(model_directory):
	#interpreter = Interpreter.load('./models/nlu/default/customernlu', RasaNLUModelConfig('config_spacy.yml'))
	interpreter = Interpreter.load(model_directory)
	print(interpreter.parse(u"I am planning my to order an 829 router. How much does it cost?"))

if __name__ == '__main__':
	model_directory = train_nlu('./data/data.json', 'config_spacy.yml', './models/nlu')
	run_nlu(model_directory)
