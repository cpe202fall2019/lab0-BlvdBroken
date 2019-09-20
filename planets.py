from pip._vendor.distlib.compat import raw_input


def weight_on_planets():
    weight = float(raw_input("What do you weigh on earth? "))
    print("On Mars you would weigh ", (weight * 0.38), " pounds.\nOn Jupiter you would weigh ", (weight * 2.38), "pounds.")


if __name__ == '__main__':
    weight_on_planets()