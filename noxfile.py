
from nox import session, Session

@session
def weave(ctx: Session) -> None:
    """
    Weave and tangle the literate programs.
    """
    ctx.install('--pre', 'litprog')
    ctx.run('litprog,' 'build')