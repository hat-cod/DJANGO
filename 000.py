from sys import api_version


api_version = "1.0"
api_version_tuple = (1, 0)

__version__ = "1.0"

__all__ = ["api_version", "api_version_tuple", "__version__"]

print(api_version)
print(api_version_tuple)
print(__version__)
print(__all__)
    