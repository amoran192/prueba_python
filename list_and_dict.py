def run():
    my_list =[1,"Hello", True, 4.5 ]
    my_dict = {"firsname": "Alejandro", "lastname": "Moran"}

    super_list = [
        {"firsname": "Alejandro", "lastname": "Moran"},
        {"firsname": "Facundo", "lastname": "Garcia"},
        {"firsname": "Manuel", "lastname": "Moran"},
        {"firsname": "Blanca ", "lastname": "Guapa"},
        {"firsname": "Pedro", "lastname": "Gonzalez"},

    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2,],
        "floating_nums": [1.1, 4.5, 6.33]

    }
    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()

