from dotenv import load_dotenv

load_dotenv()

# Main config class that is inherited by other configs
# fairly empty atm, but the point is we can easily add things to different configs
class Config:

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

# Choose config based on environment variable
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}