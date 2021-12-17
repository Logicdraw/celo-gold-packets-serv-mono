from setuptools import setup


setup(
	name='celo-gold-packets-serv-mono',
	version='1.1',
	py_modules=['cli', 'cli.commands'],
	install_requires=[
		'click',
	],
	entry_points='''
		[console_scripts]
		celo-gold-packets-serv-mono-cli=cli.cli:cli
	''',
)

