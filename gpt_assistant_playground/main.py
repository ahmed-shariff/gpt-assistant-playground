import click
import os
from loguru import logger
from environs import Env

env = Env()
env.read_env()

@click.command()
def main():
    print(env("OPENAI_API_KEY"))
    

