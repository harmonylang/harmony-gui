
all: dependencies
	rm -rf build/  # Remove previous build files
	pip3 install pyqt5
	pip3 install pillow
	pip3 install numpy
	python3 setup.py install


dependencies:
	pip3 install -r requirements.txt


dist:
	rm -rf build/ dist/ harmony_gui.egg-info/
	python3 setup.py sdist


upload-test: dist
	twine upload -r testpypi dist/*


upload: dist
	twine upload dist/*


clean:
	rm -rf build/ dist/ harmony_model_checker.egg-info/
