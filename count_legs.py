def count_legs(animal1, animal2, animal3):
    # YOUR CODE HERE
    return animal1 * 2 + animal2 * 4 + animal3 * 4

if __name__ == "__main__":
    animal1, animal2, animal3 = map(int, input().split())
    leg_count = count_legs(animal1, animal2, animal3)
    # YOUR CODE HERE
    print(leg_count)
