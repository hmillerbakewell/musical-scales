rm -rf ./docs/build
sphinx-apidoc -o docs/source/ ./src/musical_scales
sphinx-build -b html docs/source/ docs/build/