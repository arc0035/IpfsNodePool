import click
import launcher

# 定义一个组
@click.group()
def cli():
    pass

# 定义fetch命令
@click.command()
def fetch():
    launcher.fetcher.run_fetcher()

# 定义web命令
@click.command()
def web():
    print('Not implemented')

# 讲上述两个命令增加到组中
cli.add_command(fetch)
cli.add_command(web)
if __name__ == '__main__':
    cli()