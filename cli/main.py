import argparse
from packages.core.engine import Engine
from services.orchestrator import Orchestrator
def main():
    parser = argparse.ArgumentParser(description='Hyperion Framework CLI')
    parser.add_argument('--start', action='store_true', help='Start the engine')
    args = parser.parse_args()
    if args.start:
        engine = Engine(None)
        orchestrator = Orchestrator(engine)
        orchestrator.start()