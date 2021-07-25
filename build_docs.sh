rm -rf ./docs/build
sphinx-apidoc -feo docs/source/ ./src/musical_scales
sphinx-build -aEb html docs/source/ docs/build/