# Might need in future
def try_except(success, failure, *exceptions):
    try:
        return success()
    except exceptions or Exception:
        print("hi")
        return failure() if callable(failure) else failure
