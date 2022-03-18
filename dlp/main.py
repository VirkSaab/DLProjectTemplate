import click
from pyfiglet import Figlet
from dlp import PROJ_DIR, ROOT_DIR
from dlp.utils import load_yaml

# Load project info
CONTEXT_SETTINGS = dict(auto_envvar_prefix="COMPLEX")
# Load Config file
CNF = load_yaml(ROOT_DIR/"configs/default.yaml")


# ----------------------------------------> CLI ::
# * Entry point
@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        # * BANNER
        # Find more fonts here: http://www.figlet.org/examples.html
        f = Figlet(font="slant")
        click.echo()
        banner = ' '.join(CNF.project_name.upper())
        # banner = f"..._ {banner} _..."
        click.secho(f"{f.renderText(banner)}", fg="yellow")
        print(
            f"""Welcome to {CNF.project_name.upper()} CLI
    Type `[yellow]{CNF.project_name.lower()} --help[/yellow]` for usage details
    """
        )
        print(ctx.get_help())

    else:
        click.secho(f"\n[@ {ctx.invoked_subcommand}] begin:", fg="cyan")


# ----------------------------------------> TESTS ::
@cli.command()
def run_tests():
    """Run code tests"""
    import subprocess
    subprocess.run(['pytest', f'{CNF.paths.tests_dir}'])