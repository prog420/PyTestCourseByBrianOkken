def pytest_addoption(parser):
    parser.addoption(
        "--func-db",
        action="store_true",
        help="change db fixture scope in runtime"
    )