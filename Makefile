# Setup the project environment by:
# - Run pipenv shell to start the virtual env.
env:
	pipenv --python=${conda run which python} --site-packages
	pipenv shell 

# Install all libraries of package.
install-all:
	pipenv install --system --dev

# Install a package. 
install:
	pipenv install $(pkg)

# Install a package in dev mode.
install-dev:
	pipenv install --dev $(pkg)

# Run streamlit and talk with the assistant.
streamlit:
	python -m streamlit run ./bin/streamlit.py
