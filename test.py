
# python test.py



import pkg_resources

def load_requirements(file_path):
    """Load requirements from a given requirements file."""
    with open(file_path, 'r') as f:
        # Read the lines, filter comments and whitespace
        requirements = [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]
    return requirements

def check_packages(packages):
    """Check if each package in the list is installed."""
    for package in packages:
        try:
            pkg_resources.require(package)
            print(f"{package} is installed.")
        except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict):
            print(f"{package} is NOT installed.")

if __name__ == "__main__":
    # Load requirements from requirements.txt
    requirements_file = 'requirements.txt'
    required_packages = load_requirements(requirements_file)

    print("Checking installed packages...\n")
    check_packages(required_packages)

# List of packages to check
# required_packages = [
#     "html5lib"
#     "PyPDF2"
#     "openai"
#     "webdriver-manager"
#     "setuptoolspandas"
#     "numpy"
#     "matplotlib"
#     "seaborn"
#     "plotly"
#     "scikit-learn"
#     "statsmodels"
#     "xgboost"
#     "requests"
#     "beautifulsoup4"
#     "bs4"
#     "lxml"
#     "yfinance"
#     "nltk"
#     "textblob"
#     "vaderSentiment"
#     "SQLAlchemy"
#     "python-dotenv"
#     "jupyter"
#     "ipykernel"
#     "twilio"
#     "streamlit"
#     "TA-Lib"
#     # Add any other required packages
# ]

# def check_packages(packages):
#     for package in packages:
#         try:
#             pkg_resources.require(package)
#             print(f"{package} is installed.")
#         except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict):
#             print(f"{package} is NOT installed.")

# if __name__ == "__main__":
#     print("Checking installed packages...\n")
#     check_packages(required_packages)

# python test.py