# -*- coding: utf-8 -*
import helpers

def get_hmm():
    """Get a thought."""
    return "hmmm..."


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())


if __name__ == "__main__":
    print(get_hmm())
    hmm()
