def info_kwargs(**kwargs):
    for k, v in sorted(kwargs.items()):
        print(f"{k}: {v}")


info_kwargs(first_name="Timur", last_name="Guev", age=28, job="teacher")
