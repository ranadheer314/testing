from invoke.tasks import task

@task
def lint(c):
    c.run("ruff check --fix-only --exit-zero", echo=True)
    c.run


@task
def fmt(c):
    c.run("ruff format",echo=True)


@task
def build(c):
    c.run("poetry build")
