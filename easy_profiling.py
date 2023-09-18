def test():
    return [x for x in range(100_000)]

def main(func):
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        func()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # If you want to see directly on code interpreter, but I'm going to use snakeviz to visualize the profiling.
    stats.print_stats()
    stats.dump_stats(filename="needs_profiling.prof")

main(test)